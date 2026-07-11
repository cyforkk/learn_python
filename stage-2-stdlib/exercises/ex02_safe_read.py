# 练习：安全读文件（最简单版）
# 先读笔记：文件读写 + 异常处理
# 运行：python ex02_safe_read.py
#
# 目标：文件存在就打印内容；不存在就提示，不要崩溃。

path = input("请输入文件路径: ")

try:
    f = open(path, encoding="utf-8")
    text = f.read()
    f.close()
    print(text)
except FileNotFoundError:
    print("文件不存在:", path)
