import pytest
from pytest import MonkeyPatch

from secret_server.config import base


@pytest.fixture(autouse=True)
def _patch_settings(monkeypatch: MonkeyPatch) -> None:
    """Path the settings."""

    def get_settings(dotenv_filename: str = ".env.testing") -> base.Settings:
        return base.Settings.from_env(dotenv_filename=dotenv_filename)

    monkeypatch.setattr(base, "get_settings", get_settings)
