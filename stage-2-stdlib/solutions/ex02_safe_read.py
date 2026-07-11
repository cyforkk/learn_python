"""参考答案：ex02 安全读文件。"""

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
