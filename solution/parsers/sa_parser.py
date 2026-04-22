from __future__ import annotations

import csv
from pathlib import Path

from solution.domain.models import Entry
from solution.parsers.common import parse_float, parse_timestamp


def parse_sa(path: Path) -> list[Entry]:
    out: list[Entry] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            out.append(
                Entry(
                    session_id=str(row.get("session_id", "")).strip(),
                    processor=str(row.get("processor", "")).strip(),
                    department=str(row.get("department", "")).strip(),
                    timestamp=parse_timestamp(row.get("timestamp", "")),
                    ref=str(row.get("ref", "")).strip(),
                    bin_code=str(row.get("bin", "")).strip(),
                    value=parse_float(row.get("output_metric")),
                    category=str(row.get("classification", "")).strip(),
                    source_file=str(path),
                )
            )
    return out
