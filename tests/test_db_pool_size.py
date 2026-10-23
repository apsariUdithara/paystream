import importlib
import pytest
from paystream.database import config

def test_pool_size_exceeds_max_connections_raises(monkeypatch):
    """Setting a pool size that would exceed the DB max connections should fail fast."""
    monkeypatch.setenv("PAYSTREAM_DB_POOL_SIZE", "100")
    monkeypatch.setenv("PAYSTREAM_INSTANCES", "5")
    monkeypatch.setenv("PAYSTREAM_DB_MAX_CONNECTIONS", "100")
    with pytest.raises(ValueError) as excinfo:
        importlib.reload(config)
    assert "DB_POOL_SIZE * INSTANCES" in str(excinfo.value)
