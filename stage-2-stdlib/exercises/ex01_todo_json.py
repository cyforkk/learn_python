# 练习：JSON 待办（加练 · 尽量简单）
# 先读笔记：文件读写
# 运行：python ex01_todo_json.py
# 命令：add 内容 | list | quit

import json
from pathlib import Path

file = Path("todos.json")

if file.exists():
    todos = json.loads(file.read_text(encoding="utf-8"))
else:
    todos = []

print("命令: add 内容 | list | quit")
while True:
    cmd = input("> ").strip()
    if cmd == "quit":
        file.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")
        print("已保存")
        break
    if cmd == "list":
        if not todos:
            print("(空)")
        for i, t in enumerate(todos, 1):
            print(i, t)
    elif cmd.startswith("add "):
        text = cmd[4:].strip()
        if text:
            todos.append(text)
            print("已添加")
    else:
        print("未知命令")
