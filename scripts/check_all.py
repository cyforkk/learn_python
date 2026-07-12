#!/usr/bin/env python3
"""仓库自检：语法 + solutions 冒烟。exercises 是题目骨架，不要求能跑通业务。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("$", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd or ROOT).returncode


def main() -> int:
    py = sys.executable
    failed: list[str] = []

    print("\n=== compileall (-B 不写 pyc，避免 Windows 锁文件) ===")
    if (
        run(
            [
                py,
                "-B",
                "-m",
                "compileall",
                "-q",
                str(ROOT / "stage-1-basics" / "solutions"),
                str(ROOT / "stage-2-stdlib" / "solutions"),
                str(ROOT / "projects"),
            ]
        )
        != 0
    ):
        failed.append("compileall")

    print("\n=== solutions 冒烟（答案应能跑；作业 exercises 是空骨架）===")
    for p in [
        ROOT / "stage-1-basics" / "solutions" / "ex04_multiplication_table.py",
        ROOT / "stage-1-basics" / "solutions" / "ex03_score_stats.py",
        ROOT / "stage-1-basics" / "solutions" / "ex05_refactor_functions.py",
        ROOT / "stage-1-basics" / "solutions" / "ex06_contacts.py",
        ROOT / "stage-2-stdlib" / "solutions" / "ex05_book_class.py",
        ROOT / "stage-2-stdlib" / "solutions" / "ex06_batch_rename.py",
        ROOT / "stage-0-setup" / "hello.py",
        ROOT / "stage-4-tracks" / "ai" / "starter" / "main.py",
    ]:
        if p.exists() and run([py, str(p)]) != 0:
            failed.append(str(p.relative_to(ROOT)))

    print("\n=== pytest（加练模块，失败可忽略主线）===")
    for t in [
        ROOT / "stage-3-engineering" / "exercises" / "ex03_pytest_stats",
        ROOT / "projects" / "todo-cli",
    ]:
        if t.exists():
            code = run([py, "-m", "pytest", "-q", str(t)])
            if code != 0:
                print(f"(pytest 未过) {t.relative_to(ROOT)}")

    print("\n=== summary ===")
    if failed:
        print("FAILED:")
        for f in failed:
            print(" -", f)
        return 1
    print("ALL_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
