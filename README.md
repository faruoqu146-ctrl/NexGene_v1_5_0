# NexGene v1.5.0

**NexGene** — personal health intelligence with clinical, genomic, and live evidence layers.

## What's new in v1.5.0 (Phase 8)

- **Genomic live intelligence**: structured genomic compartment + live evidence retrieval (PubMed / Crossref).
- **Clinical compartment**: isolated clinical data plane with contract tests.
- **Learning cycle**: offline/online learning script for evidence synthesis.
- Security-hardened FastAPI backend, mobile UI, full test suite (fixed and passing).

## Quick start

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Or Docker
docker compose up --build
```

Mobile UI: open `mobile/index.html` (or serve the `mobile/` folder).

## Structure

- `backend/` — FastAPI app (`app/main.py`), requirements, tests
- `mobile/` — frontend (app.js, index.html, styles.css)
- `docs/` — phase architecture notes (5–8)
- `knowledge/` — evidence schema
- `scripts/learning_cycle.py` — learning / evidence cycle

## Tests

```bash
cd backend
pytest -v
```

All contract, security, clinical, intelligence, and v1.5 tests are expected to pass after this fixed package.

## License / status

Private development prototype. Not for clinical use.
