"""
练习 03：pytest 用例

运行：
  pip install pytest
  cd stage-3-engineering/exercises/ex03_pytest_stats
  pytest -q
"""

import pytest

from stats import clamp, mean


def test_mean_normal() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_empty() -> None:
    with pytest.raises(ValueError):
        mean([])


def test_clamp_middle() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_edges() -> None:
    assert clamp(-1, 0, 10) == 0
    assert clamp(99, 0, 10) == 10
