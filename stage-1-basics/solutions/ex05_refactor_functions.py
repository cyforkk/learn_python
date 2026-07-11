# 参考答案：成绩等级函数（最简单版）


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
