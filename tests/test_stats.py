"""Baseline tests (green before the fix)."""
from oss_f01.stats import mean, percent


def test_mean_basic():
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_empty():
    assert mean([]) == 0.0


def test_percent_zero_whole():
    assert percent(5.0, 0.0) == 0.0

