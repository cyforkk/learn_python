"""AI 方向 starter：无 API Key 的关键词「小助手」（先理解输入→规则→输出）。"""


def reply(text: str) -> str:
    t = text.strip().lower()
    if any(w in t for w in ("你好", "hello", "hi")):
        return "你好！我是规则版小助手，可先用来练交互结构。"
    if any(w in t for w in ("python", "学习")):
        return "建议路径：语法 → 标准库 → 一个小项目 → 再学框架/模型。"
    if any(w in t for w in ("天气", "weather")):
        return "我还不会查真天气；接 API 后可以把这里换成真实调用。"
    return "我只认识少量关键词。试试：你好 / Python / 天气"


def main() -> None:
    samples = ["你好", "怎么学 Python", "今天天气", "随便聊聊"]
    for s in samples:
        print(f"用户: {s}")
        print(f"助手: {reply(s)}")
        print("---")


if __name__ == "__main__":
    main()
