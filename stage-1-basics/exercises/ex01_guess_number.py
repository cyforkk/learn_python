"""
练习 01：猜数字（限制次数）

【新手】先做到：运行 python ex01_guess_number.py 能玩起来。
  全部逻辑写在 main() 里也可以，不必纠结函数怎么拆。
  文件后半的 _selfcheck / --check 可暂时忽略。

要求：
1. 随机生成 1～100 的整数（可用 import random）
2. 用户最多猜 7 次
3. 每次提示「太大了」/「太小了」/「猜对了」
4. 猜对则提前结束，并打印用了几次
5. 7 次都错则公布正确答案

运行：python ex01_guess_number.py
可选自检（以后再说）：python ex01_guess_number.py --check
"""

import random


def compare_guess(guess: int, answer: int) -> str:
    """返回 'low' | 'high' | 'ok'。"""
    if guess < answer:
        return "low"
    if guess > answer:
        return "high"
    return "ok"


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

        result = compare_guess(guess, answer)
        if result == "low":
            print("太小了")
        elif result == "high":
            print("太大了")
        else:
            print(f"猜对了！用了 {attempt} 次。")
            return

    print(f"次数用尽。正确答案是 {answer}。")


def _selfcheck() -> None:
    assert compare_guess(10, 50) == "low"
    assert compare_guess(90, 50) == "high"
    assert compare_guess(50, 50) == "ok"
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
