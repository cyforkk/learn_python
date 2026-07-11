"""
练习 01：JSON 待办读写

要求：
1. 使用 pathlib + json
2. load_todos / save_todos / add_todo
3. 文件不存在时 load 返回 []
4. 命令行简单交互：add / list / quit（main）

自检：python ex01_todo_json.py --check
"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos(path: Path = DATA_FILE) -> list[dict]:
    # TODO
    raise NotImplementedError


def save_todos(todos: list[dict], path: Path = DATA_FILE) -> None:
    # TODO
    raise NotImplementedError


def add_todo(todos: list[dict], text: str) -> None:
    # TODO
    raise NotImplementedError


def main() -> None:
    todos = load_todos()
    # TODO: 交互循环
    pass


def _selfcheck() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "t.json"
        assert load_todos(path) == []
        todos: list[dict] = []
        add_todo(todos, "买牛奶")
        assert len(todos) == 1
        assert todos[0]["text"] == "买牛奶"
        assert todos[0]["done"] is False
        save_todos(todos, path)
        loaded = load_todos(path)
        assert loaded[0]["text"] == "买牛奶"
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
