"""参考答案：ex04 九九乘法表。"""


def build_table() -> list[str]:
    rows: list[str] = []
    for i in range(1, 10):
        cells = [f"{j}*{i}={j * i}" for j in range(1, i + 1)]
        rows.append("\t".join(cells))
    return rows


def print_table() -> None:
    for line in build_table():
        print(line)


def _selfcheck() -> None:
    rows = build_table()
    assert len(rows) == 9
    assert "1*1=1" in rows[0].replace(" ", "").replace("\t", "")
    row3 = rows[2].replace(" ", "").replace("\t", "")
    assert "2*3=6" in row3
    assert "3*3=9" in row3
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        print_table()
