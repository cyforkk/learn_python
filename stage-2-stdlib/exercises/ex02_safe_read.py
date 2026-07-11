"""
练习 02：安全读文件

自检：python ex02_safe_read.py --check
"""

from __future__ import annotations

from pathlib import Path


def read_text_safe(path: str | Path) -> str | None:
    # TODO
    raise NotImplementedError


def main() -> None:
    # TODO
    pass


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

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
