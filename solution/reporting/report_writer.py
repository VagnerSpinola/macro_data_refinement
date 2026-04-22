from __future__ import annotations

from collections import Counter
from pathlib import Path

from solution.reporting.methodology import build_methodology_text


def write_report(
    output_path: Path,
    total_entries: int,
    valid_entries: int,
    invalid_counts: Counter[str],
    final_sum: float,
) -> None:
    lines: list[str] = []
    lines.append("Macro Data Refinement - Final Report")
    lines.append("===================================")
    lines.append("")
    lines.append("Objective")
    lines.append("---------")
    lines.append("Calculate the sum of all valid entry values across all departments.")
    lines.append("")
    lines.append("Results")
    lines.append("-------")
    lines.append(f"Total entries scanned: {total_entries}")
    lines.append(f"Valid entries: {valid_entries}")
    lines.append(f"Invalid entries: {total_entries - valid_entries}")
    lines.append(f"Final sum (valid entries only): {final_sum:.2f}")
    lines.append("")
    lines.append("Anomaly Summary (invalid by first failing rule)")
    lines.append("-----------------------------------------------")
    for reason, count in invalid_counts.most_common():
        lines.append(f"- {reason}: {count}")

    lines.append("")
    lines.append(build_methodology_text())
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
