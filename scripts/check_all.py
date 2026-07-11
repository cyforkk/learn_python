#!/usr/bin/env python3
"""一键自检：stage-1/2 --check、pytest、语法扫描。在仓库根目录运行。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("$", " ".join(cmd), f"(cwd={cwd or ROOT})")
    r = subprocess.run(cmd, cwd=cwd or ROOT)
    return r.returncode


def main() -> int:
    py = sys.executable
    failed: list[str] = []

    # 语法
    print("\n=== syntax (compileall) ===")
    code = run([py, "-m", "compileall", "-q", str(ROOT / "stage-1-basics"), str(ROOT / "stage-2-stdlib"), str(ROOT / "stage-3-engineering"), str(ROOT / "stage-4-tracks"), str(ROOT / "projects"), str(ROOT / "scripts")])
    if code != 0:
        failed.append("compileall")

    # stage-1 solutions --check
    print("\n=== stage-1 solutions --check ===")
    for p in sorted((ROOT / "stage-1-basics" / "solutions").glob("ex*.py")):
        if run([py, str(p), "--check"]) != 0:
            failed.append(str(p.relative_to(ROOT)))

    # stage-1 exercises --check (应已实现)
    print("\n=== stage-1 exercises --check ===")
    for p in sorted((ROOT / "stage-1-basics" / "exercises").glob("ex*.py")):
        if run([py, str(p), "--check"]) != 0:
            failed.append(str(p.relative_to(ROOT)))

    # stage-2
    print("\n=== stage-2 --check ===")
    s2_ex = ROOT / "stage-2-stdlib" / "exercises"
    s2_sol = ROOT / "stage-2-stdlib" / "solutions"
    for base in (s2_ex, s2_sol):
        for p in sorted(base.glob("ex*.py")):
            if run([py, str(p), "--check"]) != 0:
                failed.append(str(p.relative_to(ROOT)))
        mini = base / "ex03_mini_package" / "main.py"
        if mini.exists():
            if run([py, str(mini), "--check"], cwd=mini.parent) != 0:
                failed.append(str(mini.relative_to(ROOT)))

    # pytest
    print("\n=== pytest ===")
    targets = [
        ROOT / "stage-3-engineering" / "exercises" / "ex03_pytest_stats",
        ROOT / "stage-3-engineering" / "solutions" / "ex03_pytest_stats",
        ROOT / "projects" / "todo-cli",
    ]
    for t in targets:
        if t.exists():
            if run([py, "-m", "pytest", "-q", str(t)]) != 0:
                failed.append(f"pytest:{t.relative_to(ROOT)}")

    mini = ROOT / "stage-3-engineering" / "exercises" / "ex05_mini_project"
    if mini.exists():
        env_cmd = [py, "-m", "pytest", "-q"]
        print("$", " ".join(env_cmd), f"(cwd={mini})")
        r = subprocess.run(env_cmd, cwd=mini)
        if r.returncode != 0:
            failed.append("pytest:ex05_mini_project")

    # stage-4 / smoke（不强制外网）
    print("\n=== smoke (no network) ===")
    must = [
        ROOT / "stage-0-setup" / "hello.py",
        ROOT / "stage-4-tracks" / "ai" / "starter" / "main.py",
        ROOT / "stage-4-tracks" / "ai" / "demo" / "main.py",
    ]
    optional = [
        ROOT / "stage-4-tracks" / "data" / "starter" / "main.py",
        ROOT / "stage-4-tracks" / "data" / "demo" / "main.py",
        ROOT / "stage-4-tracks" / "web" / "starter" / "main.py",
        ROOT / "stage-4-tracks" / "web" / "demo" / "main.py",
    ]
    for p in must:
        if p.exists() and run([py, str(p)]) != 0:
            failed.append(str(p.relative_to(ROOT)))
    for p in optional:
        if not p.exists():
            continue
        if run([py, str(p)]) != 0:
            print(f"(optional fail) {p.relative_to(ROOT)} — pip install 对应 requirements 后重试")

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
