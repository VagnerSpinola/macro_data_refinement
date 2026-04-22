from __future__ import annotations

from datetime import datetime


ALLOWED_DEPARTMENTS = {"MDR", "SA", "WB"}
ALLOWED_PROCESSORS = {
    "James.L",
    "Nora.K",
    "Arthur.B",
    "Lena.P",
    "Felix.G",
    "Dr.Voss",
    "Clara.M",
}
ALLOWED_BINS = {"GR", "BL", "AX", "SP"}
ALLOWED_CATEGORIES = {"alpha", "beta", "gamma", "delta"}

AUTHORIZED_BINS_BY_DEPARTMENT = {
    "MDR": {"GR", "BL", "AX"},
    "SA": {"SP", "BL"},
    "WB": {"GR", "AX"},
}

Q4_2025_START = datetime(2025, 10, 1, 0, 0, 0)
Q4_2025_END = datetime(2025, 12, 31, 23, 59, 59)
NORA_TERMINATION_CUTOFF = datetime(2025, 11, 15, 23, 59, 59)
