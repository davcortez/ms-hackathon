from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Match API"

    environment: str
    gemini_api_key: str

    cors_allow_credentials: bool = False
    cors_http_methods: list
    cors_headers: list
    cors_origins: list

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
