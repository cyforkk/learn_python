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
        print(b.summary(), "| 长书?", b.is_long())


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
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

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
