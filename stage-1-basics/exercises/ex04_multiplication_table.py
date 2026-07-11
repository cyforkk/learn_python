# 练习：九九乘法表（最简单版）
# 先读笔记：条件与循环
# 运行：python ex04_multiplication_table.py
#
# 目标：用两层 for，打印下三角九九表即可。

for i in range(1, 10):          # 第 i 行
    for j in range(1, i + 1):   # 这一行有 i 个算式
        print(f"{j}*{i}={j * i}", end="  ")
    print()  # 一行结束，换行
