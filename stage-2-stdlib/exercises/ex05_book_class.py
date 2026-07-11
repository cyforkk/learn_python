"""
练习 05：简单 Book 类

自检：python ex05_book_class.py --check
"""


class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self) -> str:
        return f"《{self.title}》- {self.author}, {self.pages}页"

    def is_long(self) -> bool:
        return self.pages >= 300


def main() -> None:
    books = [
        Book("Fluent Python", "Luciano", 1000),
        Book("短篇集", "Someone", 120),
    ]
    for b in books:
        print(b.summary(), "| 长书?", b.is_long())


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
