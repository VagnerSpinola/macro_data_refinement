from __future__ import annotations


def build_methodology_text() -> str:
    return (
        "Methodology\n"
        "-----------\n"
        "This solution processes all session files recursively from quarterly_output/sessions and does not rely on folder names for data meaning. "
        "Each record is normalized into a unified Entry model with the canonical fields required by the challenge: session_id, processor, department, "
        "timestamp, ref, bin, value, and category. Three parsers are implemented to support the official formats: JSON (.mdr), CSV (.csv), and "
        "pipe-delimited text (.txt). Parsing is defensive, so malformed timestamps and non-numeric values are not allowed to crash the run; they are "
        "classified as invalid and tracked in the anomaly summary.\n\n"
        "Validation is applied as a deterministic rules engine and follows the published sequence: the six Processing Manual rules plus all supplementary "
        "Compliance Annex rules. The script enforces department, processor, bin, and category whitelists; positive values; Q4-2025 date boundaries; "
        "Nora.K termination cutoff; SP bin restriction to SA; department-bin authorization matrix; strict value ceiling (<1000.00); and weekday-only sessions.\n\n"
        "Duplicate session handling is implemented at dataset level, as requested by the annex. For each session_id, only the earliest occurrence by timestamp "
        "is retained. Any later occurrence with the same session_id is excluded. Tie-breaking is deterministic by source file path to guarantee reproducible "
        "results between runs.\n\n"
        "The final output metric is computed as the sum of values from all valid entries only. In parallel, the script produces an anomaly distribution by "
        "first-failing rule, enabling clear auditability of removals. This keeps the calculation transparent, testable, and ready for technical review."
    )
