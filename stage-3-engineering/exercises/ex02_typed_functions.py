"""
练习 02：补全类型注解

要求：
1. 为下列函数补全参数与返回值类型注解
2. 保持行为不变
3. （可选）用编辑器看是否还能正确提示类型

运行：python ex02_typed_functions.py
"""


def add(a, b):
    return a + b


def join_names(names, sep):
    return sep.join(names)


def find_score(scores, name):
    """scores: 姓名 -> 分数；找不到返回 None。"""
    return scores.get(name)


def main():
    print(add(1, 2))
    print(join_names(["Ada", "Bob"], ", "))
    print(find_score({"Ada": 90.0}, "Ada"))
    print(find_score({"Ada": 90.0}, "Zoe"))


if __name__ == "__main__":
    main()
