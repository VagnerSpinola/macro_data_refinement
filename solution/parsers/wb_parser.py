from __future__ import annotations

from pathlib import Path

from solution.domain.models import Entry
from solution.parsers.common import parse_float, parse_timestamp


def parse_wb(path: Path) -> list[Entry]:
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]

    metadata: dict[str, str] = {}
    data_lines: list[dict[str, str]] = []

    for line in lines:
        if "|" not in line and ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip().upper()] = value.strip()
            continue

        if "|" in line:
            item: dict[str, str] = {}
            for chunk in line.split("|"):
                if ":" not in chunk:
                    continue
                key, value = chunk.split(":", 1)
                item[key.strip().upper()] = value.strip()
            if item:
                data_lines.append(item)

    timestamp = parse_timestamp(metadata.get("TIMESTAMP", ""))

    out: list[Entry] = []
    for item in data_lines:
        out.append(
            Entry(
                session_id=str(metadata.get("SESSION", "")).strip(),
                processor=str(metadata.get("PROCESSOR", "")).strip(),
                department=str(metadata.get("DEPARTMENT", "")).strip(),
                timestamp=timestamp,
                ref=str(item.get("REF", "")).strip(),
                bin_code=str(item.get("BIN", "")).strip(),
                value=parse_float(item.get("READING")),
                category=str(item.get("TYPE", "")).strip(),
                source_file=str(path),
            )
        )
    return out
