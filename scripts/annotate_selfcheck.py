"""给练习/答案中的 _selfcheck 加上新手可读的中文注释。"""

from pathlib import Path

BANNER = """# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
"""

CHECK_LINE = '    if "--check" in sys.argv:\n'
CHECK_COMMENT = (
    "    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数\n"
)


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "def _selfcheck" not in text:
        return False
    orig = text
    if "【测试 / 自检函数" not in text:
        text = text.replace("def _selfcheck", BANNER + "def _selfcheck", 1)
    if "才会调用上面的【测试函数" not in text and CHECK_LINE in text:
        text = text.replace(CHECK_LINE, CHECK_COMMENT + CHECK_LINE, 1)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    changed: list[str] = []
    for folder in ("stage-1-basics", "stage-2-stdlib"):
        for path in (root / folder).rglob("*.py"):
            if process(path):
                changed.append(str(path.relative_to(root)))
    print(f"changed {len(changed)}")
    for c in changed:
        print(c)


if __name__ == "__main__":
    main()
