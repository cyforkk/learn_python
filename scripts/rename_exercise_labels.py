"""把「选做」改为「加练」，「必做」在标签语境改为「过关」。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = [
    ("（综合选做）", "（综合加练）"),
    ("## 选做 / 可整段跳过", "## 加练（可选）/ 可整段跳过"),
    ("## 选做（有余力）", "## 加练（可选 · 难度往往差不多）"),
    ("## 选做", "## 加练（可选）"),
    ("### 练习（多数为建议/选做）", "### 练习（多数为建议/加练）"),
    ("（选做 · 最简单版 · 只打印不真改）", "（加练 · 最简单版 · 只打印不真改）"),
    ("（选做 · 尽量简单）", "（加练 · 尽量简单）"),
    ("（选做 · 最简单版）", "（加练 · 最简单版）"),
    ("选做 · 最简单版", "加练 · 最简单版"),
    ("通讯录选做题更简单", "通讯录加练题同样简单（难度相近）"),
    ("综合选做", "综合加练"),
    ("（选做）", "（加练）"),
    ("**选做**", "**加练**"),
    ("选做 ", "加练 "),
    (" 选做", " 加练"),
    ("含「无/必做/选做」", "含「无/过关/加练」"),
    ("无 / 必做 / 选做", "无 / 过关 / 加练"),
    ("「无 / 必做 / 选做」", "「无 / 过关 / 加练」"),
    ("选做模块", "加练模块"),
    # 必做 → 过关（展示用）
    ("**必做**", "**过关**"),
    ("必做 4 题", "过关 4 题"),
    ("必做 3 题", "过关 3 题"),
    ("4 道必做", "4 道过关题"),
    ("## 必做", "## 过关（必做）"),
    ("### 练习（必做", "### 练习（过关"),
    ("只要求下面 **4 道过关题**", "只要求下面 **4 道过关题**"),
    ("阶段 1 你只要完成 4 道必做", "阶段 1 你只要完成 4 道过关题"),
    ("**必做 4 题**", "**过关 4 题**"),
    ("练习安排：必做", "练习安排：过关"),
    ("- **练习安排：过关**", "- **练习安排：过关**"),
]


def main() -> None:
    changed: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".py"}:
            continue
        if path.name == "rename_exercise_labels.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        orig = text
        for a, b in REPLACEMENTS:
            text = text.replace(a, b)
        text = text.replace("**过关过关**", "**过关**")
        text = text.replace("加练加练", "加练")
        text = text.replace("## 过关（必做）（必做）", "## 过关（必做）")
        if text != orig:
            path.write_text(text, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))
    print("changed", len(changed))
    for c in sorted(changed):
        print(c)


if __name__ == "__main__":
    main()
