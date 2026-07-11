"""按扩展名整理目录：默认 dry-run，加 --apply 才真正移动。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

# 扩展名（小写，含点）→ 子目录名
CATEGORY_MAP = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".webp": "images",
    ".pdf": "docs",
    ".doc": "docs",
    ".docx": "docs",
    ".txt": "docs",
    ".md": "docs",
    ".csv": "docs",
}


def category_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if not suffix:
        return "others"
    return CATEGORY_MAP.get(suffix, "others")


def plan_moves(source: Path) -> list[tuple[Path, Path]]:
    """返回 (源文件, 目标路径) 列表；不包含分类目录自身。"""
    moves: list[tuple[Path, Path]] = []
    category_dirs = {"images", "docs", "others"}
    for item in source.iterdir():
        if item.is_dir():
            if item.name in category_dirs:
                continue
            continue  # 不移动子目录
        if not item.is_file():
            continue
        dest_dir = source / category_for(item)
        dest = dest_dir / item.name
        moves.append((item, dest))
    return moves


def apply_moves(moves: list[tuple[Path, Path]], dry_run: bool = True) -> dict[str, int]:
    counts: dict[str, int] = {}
    for src, dest in moves:
        cat = dest.parent.name
        counts[cat] = counts.get(cat, 0) + 1
        if dry_run:
            print(f"[dry-run] {src.name} -> {dest.parent.name}/")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            print(f"[moved] {src.name} -> {dest.parent.name}/")
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="按扩展名整理文件夹（默认 dry-run，加 --apply 才移动）"
    )
    parser.add_argument(
        "source",
        type=Path,
        help="要整理的目录（请先用测试副本！）",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="真正移动文件；不加则只预览",
    )
    args = parser.parse_args()
    source: Path = args.source.resolve()

    if not source.is_dir():
        print(f"不是有效目录: {source}")
        return

    moves = plan_moves(source)
    if not moves:
        print("没有需要整理的文件。")
        return

    dry_run = not args.apply
    if dry_run:
        print("=== DRY-RUN（未移动任何文件）===")
    else:
        print("=== APPLY（正在移动）===")

    counts = apply_moves(moves, dry_run=dry_run)
    print("汇总:", counts)
    if dry_run:
        print("确认无误后加参数 --apply 执行。")


if __name__ == "__main__":
    main()
