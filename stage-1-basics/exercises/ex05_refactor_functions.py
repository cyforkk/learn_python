"""
练习 05：把重复逻辑抽成函数

1. grade_level(score) -> "A"/"B"/"C"/"D"
2. summarize(name, score) -> 如 "Ada: 92.0 -> A"
3. main 里对多个学生调用 summarize

自检：python ex05_refactor_functions.py --check
"""


def grade_level(score: float) -> str:
    # TODO
    raise NotImplementedError


def summarize(name: str, score: float) -> str:
    # TODO
    raise NotImplementedError


def main() -> None:
    students = [("Ada", 92.0), ("Bob", 78.0), ("Cindy", 55.0)]
    # TODO
    pass


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

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
