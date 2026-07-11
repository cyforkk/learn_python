"""
【本文件全是测试 · 新手可整文件后看】

文件名以 test_ 开头，函数名以 test_ 开头 → 这是 pytest 的「测试函数」。
作用：自动检查 stats.py 里的 mean / clamp 写得对不对。

- 你要学的功能在 stats.py，不在本文件
- 不会写测试也可以：只改 stats.py，用 print 自己验证
- 学有余力再运行: pytest -q

运行：
  pip install pytest
  cd stage-3-engineering/exercises/ex03_pytest_stats
  pytest -q
"""

import pytest

from stats import clamp, mean


# ----- 以下每个 test_xxx 都是【测试函数】，不是业务功能 -----


def test_mean_normal() -> None:
    # 测试：正常列表的平均值
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_empty() -> None:
    # 测试：空列表应报错
    with pytest.raises(ValueError):
        mean([])


def test_clamp_middle() -> None:
    # 测试：中间值不变
    assert clamp(5, 0, 10) == 5


def test_clamp_edges() -> None:
    # 测试：超出上下界时被截断
    assert clamp(-1, 0, 10) == 0
    assert clamp(99, 0, 10) == 10
