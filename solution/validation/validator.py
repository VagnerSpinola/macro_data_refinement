from __future__ import annotations

from datetime import datetime

from solution.config.rules import (
    ALLOWED_BINS,
    ALLOWED_CATEGORIES,
    ALLOWED_DEPARTMENTS,
    ALLOWED_PROCESSORS,
    AUTHORIZED_BINS_BY_DEPARTMENT,
    NORA_TERMINATION_CUTOFF,
    Q4_2025_END,
    Q4_2025_START,
)
from solution.domain.models import Entry, ValidationResult


def validate_entry(entry: Entry, kept_sessions: dict[str, tuple[datetime, str]]) -> ValidationResult:
    if entry.timestamp is None:
        return ValidationResult(False, "invalid_timestamp_format")
    if entry.value is None:
        return ValidationResult(False, "invalid_value_format")

    kept = kept_sessions.get(entry.session_id)
    if kept is not None and (entry.timestamp, entry.source_file) != kept:
        return ValidationResult(False, "duplicate_session_id")

    if entry.department not in ALLOWED_DEPARTMENTS:
        return ValidationResult(False, "invalid_department")

    if entry.processor not in ALLOWED_PROCESSORS:
        return ValidationResult(False, "invalid_processor")

    if entry.bin_code not in ALLOWED_BINS:
        return ValidationResult(False, "invalid_bin")

    if entry.category not in ALLOWED_CATEGORIES:
        return ValidationResult(False, "invalid_category")

    if entry.value <= 0:
        return ValidationResult(False, "value_not_positive")

    if not (Q4_2025_START <= entry.timestamp <= Q4_2025_END):
        return ValidationResult(False, "timestamp_out_of_q4_2025")

    if entry.processor == "Nora.K" and entry.timestamp > NORA_TERMINATION_CUTOFF:
        return ValidationResult(False, "nora_k_after_termination")

    if entry.bin_code == "SP" and entry.department != "SA":
        return ValidationResult(False, "sp_outside_sa")

    allowed_bins = AUTHORIZED_BINS_BY_DEPARTMENT[entry.department]
    if entry.bin_code not in allowed_bins:
        return ValidationResult(False, "unauthorized_department_bin_matrix")

    if entry.value >= 1000.0:
        return ValidationResult(False, "value_ceiling_violation")

    if entry.timestamp.weekday() >= 5:
        return ValidationResult(False, "weekend_session")

    return ValidationResult(True)
