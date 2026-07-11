"""
练习 01：JSON 待办读写

要求：
1. 使用 pathlib + json
2. 待办保存在本文件同目录的 todos.json
3. 支持：
   - 启动时若文件不存在，当作空列表
   - add(text): 追加一条 {"text": text, "done": false}
   - list_all(): 打印全部
   - save/load 持久化
4. 命令行简单交互：add / list / quit

运行：python ex01_todo_json.py
"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos() -> list[dict]:
    # TODO
    raise NotImplementedError


def save_todos(todos: list[dict]) -> None:
    # TODO
    raise NotImplementedError


def add_todo(todos: list[dict], text: str) -> None:
    # TODO
    raise NotImplementedError


def main() -> None:
    todos = load_todos()
    # TODO: 交互循环
    pass


if __name__ == "__main__":
    main()
