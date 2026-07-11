#!/usr/bin/env python3
"""仓库自检：语法编译 + 可选 checks/ + 部分 pytest。在仓库根目录运行。"""

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

    print("\n=== compileall ===")
    if run([py, "-m", "compileall", "-q",
            str(ROOT / "stage-1-basics"),
            str(ROOT / "stage-2-stdlib"),
            str(ROOT / "stage-3-engineering"),
            str(ROOT / "projects"),
            str(ROOT / "scripts")]) != 0:
        failed.append("compileall")

    print("\n=== stage-1 可选 checks/（不是作业）===")
    for p in sorted((ROOT / "stage-1-basics" / "exercises" / "checks").glob("ex*_check.py")):
        if run([py, str(p)]) != 0:
            failed.append(str(p.relative_to(ROOT)))

    print("\n=== stage-2 可选 checks/ ===")
    checks2 = ROOT / "stage-2-stdlib" / "exercises" / "checks"
    if checks2.exists():
        for p in sorted(checks2.glob("ex*_check.py")):
            if run([py, str(p)]) != 0:
                failed.append(str(p.relative_to(ROOT)))

    print("\n=== 冒烟：极简练习可 import/运行无 input 的脚本 ===")
    for p in [
        ROOT / "stage-1-basics" / "exercises" / "ex04_multiplication_table.py",
        ROOT / "stage-1-basics" / "exercises" / "ex03_score_stats.py",
        ROOT / "stage-1-basics" / "exercises" / "ex05_refactor_functions.py",
        ROOT / "stage-1-basics" / "exercises" / "ex06_contacts.py",
        ROOT / "stage-2-stdlib" / "exercises" / "ex05_book_class.py",
        ROOT / "stage-2-stdlib" / "exercises" / "ex06_batch_rename.py",
        ROOT / "stage-0-setup" / "hello.py",
        ROOT / "stage-4-tracks" / "ai" / "starter" / "main.py",
    ]:
        if p.exists() and run([py, str(p)]) != 0:
            failed.append(str(p.relative_to(ROOT)))

    print("\n=== pytest（加练模块，失败不挡主线时可忽略）===")
    for t in [
        ROOT / "stage-3-engineering" / "exercises" / "ex03_pytest_stats",
        ROOT / "projects" / "todo-cli",
    ]:
        if t.exists():
            code = run([py, "-m", "pytest", "-q", str(t)])
            if code != 0:
                print(f"(pytest 未过) {t.relative_to(ROOT)} — 新手可忽略")

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
