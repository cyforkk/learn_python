"""参考答案：类型注解。"""


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def join_names(names: list[str], sep: str) -> str:
    return sep.join(names)


def find_score(scores: dict[str, float], name: str) -> float | None:
    return scores.get(name)


def main() -> None:
    print(add(1, 2))
    print(join_names(["Ada", "Bob"], ", "))
    print(find_score({"Ada": 90.0}, "Ada"))
    print(find_score({"Ada": 90.0}, "Zoe"))


if __name__ == "__main__":
    main()
