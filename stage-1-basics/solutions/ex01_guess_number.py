"""参考答案：ex01 猜数字（限次）。请先独立完成 exercises 再对照。"""

import random


def main() -> None:
    answer = random.randint(1, 100)
    max_tries = 7
    print(f"我想了一个 1-100 的数字，你有 {max_tries} 次机会。")

    for attempt in range(1, max_tries + 1):
        raw = input(f"第 {attempt} 次猜测: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("请输入整数。")
            continue

        if guess < answer:
            print("太小了")
        elif guess > answer:
            print("太大了")
        else:
            print(f"猜对了！用了 {attempt} 次。")
            return

    print(f"次数用尽。正确答案是 {answer}。")


if __name__ == "__main__":
    main()
