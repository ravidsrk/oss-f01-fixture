"""Tiny stats helpers."""


def mean(xs: list[float]) -> float:
    """Arithmetic mean; 0.0 for an empty input."""
    if not xs:
        return 0.0
    return sum(xs) / len(xs)


def percent(part: float, whole: float) -> float:
    """Return ``part`` as a percentage of ``whole`` (0-100 scale)."""
    if whole == 0:
        return 0.0
    return part / whole
