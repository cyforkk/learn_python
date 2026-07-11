"""参考答案：ex04 九九乘法表。"""


def print_table() -> None:
    for i in range(1, 10):
        row = []
        for j in range(1, i + 1):
            row.append(f"{j}*{i}={j * i}")
        print("\t".join(row))


if __name__ == "__main__":
    print_table()
