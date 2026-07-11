"""参考答案：ex04 pathlib 列目录。"""

from pathlib import Path


def count_entries(path: Path) -> tuple[int, int]:
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


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
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

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        list_cwd()
