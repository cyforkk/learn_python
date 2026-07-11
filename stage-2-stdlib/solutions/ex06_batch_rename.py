names = ["b.txt", "a.txt", "c.txt"]
names.sort()
i = 1
for name in names:
    print(name, "->", f"file_{i}.txt")
    i = i + 1
