"""
练习 04：pathlib 列目录

要求：
1. count_entries(path) -> tuple[int, int]  返回 (文件数, 子目录数)
2. list_cwd() 打印当前目录详情（可调用 count_entries）

自检：python ex04_list_files.py --check
"""

from pathlib import Path


def count_entries(path: Path) -> tuple[int, int]:
    """统计 path 下直接子项中的文件数与目录数（不含递归）。"""
    # TODO
    raise NotImplementedError


def list_cwd() -> None:
    # TODO
    pass


def _selfcheck() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.txt").write_text("x", encoding="utf-8")
        (root / "b.txt").write_text("y", encoding="utf-8")
        (root / "sub").mkdir()
        files, dirs = count_entries(root)
        assert files == 2
        assert dirs == 1
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        list_cwd()
