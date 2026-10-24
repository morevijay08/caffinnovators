"""Password hashing and opaque session helpers; avoid storing plaintext tokens."""
import hashlib
import hmac
import os
import secrets
import time
from datetime import datetime, timezone
from uuid import uuid4
from fastapi import Cookie, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.student import Student, StudentSession

SESSION_SECONDS = 60 * 60 * 24 * 7
COOKIE_NAME = "lifepath_session"

def hash_password(password: str, salt: bytes | None = None) -> str:
    salt = salt or os.urandom(16)
    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 310_000)
    return "pbkdf2_sha256$310000$" + salt.hex() + "$" + derived.hex()

def verify_password(password: str, encoded: str) -> bool:
    try:
        scheme, iterations, salt_hex, hash_hex = encoded.split("$")
        if scheme != "pbkdf2_sha256":
            return False
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt_hex), int(iterations))
        return hmac.compare_digest(actual, bytes.fromhex(hash_hex))
    except (ValueError, TypeError):
        return False

def issue_session(db: Session, student_id: str) -> str:
    token = secrets.token_urlsafe(32)
    db.add(StudentSession(token_hash=hashlib.sha256(token.encode()).hexdigest(), student_id=student_id,
                          expires_at=int(time.time()) + SESSION_SECONDS))
    db.commit()
    return token

def resolve_student(db: Session, token: str | None) -> Student | None:
    if not token:
        return None
    row = db.get(StudentSession, hashlib.sha256(token.encode()).hexdigest())
    if row is None or row.expires_at <= int(time.time()):
        return None
    return db.get(Student, row.student_id)

def current_student(
    lifepath_session: str | None = Cookie(default=None),
    db: Session = Depends(get_db),
) -> Student:
    student = resolve_student(db, lifepath_session)
    if not student:
        raise HTTPException(status_code=401, detail="Please sign in to save or view your journey.")
    return student

def require_same_origin(request: Request) -> None:
    """Protect cookie-based writes against cross-site browser requests."""
    origin = request.headers.get("origin")
    expected = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173").rstrip("/")
    from urllib.parse import urlsplit
    allowed = origin is None or origin.rstrip("/") == expected
    if origin and not allowed:
        parsed = urlsplit(origin)
        allowed = (parsed.scheme == "http" and parsed.hostname in ("localhost", "127.0.0.1")
                   and parsed.port is not None and 5173 <= parsed.port <= 5180
                   and not parsed.username and not parsed.password)
    if not allowed:
        raise HTTPException(status_code=403, detail="Request origin not allowed.")
