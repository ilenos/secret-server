from __future__ import annotations

import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path


@dataclass
class SecretServerSettings:

    host: str = field(default=os.getenv("SECRET_SERVER_HOST"))
    log_level: str = field(default_factory=lambda: os.getenv("SECRET_SERVER_LOG_LEVEL", "INFO"))


@dataclass
class Settings:
    secret_server: SecretServerSettings = field(default_factory=SecretServerSettings)

    @classmethod
    def from_env(cls, dotenv_filename: str = ".env") -> Settings:

        env_file = Path(__file__).parent.parent.parent.parent.joinpath(dotenv_filename)
        if env_file.is_file():
            from dotenv import load_dotenv
            # console.print(f"[yellow]Loading environment configuration from {dotenv_filename}[/]")
            load_dotenv(env_file.resolve())
        return Settings()


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    return Settings.from_env()
