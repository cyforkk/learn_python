# 练习：通讯录（加练 · 最简单版）
# 先读笔记：复合类型
# 运行：python ex06_contacts.py

book = {}

book["小明"] = "13800000001"
book["小红"] = "13900000002"

print("小明的电话:", book.get("小明"))
print("所有人:")
for name in book:
    print(" ", name, book[name])
