from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAIN = (ROOT / "backend" / "app" / "main.py").read_text(encoding="utf-8")

def test_app_version():
    assert "APP_VERSION" in MAIN
    assert "1.5.0" in MAIN

def test_genomic_compartment_present():
    assert "genomic" in MAIN.lower()

def test_learning_status_route():
    assert "/api/v1/intelligence/learning/status" in MAIN or "learning/status" in MAIN
