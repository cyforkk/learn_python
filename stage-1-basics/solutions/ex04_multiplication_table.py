# 参考答案：九九乘法表（与 exercises 同为最简单写法）

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end="  ")
    print()
