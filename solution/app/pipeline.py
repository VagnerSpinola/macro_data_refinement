from __future__ import annotations

from collections import Counter
from pathlib import Path

from solution.parsers.loader import load_entries
from solution.reporting.report_writer import write_report
from solution.validation.duplicates import choose_kept_sessions
from solution.validation.validator import validate_entry


def run_pipeline(base_dir: Path) -> tuple[float, int, int, Counter[str], Path]:
    sessions_root = base_dir / "quarterly_output" / "sessions"
    report_path = base_dir / "final_report.txt"

    entries = load_entries(sessions_root)
    kept_sessions = choose_kept_sessions(entries)

    invalid_counts: Counter[str] = Counter()
    valid_entries = 0
    final_sum = 0.0

    for entry in entries:
        result = validate_entry(entry, kept_sessions)
        if result.is_valid:
            valid_entries += 1
            final_sum += float(entry.value)
        else:
            invalid_counts[result.reason or "unknown_invalid_reason"] += 1

    write_report(
        output_path=report_path,
        total_entries=len(entries),
        valid_entries=valid_entries,
        invalid_counts=invalid_counts,
        final_sum=final_sum,
    )

    return final_sum, len(entries), valid_entries, invalid_counts, report_path
