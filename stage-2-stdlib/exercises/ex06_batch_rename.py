"""
练习 06：批量重命名（安全版：仅规划 / 可选执行）

要求：
1. plan_rename(files, prefix) -> list[tuple[Path, Path]]
   将 a.txt, b.txt 变为 prefix_1.txt, prefix_2.txt（按名字排序）
2. 不直接改系统重要目录；自检用临时目录

建议先读：常用标准库、文件读写
难度：⭐⭐ · 约 35 分
自检：python ex06_batch_rename.py --check
"""

from __future__ import annotations

from pathlib import Path


def plan_rename(files: list[Path], prefix: str) -> list[tuple[Path, Path]]:
    """按文件名排序后生成 (旧路径, 新路径) 计划。"""
    ordered = sorted(files, key=lambda p: p.name.lower())
    plans: list[tuple[Path, Path]] = []
    for i, src in enumerate(ordered, 1):
        dest = src.with_name(f"{prefix}_{i}{src.suffix}")
        plans.append((src, dest))
    return plans


def apply_rename(plans: list[tuple[Path, Path]], dry_run: bool = True) -> None:
    for src, dest in plans:
        if dry_run:
            print(f"[dry-run] {src.name} -> {dest.name}")
        else:
            src.rename(dest)
            print(f"[renamed] {src.name} -> {dest.name}")


def main() -> None:
    print("示例：对本目录下 .txt 做计划（默认 dry-run）")
    files = sorted(Path(__file__).parent.glob("*.txt"))
    plans = plan_rename(files, "note")
    apply_rename(plans, dry_run=True)


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
        a = root / "b.txt"
        b = root / "a.txt"
        a.write_text("1", encoding="utf-8")
        b.write_text("2", encoding="utf-8")
        plans = plan_rename([a, b], "file")
        # 排序后 a.txt 在前
        assert plans[0][0].name == "a.txt"
        assert plans[0][1].name == "file_1.txt"
        assert plans[1][1].name == "file_2.txt"
        apply_rename(plans, dry_run=False)
        assert (root / "file_1.txt").exists()
        assert (root / "file_2.txt").exists()
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
