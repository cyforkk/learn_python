# 练习：猜数字（最简单版）
# 先读笔记：条件与循环（会用到 input）
# 运行：python ex01_guess_number.py
#
# 目标：随机 1～100，最多猜 7 次，提示太大/太小/猜对。

import random

answer = random.randint(1, 100)
print("我想了一个 1～100 的数字，你有 7 次机会。")

for n in range(1, 8):
    guess = int(input(f"第 {n} 次: "))
    if guess < answer:
        print("太小了")
    elif guess > answer:
        print("太大了")
    else:
        print("猜对了！")
        break
else:
    # for 正常结束（没 break）才会走到这里
    print("次数用完了，答案是", answer)
