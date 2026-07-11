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


if __name__ == "__main__":
    main()
