"""参考答案：ex03 小模块。"""

from greeter import greet


def main() -> None:
    name = input("你的名字: ").strip() or "World"
    print(greet(name))


if __name__ == "__main__":
    main()
