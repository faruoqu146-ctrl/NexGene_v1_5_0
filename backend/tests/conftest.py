"""Isolate each test process on throwaway SQLite files under /tmp."""
import os

os.environ.setdefault("DEV_MODE", "true")
os.environ.setdefault("COOKIE_SECURE", "false")
os.environ.setdefault("CLINICAL_PROVIDER_KEY", "test-provider-key")
os.environ.setdefault("GENOMIC_PROVIDER_KEY", "test-genomic-key")
os.environ.setdefault("DATABASE_URL", "sqlite:////tmp/nexgene_pytest.db")
os.environ.setdefault("CLINICAL_DATABASE_URL", "sqlite:////tmp/nexgene_clinical_pytest.db")
os.environ.setdefault("GENOMIC_DATABASE_URL", "sqlite:////tmp/nexgene_genomic_pytest.db")
