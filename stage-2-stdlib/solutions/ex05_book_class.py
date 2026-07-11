"""参考答案：ex05 Book 类。"""


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
        print(b.summary(), "| 长书?" , b.is_long())


if __name__ == "__main__":
    main()
