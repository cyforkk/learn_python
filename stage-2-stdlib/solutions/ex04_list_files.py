from pathlib import Path

for item in Path(".").iterdir():
    if item.is_file():
        print("[文件]", item.name)
    elif item.is_dir():
        print("[目录]", item.name)
