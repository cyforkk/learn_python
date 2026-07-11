"""参考答案：ex04 pathlib 列目录。"""

from pathlib import Path


def list_cwd() -> None:
    cwd = Path.cwd()
    files = 0
    dirs = 0
    print(f"目录: {cwd}")
    for item in sorted(cwd.iterdir(), key=lambda p: p.name.lower()):
        if item.is_file():
            files += 1
            print(f"[文件] {item.name}\t{item.stat().st_size} bytes")
        elif item.is_dir():
            dirs += 1
            print(f"[目录] {item.name}")
    print(f"合计: 文件 {files} 个, 子目录 {dirs} 个")


if __name__ == "__main__":
    list_cwd()
