"""Runtime configuration for the viewer bot."""
from __future__ import annotations

import os
from pathlib import Path
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseModel):
    user_agent_pool: str = Field(default="mobile")
    request_timeout: int = 15
    retry_attempts: int = 3
    delay_min_ms: int = 800
    delay_max_ms: int = 2400
    proxy_file: Path = BASE_DIR / "data" / "proxies.txt"
    session_dir: Path = BASE_DIR / "data" / "sessions"
    log_level: str = "INFO"
    max_views_per_session: int = 5


def load_settings() -> Settings:
    return Settings(
        user_agent_pool=os.getenv("TTVB_UA_POOL", "mobile"),
        request_timeout=int(os.getenv("TTVB_TIMEOUT", "15")),
        retry_attempts=int(os.getenv("TTVB_RETRIES", "3")),
        log_level=os.getenv("TTVB_LOG_LEVEL", "INFO"),
    )