"""URL and input validation helpers."""
from __future__ import annotations

import re

_TIKTOK_RE = re.compile(r"^https?://(www\.)?tiktok\.com/@[\w.\-]+/video/\d+")


def is_valid_tiktok_url(url: str) -> bool:
    return bool(_TIKTOK_RE.match(url.strip()))


def parse_view_count(raw: str) -> int:
    raw = raw.strip().lower()
    if raw.endswith("k"):
        return int(float(raw[:-1]) * 1_000)
    if raw.endswith("m"):
        return int(float(raw[:-1]) * 1_000_000)
    return int(raw)