"""命令行待办：add / list / done / delete / quit，JSON 持久化。"""

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


def mark_done(todos: list[dict], index: int) -> bool:
    """index 为 1-based。成功返回 True。"""
    if index < 1 or index > len(todos):
        return False
    todos[index - 1]["done"] = True
    return True


def delete_todo(todos: list[dict], index: int) -> bool:
    if index < 1 or index > len(todos):
        return False
    todos.pop(index - 1)
    return True


def format_list(todos: list[dict]) -> str:
    if not todos:
        return "(暂无任务)"
    lines = []
    for i, item in enumerate(todos, 1):
        flag = "x" if item.get("done") else " "
        lines.append(f"{i}. [{flag}] {item.get('text', '')}")
    return "\n".join(lines)


def main() -> None:
    todos = load_todos()
    print("待办 CLI：add <内容> | list | done <编号> | delete <编号> | quit")
    while True:
        raw = input("> ").strip()
        if not raw:
            continue
        if raw == "quit":
            save_todos(todos)
            print("已保存，再见。")
            break
        if raw == "list":
            print(format_list(todos))
            continue
        if raw.startswith("add "):
            text = raw[4:].strip()
            if not text:
                print("内容不能为空。")
                continue
            add_todo(todos, text)
            save_todos(todos)
            print("已添加。")
            continue
        if raw.startswith("done "):
            part = raw[5:].strip()
            try:
                idx = int(part)
            except ValueError:
                print("编号必须是整数。")
                continue
            if mark_done(todos, idx):
                save_todos(todos)
                print("已标记完成。")
            else:
                print("编号无效。")
            continue
        if raw.startswith("delete "):
            part = raw[7:].strip()
            try:
                idx = int(part)
            except ValueError:
                print("编号必须是整数。")
                continue
            if delete_todo(todos, idx):
                save_todos(todos)
                print("已删除。")
            else:
                print("编号无效。")
            continue
        print("未知命令。可用: add / list / done / delete / quit")


if __name__ == "__main__":
    main()
