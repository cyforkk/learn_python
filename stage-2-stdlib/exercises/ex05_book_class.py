"""
练习 05：简单 Book 类

要求：
1. 定义 class Book:
   - __init__(self, title: str, author: str, pages: int)
   - summary(self) -> str  返回 "《title》- author, pages页"
   - is_long(self) -> bool  pages >= 300 为 True
2. 创建至少 2 本书，打印 summary 与 is_long

运行：python ex05_book_class.py
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


if __name__ == "__main__":
    main()
