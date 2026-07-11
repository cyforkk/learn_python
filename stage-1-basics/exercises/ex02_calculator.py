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
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return None
        return a / b
    raise ValueError(f"不支持的运算符: {op}")


def main() -> None:
    print("输入格式: 数字 运算符 数字 ，例如 3 + 4 ；输入 q 退出")
    while True:
        raw = input("> ").strip()
        if raw.lower() == "q":
            print("再见。")
            break

        parts = raw.split()
        if len(parts) != 3:
            print("格式应为: 数字 运算符 数字")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            result = calculate(a, op, b)
        except ValueError as e:
            print(e)
            continue

        if result is None:
            print("除数不能为 0")
        else:
            print("结果:", result)


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
