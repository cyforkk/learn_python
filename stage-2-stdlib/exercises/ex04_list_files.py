"""
练习 04：pathlib 列目录

自检：python ex04_list_files.py --check
"""

from pathlib import Path


def count_entries(path: Path) -> tuple[int, int]:
    """统计 path 下直接子项中的文件数与目录数（不含递归）。"""
    files = 0
    dirs = 0
    for item in path.iterdir():
        if item.is_file():
            files += 1
        elif item.is_dir():
            dirs += 1
    return files, dirs


def list_cwd() -> None:
    cwd = Path.cwd()
    files, dirs = count_entries(cwd)
    print(f"目录: {cwd}")
    for item in sorted(cwd.iterdir(), key=lambda p: p.name.lower()):
        if item.is_file():
            print(f"[文件] {item.name}\t{item.stat().st_size} bytes")
        elif item.is_dir():
            print(f"[目录] {item.name}")
    print(f"合计: 文件 {files} 个, 子目录 {dirs} 个")


def _selfcheck() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.txt").write_text("x", encoding="utf-8")
        (root / "b.txt").write_text("y", encoding="utf-8")
        (root / "sub").mkdir()
        n_files, n_dirs = count_entries(root)
        assert n_files == 2
        assert n_dirs == 1
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        list_cwd()
