# 参考答案：计算器（选做 · 最简单版）

print("输入: 数字 运算符 数字  例如 3 + 4 ；输入 q 退出")

while True:
    line = input("> ")
    if line == "q":
        break

    parts = line.split()
    if len(parts) != 3:
        print("格式不对，请像这样: 3 + 4")
        continue

    a = float(parts[0])
    op = parts[1]
    b = float(parts[2])

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("除数不能是 0")
        else:
            print(a / b)
    else:
        print("不支持的运算符")
