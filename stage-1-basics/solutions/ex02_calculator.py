"""参考答案：ex02 简易计算器。"""


def calculate(a: float, op: str, b: float) -> float | None:
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
    while True:
        raw = input("输入表达式（如 3 + 4），或 q 退出: ").strip()
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
