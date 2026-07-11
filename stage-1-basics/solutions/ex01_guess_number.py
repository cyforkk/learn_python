# 参考答案：猜数字（最简单版）

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
    print("次数用完了，答案是", answer)
