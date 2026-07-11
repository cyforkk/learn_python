"""
练习 04：九九乘法表（新手优先做这题）

【新手】两层 for 循环直接 print 即可，能打出表就算过关。
  build_table / --check 是进阶写法，可先不管。

要求：
1. 打印标准九九乘法表（下三角）
2. 用嵌套 for，不要手写 81 行 print

运行：python ex04_multiplication_table.py
可选自检：python ex04_multiplication_table.py --check
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


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
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

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        print_table()
