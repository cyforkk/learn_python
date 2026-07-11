# 练习：列出当前目录（选做 · 最简单版）
# 运行：python ex04_list_files.py

from pathlib import Path

folder = Path(".")
for item in folder.iterdir():
    if item.is_file():
        print("[文件]", item.name)
    elif item.is_dir():
        print("[目录]", item.name)
