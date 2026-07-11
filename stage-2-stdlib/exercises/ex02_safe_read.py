"""
练习 02：安全读文件

自检：python ex02_safe_read.py --check
"""

from __future__ import annotations

from pathlib import Path


def read_text_safe(path: str | Path) -> str | None:
    p = Path(path)
    try:
        return p.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"文件不存在: {p}")
        return None
    except OSError as e:
        print(f"读取失败: {e}")
        return None


def main() -> None:
    path = input("输入文件路径: ").strip()
    content = read_text_safe(path)
    if content is not None:
        print(content[:200])


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
def _selfcheck() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "a.txt"
        p.write_text("hello中文", encoding="utf-8")
        assert read_text_safe(p) == "hello中文"
        assert read_text_safe(Path(tmp) / "missing.txt") is None
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
