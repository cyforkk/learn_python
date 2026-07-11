# 练习：批量重命名计划（选做 · 最简单版 · 只打印不真改）
# 运行：python ex06_batch_rename.py

from pathlib import Path

# 示例：假装有这些文件名
names = ["b.txt", "a.txt", "c.txt"]
names.sort()

print("重命名计划（不会真的改文件）:")
i = 1
for name in names:
    print(name, "->", f"file_{i}.txt")
    i = i + 1
