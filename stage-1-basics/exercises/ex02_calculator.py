"""
练习 02：简易计算器

要求：
1. 提示用户输入：数字 a、运算符（+ - * /）、数字 b
2. 输出计算结果
3. 除法除数为 0 时返回 None（不要崩溃）
4. 运算符非法时 raise ValueError
5. （可选）用循环支持连续计算，输入 q 退出

自检：python ex02_calculator.py --check
"""


def calculate(a: float, op: str, b: float) -> float | None:
    """根据运算符计算；除零返回 None；非法运算符 raise ValueError。"""
    # TODO
    raise NotImplementedError


def main() -> None:
    # TODO: 读入输入并调用 calculate
    pass


def _selfcheck() -> None:
    assert calculate(3, "+", 4) == 7
    assert calculate(10, "-", 3) == 7
    assert calculate(2, "*", 5) == 10
    assert calculate(8, "/", 2) == 4
    assert calculate(1, "/", 0) is None
    try:
        calculate(1, "^", 2)
        raise AssertionError("应抛出 ValueError")
    except ValueError:
        pass
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
