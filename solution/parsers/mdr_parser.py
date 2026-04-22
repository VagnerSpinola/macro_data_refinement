from __future__ import annotations

import json
from pathlib import Path

from solution.domain.models import Entry
from solution.parsers.common import parse_float, parse_timestamp


def parse_mdr(path: Path) -> list[Entry]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    timestamp = parse_timestamp(payload.get("timestamp", ""))

    out: list[Entry] = []
    for item in payload.get("entries", []):
        out.append(
            Entry(
                session_id=str(payload.get("session_id", "")).strip(),
                processor=str(payload.get("processor", "")).strip(),
                department=str(payload.get("department", "")).strip(),
                timestamp=timestamp,
                ref=str(item.get("ref", "")).strip(),
                bin_code=str(item.get("bin", "")).strip(),
                value=parse_float(item.get("value")),
                category=str(item.get("category", "")).strip(),
                source_file=str(path),
            )
        )
    return out
