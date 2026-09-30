# NexGene v1.5.0

## Phase 8: Genomic + Live Evidence Intelligence Foundation

v1.5.0 extends the clinical-compartment architecture with a separate genomic compartment, live scholarly retrieval, live environmental context, and a recurring versioned learning cycle.

### New layers

- **Genomic compartment**: separate database, opaque subject references, dual authorization, genomic variants, and polygenic scores with provenance.
- **Live evidence retrieval**: PubMed/NCBI E-utilities and Crossref metadata adapters.
- **Live context**: configurable weather/context retrieval based on user-configured city/country.
- **Recurring learning**: deterministic 90-day personal baseline cycle with model/version provenance.
- **Learning status**: `/api/v1/intelligence/learning/status` exposes recent learning artifacts for the authenticated user.

### Long-term intelligence direction

```text
Lifestyle + Physiological + Molecular + Clinical + Genetic
                         ↓
                 Data quality / provenance
                         ↓
                 Personal longitudinal models
                         ↓
             Live evidence + research retrieval
                         ↓
                  Evidence-weighted inference
                         ↓
                    Safety / escalation
                         ↓
                 Factual AI synthesis layer
```

The AI layer is downstream of structured evidence. It is not the source of truth and is not a substitute for clinical judgment.

### Development configuration

Copy `.env.example` and set values as needed:

```bash
GENOMIC_DATABASE_URL=sqlite:///./nexgene_genomic.db
GENOMIC_PROVIDER_ID=development-genomics-provider
GENOMIC_PROVIDER_KEY=replace-with-a-local-development-secret
LIVE_CONTEXT_ENABLED=true
EVIDENCE_LIVE_ENABLED=true
NCBI_EMAIL=your-contact@example.com
NCBI_API_KEY=optional
CROSSREF_MAILTO=your-contact@example.com
```

### Run

```bash
docker compose up --build
```

Local API:

```bash
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Tests:

```bash
DEV_MODE=true python -m pytest backend/tests -v
```

All 21 tests pass after the v1.5.0 debug pass (SQLite timezone-safe comparisons, valid dummy password hash, DEV_MODE rate limits, contract tests updated).

### Important boundaries

- No full genomic interpretation or clinical decision support is claimed by this release.
- Live evidence retrieval is metadata-first; it does not grant unrestricted rights to copyrighted full text.
- Live context is contextual information, not a diagnostic measurement.
- Clinical and genomic compartments remain separately authorized.
- The current mobile UI remains frozen while testing continues.

## Version

`APP_VERSION = 1.5.0`
