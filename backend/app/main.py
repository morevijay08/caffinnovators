
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.api.interest_assessment import router as interest_router
from app.api.careers import router as careers_router
from app.api.recommendations import router as recommendations_router
from app.api.discovery import router as discovery_router
from app.api.math_assessment import router as math_assessment_router
from app.api.student import router as student_router
from app.api.career_assistant import router as assistant_router
from app.db import init_db

app = FastAPI(title="LifePath India API", version="0.1.0")

app.include_router(interest_router)
app.include_router(careers_router)
app.include_router(recommendations_router)
app.include_router(discovery_router)
app.include_router(math_assessment_router)
app.include_router(student_router)
app.include_router(assistant_router)

frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
# Vite falls back to another port if 5173 is occupied; allow loopback dev origins only.
local_vite_origins = [f"http://{host}:{port}" for host in ("localhost", "127.0.0.1") for port in range(5173, 5181)]
allowed_frontend_origins = list(dict.fromkeys([frontend_origin, *local_vite_origins]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_frontend_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH"],
    allow_headers=["Content-Type"],
)


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="lifepath-api")


@app.on_event("startup")
def initialize_database() -> None:
    """Initialize SQLite tables for anonymous assessment result snapshots."""
    init_db()
