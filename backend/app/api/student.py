"""Cookie-authenticated student journey API (no emails or full names)."""
import hashlib
import json
import os
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from pydantic import TypeAdapter, ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.student import Student, StudentJourney, StudentSession
from app.schemas.student import (
    Assessment, ChatMessage, Credentials, JourneyData, JourneyPatch, PathChange, Profile, StudentIdentity,
)
from app.services.student_auth import COOKIE_NAME, SESSION_SECONDS, current_student, hash_password, issue_session, require_same_origin, resolve_student, verify_password

router = APIRouter(prefix="/api/v1", tags=["student accounts"])
FIELDS = {
    "profile": TypeAdapter(Profile | None),
    "assessment": TypeAdapter(Assessment | None),
    "selectedCareerId": TypeAdapter(str | None),
    "pathHistory": TypeAdapter(list[PathChange]),
    "reflections": TypeAdapter(dict[str,str]),
    "chatHistory": TypeAdapter(list[ChatMessage]),
}

def set_cookie(response: Response, token: str):
    response.set_cookie(key=COOKIE_NAME, value=token, max_age=SESSION_SECONDS,
        httponly=True, secure=os.getenv("COOKIE_SECURE", "0") == "1",
        samesite="lax", path="/")

def get_state(db: Session, student_id: str) -> StudentJourney:
    row = db.get(StudentJourney, student_id)
    if row is None:
        row = StudentJourney(student_id=student_id, path_history_json="[]", reflections_json="{}", chat_history_json="[]")
        db.add(row)
        db.flush()
    return row

def public_state(row: StudentJourney) -> JourneyData:
    return JourneyData(
        profile=json.loads(row.profile_json) if row.profile_json else None,
        assessment=json.loads(row.assessment_json) if row.assessment_json else None,
        selectedCareerId=row.selected_career_id,
        pathHistory=json.loads(row.path_history_json),
        reflections=json.loads(row.reflections_json),
        chatHistory=json.loads(row.chat_history_json),
    )

@router.post("/auth/register", response_model=StudentIdentity, status_code=201)
def register(credentials: Credentials, response: Response, request: Request, db: Session = Depends(get_db)):
    require_same_origin(request)
    student = Student(id=str(uuid4()), username=credentials.username,
                      password_hash=hash_password(credentials.password),
                      created_at=datetime.now(timezone.utc).isoformat())
    db.add(student)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(409, "This username is already taken.") from exc
    token = issue_session(db, student.id)
    set_cookie(response, token)
    return StudentIdentity(id=student.id, username=student.username)

@router.post("/auth/login", response_model=StudentIdentity)
def login(credentials: Credentials, response: Response, request: Request, db: Session = Depends(get_db)):
    require_same_origin(request)
    student = db.scalar(select(Student).where(Student.username == credentials.username))
    if not student or not verify_password(credentials.password, student.password_hash):
        raise HTTPException(401, "Invalid username or password.")
    token = issue_session(db, student.id)
    set_cookie(response, token)
    return StudentIdentity(id=student.id, username=student.username)

@router.get("/auth/me", response_model=StudentIdentity)
def me(student: Student = Depends(current_student)):
    return StudentIdentity(id=student.id, username=student.username)

@router.post("/auth/logout", status_code=204)
def logout(request: Request, response: Response, db: Session = Depends(get_db)):
    require_same_origin(request)
    token = request.cookies.get(COOKIE_NAME)
    if token:
        db.delete(db.get(StudentSession, hashlib.sha256(token.encode()).hexdigest())) if db.get(StudentSession, hashlib.sha256(token.encode()).hexdigest()) else None
        db.commit()
    response.delete_cookie(COOKIE_NAME, path="/")

@router.get("/journey", response_model=JourneyData)
def journey(student: Student = Depends(current_student), db: Session = Depends(get_db)):
    row = get_state(db, student.id)
    result = public_state(row)
    db.commit()
    return result

@router.patch("/journey", response_model=JourneyData)
def patch_journey(patch: JourneyPatch, request: Request, student: Student = Depends(current_student), db: Session = Depends(get_db)):
    require_same_origin(request)
    try:
        parsed = FIELDS[patch.field].validate_python(patch.value)
        if patch.field == "selectedCareerId" and parsed is not None and len(parsed) > 100:
            raise ValueError("Career ID is too long.")
        if patch.field == "pathHistory" and len(parsed) > 100:
            raise ValueError("Path history is too long.")
        if patch.field == "chatHistory" and len(parsed) > 20:
            raise ValueError("Chat history is too long.")
        if patch.field == "reflections" and (len(parsed)>50 or any(len(k)>100 or len(v)>800 for k,v in parsed.items())):
            raise ValueError("Reflections exceed limits.")
    except (ValidationError, ValueError) as exc:
        raise HTTPException(422, "Invalid saved journey data.") from exc
    row = get_state(db, student.id)
    if patch.field == "profile":
        row.profile_json = parsed.model_dump_json() if parsed is not None else None
    elif patch.field == "assessment":
        row.assessment_json = parsed.model_dump_json() if parsed is not None else None
    elif patch.field == "selectedCareerId":
        row.selected_career_id = parsed
    else:
        attr = {"pathHistory":"path_history_json","reflections":"reflections_json","chatHistory":"chat_history_json"}[patch.field]
        setattr(row, attr, json.dumps([v.model_dump() for v in parsed] if patch.field in ("pathHistory","chatHistory") else parsed))
    db.commit()
    return public_state(row)
