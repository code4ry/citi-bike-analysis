# src/citibike_forecaster/config.py
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Read a .env file if one exists; ignore unrelated variables in it
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Each field maps to an env var with the same name, uppercased:
    # database_url <- DATABASE_URL, poll_seconds <- POLL_SECONDS, etc.
    database_url: str = "postgresql+psycopg://citibike:change-me@localhost:5432/citibike"
    gbfs_index_url: str = "https://gbfs.citibikenyc.com/gbfs/2.3/gbfs.json"
    poll_seconds: int = 900
    model_path: str = "models/model.json"

    weather_lat: float = 40.73
    weather_lon: float = -73.99


@lru_cache
def get_settings() -> Settings:
    return Settings()