"""
练习 03：小模块拆分

在 greeter.py 实现 greet；本文件 import 并调用。

自检：python main.py --check
运行：python main.py
"""

# TODO: from greeter import greet


def main() -> None:
    # TODO
    pass


def _selfcheck() -> None:
    from greeter import greet

    assert greet("Ada") == "Hello, Ada!"
    assert greet("World") == "Hello, World!"
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
