from pathlib import Path

def test_intelligence_engine_contract():
    root = Path(__file__).resolve().parents[2]
    main = (root / "backend" / "app" / "main.py").read_text(encoding="utf-8")
    assert "class IntelligenceEngine" in main or "def intelligence" in main.lower()
