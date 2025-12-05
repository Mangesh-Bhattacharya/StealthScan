# utils/validators.py
"""
Input validators for the safe simulator.
Do not attempt to resolve or ping hosts here — only simple syntactic checks.
"""

import re
from typing import List

HOSTNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,253}$")

def validate_target(target: str) -> bool:
    if not target:
        return False
    # simple check: allow hostnames, 'localhost', or labels
    if target.lower() == "localhost":
        return True
    if HOSTNAME_RE.match(target):
        return True
    return False

def validate_targets(targets: List[str]) -> List[str]:
    invalid = [t for t in targets if not validate_target(t)]
    return invalid
# --- end of validators.py ---
