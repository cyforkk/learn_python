# 参考答案：安全读文件（最简单版）

path = input("请输入文件路径: ")

try:
    f = open(path, encoding="utf-8")
    text = f.read()
    f.close()
    print(text)
except FileNotFoundError:
    print("文件不存在:", path)
