"""AI 中型 demo：规则分类 + 简单统计（无 API Key）。"""

from __future__ import annotations


POSITIVE = {"好", "棒", "喜欢", "开心", "优秀", "love", "great"}
NEGATIVE = {"差", "烂", "讨厌", "难过", "糟糕", "bad", "hate"}


def sentiment(text: str) -> str:
    t = text.lower()
    pos = sum(1 for w in POSITIVE if w in t)
    neg = sum(1 for w in NEGATIVE if w in t)
    if pos > neg:
        return "positive"
    if neg > pos:
        return "negative"
    return "neutral"


def main() -> None:
    samples = [
        "这个课程真不错，我很喜欢",
        "体验太差了，糟糕",
        "今天天气一般",
        "great job, love it",
    ]
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for s in samples:
        label = sentiment(s)
        counts[label] += 1
        print(f"[{label:8}] {s}")
    print("统计:", counts)
    print("下一步：把 sentiment() 换成真实 LLM / 模型 API 调用")


if __name__ == "__main__":
    main()
