from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Entry:
    session_id: str
    processor: str
    department: str
    timestamp: datetime | None
    ref: str
    bin_code: str
    value: float | None
    category: str
    source_file: str


@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    reason: str | None = None
