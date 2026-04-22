from __future__ import annotations

from datetime import datetime
from typing import Iterable

from solution.domain.models import Entry


def choose_kept_sessions(entries: Iterable[Entry]) -> dict[str, tuple[datetime, str]]:
    """
    Duplicate Session IDs rule: keep only the first occurrence by timestamp.
    Ties are broken by source path for deterministic behavior.
    """
    kept: dict[str, tuple[datetime, str]] = {}

    for entry in entries:
        if entry.timestamp is None:
            continue

        candidate = (entry.timestamp, entry.source_file)
        current = kept.get(entry.session_id)
        if current is None or candidate < current:
            kept[entry.session_id] = candidate

    return kept
