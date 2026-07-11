"""被测试模块：mean / clamp。"""


def mean(nums: list[float]) -> float:
    """空列表应抛出 ValueError。"""
    if not nums:
        raise ValueError("nums 不能为空")
    return sum(nums) / len(nums)


def clamp(value: float, low: float, high: float) -> float:
    """将 value 限制在 [low, high]。"""
    return max(low, min(high, value))
