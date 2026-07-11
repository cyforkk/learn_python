"""
练习 05：把重复逻辑抽成函数

下面脚本有重复代码。请重构：
1. 编写函数 grade_level(score: float) -> str
   - score >= 90 -> "A"
   - score >= 80 -> "B"
   - score >= 60 -> "C"
   - 否则 -> "D"
2. 编写函数 summarize(name: str, score: float) -> str
   - 返回类似 "Ada: 92 -> A" 的字符串
3. main 里对多个学生调用 summarize 并打印
4. 删除重复的 if/elif 块

运行：python ex05_refactor_functions.py
"""


def grade_level(score: float) -> str:
    # TODO
    raise NotImplementedError


def summarize(name: str, score: float) -> str:
    # TODO
    raise NotImplementedError


def main() -> None:
    # 重构前（请删掉重复逻辑，改为调用函数）：
    # name, score = "Ada", 92
    # if score >= 90:
    #     level = "A"
    # ...
    students = [("Ada", 92.0), ("Bob", 78.0), ("Cindy", 55.0)]
    # TODO
    pass


if __name__ == "__main__":
    main()
