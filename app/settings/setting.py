from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEV = "dev"
    HOMOLOG = "homolog"
    PROD = "prod"


class AppEnvironmentSettings(BaseSettings):
    environment: Environment = Environment.DEV

    model_config = {
        "env_prefix": "APP_",
        "extra": "forbid",
    }


class DatabaseSettings(BaseSettings):
    url_dev: str
    url_homolog: str
    url_prod: str

    model_config = {"env_prefix": "DATABASE_"}

    def get_current_url(self) -> str:
        environment = get_settings().env.environment

        if environment == Environment.HOMOLOG and self.url_homolog:
            return self.url_homolog
        elif environment == Environment.PROD and self.url_prod:
            return self.url_prod
        return self.url_dev


class SentrySettings(BaseSettings):
    dns: str

    model_config = {
        "env_prefix": "SENTRY_",
        "extra": "forbid",
    }


class Settings(BaseSettings):
    env: AppEnvironmentSettings = AppEnvironmentSettings()
    database: DatabaseSettings = DatabaseSettings()
    sentry: SentrySettings = SentrySettings()

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
        "extra": "allow",
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
