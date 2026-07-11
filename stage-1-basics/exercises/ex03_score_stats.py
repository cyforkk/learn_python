"""
练习 03：学生成绩统计

要求：
1. 用字典保存至少 4 名学生姓名 -> 分数
2. 打印：平均分、最高分及姓名、最低分及姓名
3. 打印所有「不低于平均分」的学生

自检：python ex03_score_stats.py --check
"""


def average(scores: dict[str, float]) -> float:
    # TODO
    raise NotImplementedError


def top_student(scores: dict[str, float]) -> tuple[str, float]:
    """返回 (姓名, 分数) 最高分者；可假设字典非空。"""
    # TODO
    raise NotImplementedError


def bottom_student(scores: dict[str, float]) -> tuple[str, float]:
    """返回 (姓名, 分数) 最低分者；可假设字典非空。"""
    # TODO
    raise NotImplementedError


def main() -> None:
    scores = {
        "Ada": 92.0,
        "Bob": 78.5,
        "Cindy": 88.0,
        "Dan": 65.0,
    }
    # TODO: 调用函数并打印结果
    pass


def _selfcheck() -> None:
    scores = {"Ada": 92.0, "Bob": 78.5, "Cindy": 88.0, "Dan": 65.0}
    assert abs(average(scores) - 80.875) < 1e-9
    assert top_student(scores) == ("Ada", 92.0)
    assert bottom_student(scores) == ("Dan", 65.0)
    # 空字典：推荐返回 0.0
    assert average({}) == 0.0
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
