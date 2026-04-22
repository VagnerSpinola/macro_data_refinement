from __future__ import annotations

from pathlib import Path

from solution.domain.models import Entry
from solution.parsers.mdr_parser import parse_mdr
from solution.parsers.sa_parser import parse_sa
from solution.parsers.wb_parser import parse_wb


def load_entries(sessions_root: Path) -> list[Entry]:
    entries: list[Entry] = []

    for path in sessions_root.rglob("*"):
        if not path.is_file():
            continue

        suffix = path.suffix.lower()
        if suffix == ".mdr":
            entries.extend(parse_mdr(path))
        elif suffix == ".csv":
            entries.extend(parse_sa(path))
        elif suffix == ".txt":
            entries.extend(parse_wb(path))

    return entries
