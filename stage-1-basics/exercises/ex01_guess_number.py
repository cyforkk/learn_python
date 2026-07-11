"""
练习 01：猜数字（限制次数）

要求：
1. 随机生成 1～100 的整数（可用 import random）
2. 用户最多猜 7 次
3. 每次提示「太大了」/「太小了」/「猜对了」
4. 猜对则提前结束，并打印用了几次
5. 7 次都错则公布正确答案

自检（测纯函数，不测交互）：
  python ex01_guess_number.py --check
交互运行：
  python ex01_guess_number.py
"""


def compare_guess(guess: int, answer: int) -> str:
    """返回 'low' | 'high' | 'ok'。"""
    # TODO
    raise NotImplementedError


def main() -> None:
    # TODO: 在这里实现完整游戏（可调用 compare_guess）
    pass


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
