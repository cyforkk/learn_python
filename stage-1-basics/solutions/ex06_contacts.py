"""参考答案：ex06 通讯录。"""


def add_contact(book: dict[str, str], name: str, phone: str) -> None:
    book[name] = phone


def find_contact(book: dict[str, str], name: str) -> str | None:
    return book.get(name)


def list_contacts(book: dict[str, str]) -> list[str]:
    return [f"{n}: {p}" for n, p in sorted(book.items())]


def main() -> None:
    book: dict[str, str] = {}
    add_contact(book, "Ada", "13800000001")
    add_contact(book, "Bob", "13900000002")
    print("查找 Ada:", find_contact(book, "Ada"))
    for line in list_contacts(book):
        print(line)


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
def _selfcheck() -> None:
    book: dict[str, str] = {}
    add_contact(book, "Ada", "100")
    assert find_contact(book, "Ada") == "100"
    assert find_contact(book, "Zoe") is None
    add_contact(book, "Bob", "200")
    lines = list_contacts(book)
    assert any("Ada" in x for x in lines)
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
