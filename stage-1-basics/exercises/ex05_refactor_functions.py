"""
练习 05：把重复逻辑抽成函数

1. grade_level(score) -> "A"/"B"/"C"/"D"
2. summarize(name, score) -> 如 "Ada: 92.0 -> A"
3. main 里对多个学生调用 summarize

自检：python ex05_refactor_functions.py --check
"""


def grade_level(score: float) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


def summarize(name: str, score: float) -> str:
    return f"{name}: {score} -> {grade_level(score)}"


def main() -> None:
    students = [("Ada", 92.0), ("Bob", 78.0), ("Cindy", 55.0)]
    for name, score in students:
        print(summarize(name, score))


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
def _selfcheck() -> None:
    assert grade_level(95) == "A"
    assert grade_level(85) == "B"
    assert grade_level(70) == "C"
    assert grade_level(50) == "D"
    assert grade_level(90) == "A"
    assert grade_level(80) == "B"
    assert grade_level(60) == "C"
    s = summarize("Ada", 92.0)
    assert "Ada" in s and "A" in s and "92" in s
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
