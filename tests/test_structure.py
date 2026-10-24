"""Fast repository structure smoke checks for TASK-002."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_shell_files_exist():
    for path in [
        "app.py",
        "components/state.py",
        "pages/home.py",
        "pages/onboarding.py",
        "pages/discovery.py",
        "pages/careers.py",
        "pages/roadmap.py",
        "pages/readiness.py",
        "pages/dashboard.py",
        "pages/change_path.py",
        "requirements.txt",
    ]:
        assert (ROOT / path).is_file(), path


def test_navigation_routes_present():
    source = (ROOT / "app.py").read_text(encoding="utf-8")
    for page in ("home", "onboarding", "discovery", "careers", "roadmap", "readiness", "dashboard", "change_path"):
        assert f"pages/{page}.py" in source
