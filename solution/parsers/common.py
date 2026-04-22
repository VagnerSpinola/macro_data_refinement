from __future__ import annotations

from datetime import datetime


def parse_timestamp(raw: str) -> datetime | None:
    value = str(raw).strip()
    if not value:
        return None

    try:
        if "T" in value:
            return datetime.fromisoformat(value)
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None


def parse_float(raw: object) -> float | None:
    try:
        return float(raw)
    except Exception:
        return None
