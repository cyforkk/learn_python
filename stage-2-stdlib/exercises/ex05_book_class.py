"""
练习 05：简单 Book 类

summary 格式： 《title》- author, pages页
is_long：pages >= 300

自检：python ex05_book_class.py --check
"""


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        # TODO
        raise NotImplementedError

    def summary(self) -> str:
        # TODO
        raise NotImplementedError

    def is_long(self) -> bool:
        # TODO
        raise NotImplementedError


def main() -> None:
    # TODO
    pass


def _selfcheck() -> None:
    b = Book("Fluent Python", "Luciano", 1000)
    assert b.summary() == "《Fluent Python》- Luciano, 1000页"
    assert b.is_long() is True
    s = Book("短篇", "A", 120)
    assert s.is_long() is False
    assert "短篇" in s.summary()
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
