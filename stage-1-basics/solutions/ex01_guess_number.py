"""参考答案：ex01 猜数字（限次）。请先独立完成 exercises 再对照。"""

import random


def compare_guess(guess: int, answer: int) -> str:
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


# ---------------------------------------------------------------------------
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
# 函数名 _selfcheck：用 assert 自动检查上面业务代码对不对。
# 这不是题目要求写的功能，也不会在正常运行时执行。
# 你只需完成上面的 main / 业务函数，运行:  python 本文件.py
# 以后想自检再运行:  python 本文件.py --check
# ---------------------------------------------------------------------------
def _selfcheck() -> None:
    assert compare_guess(10, 50) == "low"
    assert compare_guess(90, 50) == "high"
    assert compare_guess(50, 50) == "ok"
    print("selfcheck OK")


if __name__ == "__main__":
    import sys

    # --check 才会调用上面的【测试函数 _selfcheck】；新手不要加这个参数
    if "--check" in sys.argv:
        _selfcheck()
    else:
        main()
