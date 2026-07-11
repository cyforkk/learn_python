"""业务函数（被测试的对象，不是测试本身）。"""


def mean(nums: list[float]) -> float:
    if not nums:
        raise ValueError("nums 不能为空")
    return sum(nums) / len(nums)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))
