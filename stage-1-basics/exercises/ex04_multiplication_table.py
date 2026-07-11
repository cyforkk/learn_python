"""
练习 04：九九乘法表

要求：
1. 打印标准九九乘法表（下三角）
2. 用嵌套 for，不要手写 81 行 print
3. 实现 build_table() -> list[str]，每行一个字符串（便于自检）
   print_table() 可以打印 build_table() 的结果

自检：python ex04_multiplication_table.py --check
"""


def build_table() -> list[str]:
    """返回 9 行字符串，第 i 行（1-based）含 1*i ... i*i。"""
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
