# 练习：用函数判断成绩等级（最简单版）
# 先读笔记：函数
# 运行：python ex05_refactor_functions.py
#
# 目标：写一个函数，根据分数返回 A/B/C/D，再打印几个学生。


def level(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


print("小明", 92, "->", level(92))
print("小红", 78, "->", level(78))
print("小刚", 55, "->", level(55))
