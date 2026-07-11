# 练习：成绩统计（最简单版）
# 先读笔记：复合类型（字典）
# 运行：python ex03_score_stats.py
#
# 目标：用字典存成绩，打印平均分、最高、最低。

scores = {
    "小明": 92,
    "小红": 78,
    "小刚": 88,
    "小丽": 65,
}

# 平均分
total = 0
for name in scores:
    total = total + scores[name]
avg = total / len(scores)
print("平均分:", avg)

# 最高、最低（用简单循环，不用 max 高级写法）
high_name = ""
high_score = -1
low_name = ""
low_score = 9999

for name in scores:
    s = scores[name]
    if s > high_score:
        high_score = s
        high_name = name
    if s < low_score:
        low_score = s
        low_name = name

print("最高:", high_name, high_score)
print("最低:", low_name, low_score)

print("不低于平均分的同学:")
for name in scores:
    if scores[name] >= avg:
        print(" ", name, scores[name])
