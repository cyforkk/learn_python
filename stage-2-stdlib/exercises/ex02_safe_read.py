"""
练习 02：安全读文件

要求：
1. 编写 read_text_safe(path: str | Path) -> str | None
   - 文件存在：返回全文（encoding=utf-8）
   - 文件不存在：打印提示，返回 None
   - 其他 OSError：打印错误，返回 None
2. main 中读取一个用户输入的路径并打印前 200 个字符

运行：python ex02_safe_read.py
"""

from __future__ import annotations

from pathlib import Path


def read_text_safe(path: str | Path) -> str | None:
    # TODO
    raise NotImplementedError


def main() -> None:
    # TODO
    pass


if __name__ == "__main__":
    main()
