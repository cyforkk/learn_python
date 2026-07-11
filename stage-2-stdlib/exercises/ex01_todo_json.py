"""
练习 01：JSON 待办读写

自检：python ex01_todo_json.py --check
"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos(path: Path = DATA_FILE) -> list[dict]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)


def save_todos(todos: list[dict], path: Path = DATA_FILE) -> None:
    path.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def add_todo(todos: list[dict], text: str) -> None:
    todos.append({"text": text, "done": False})


def main() -> None:
    todos = load_todos()
    print("命令: add <内容> | list | quit")
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        if raw == "quit":
            save_todos(todos)
            print("已保存，再见。")
            break
        if raw == "list":
            if not todos:
                print("(空)")
            for i, item in enumerate(todos, 1):
                flag = "x" if item.get("done") else " "
                print(f"{i}. [{flag}] {item.get('text')}")
            continue
        if raw.startswith("add "):
            text = raw[4:].strip()
            if text:
                add_todo(todos, text)
                save_todos(todos)
                print("已添加。")
            else:
                print("内容不能为空。")
            continue
        print("未知命令。")


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
