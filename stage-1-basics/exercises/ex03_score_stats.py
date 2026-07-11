"""
练习 03：学生成绩统计

要求：
1. 用字典保存至少 4 名学生姓名 -> 分数
2. 打印：平均分、最高分及姓名、最低分及姓名
3. 打印所有「不低于平均分」的学生

自检：python ex03_score_stats.py --check
"""


def average(scores: dict[str, float]) -> float:
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


def top_student(scores: dict[str, float]) -> tuple[str, float]:
    """返回 (姓名, 分数) 最高分者；可假设字典非空。"""
    name = max(scores, key=scores.get)  # type: ignore[arg-type]
    return name, scores[name]


def bottom_student(scores: dict[str, float]) -> tuple[str, float]:
    """返回 (姓名, 分数) 最低分者；可假设字典非空。"""
    name = min(scores, key=scores.get)  # type: ignore[arg-type]
    return name, scores[name]


def main() -> None:
    scores = {
        "Ada": 92.0,
        "Bob": 78.5,
        "Cindy": 88.0,
        "Dan": 65.0,
    }
    avg = average(scores)
    hi_name, hi_score = top_student(scores)
    lo_name, lo_score = bottom_student(scores)

    print(f"平均分: {avg:.2f}")
    print(f"最高: {hi_name} {hi_score}")
    print(f"最低: {lo_name} {lo_score}")
    print("不低于平均分:")
    for name, score in scores.items():
        if score >= avg:
            print(f"  {name}: {score}")


def _selfcheck() -> None:
    scores = {"Ada": 92.0, "Bob": 78.5, "Cindy": 88.0, "Dan": 65.0}
    assert abs(average(scores) - 80.875) < 1e-9
    assert top_student(scores) == ("Ada", 92.0)
    assert bottom_student(scores) == ("Dan", 65.0)
    assert average({}) == 0.0
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
