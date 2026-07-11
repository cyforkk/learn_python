import json
from pathlib import Path

file = Path("todos.json")
todos = json.loads(file.read_text(encoding="utf-8")) if file.exists() else []

print("命令: add 内容 | list | quit")
while True:
    cmd = input("> ").strip()
    if cmd == "quit":
        file.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")
        print("已保存")
        break
    if cmd == "list":
        for i, t in enumerate(todos, 1):
            print(i, t)
    elif cmd.startswith("add "):
        todos.append(cmd[4:].strip())
        print("已添加")
