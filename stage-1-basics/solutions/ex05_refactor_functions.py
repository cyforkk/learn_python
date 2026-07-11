"""参考答案：ex05 函数重构。"""


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


if __name__ == "__main__":
    main()
