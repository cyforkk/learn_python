"""参考答案：ex01 JSON 待办。"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    text = DATA_FILE.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)


def save_todos(todos: list[dict]) -> None:
    DATA_FILE.write_text(
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
            continue
        print("未知命令。")


if __name__ == "__main__":
    main()
