# 练习：小模块（最简单版）
# 先读笔记：模块与包
# 运行（请在本目录下）：python main.py
#
# 目标：main 里 import greeter，并打印问候。

from greeter import greet

name = input("你的名字: ")
print(greet(name))
