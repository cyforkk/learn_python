"""参考答案：ex03 小模块。"""

from greeter import greet


def main() -> None:
    name = input("你的名字: ").strip() or "World"
    print(greet(name))


def _selfcheck() -> None:
    assert greet("Ada") == "Hello, Ada!"
    assert greet("World") == "Hello, World!"
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
