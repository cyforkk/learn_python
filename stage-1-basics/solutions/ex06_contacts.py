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

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
