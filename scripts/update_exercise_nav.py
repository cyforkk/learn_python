"""统一更新各笔记文末「本仓库学习导航」中的练习安排说明。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path relative to repo -> footer body after heading (markdown)
FOOTERS: dict[str, str] = {
    "stage-1-basics/notes/Python基本数据类型.md": """
- **练习安排：无仓库练习**（本篇只了解类型名字）
- 容器以后再练 → [Python复合类型.md](Python复合类型.md)
- 地图：[docs/learning-map.md](../../docs/learning-map.md) · 原则：[docs/exercise-policy.md](../../docs/exercise-policy.md)
""",
    "stage-1-basics/notes/Python输入输出.md": """
- **练习安排：无独立练习**（`input`/`print` 会在猜数字里用到）
- 学完「条件与循环」后做 → [ex01 猜数字](../exercises/ex01_guess_number.py)
- 下一篇：[Python运算符与表达式.md](Python运算符与表达式.md)
""",
    "stage-1-basics/notes/Python运算符与表达式.md": """
- **练习安排：无独立练习**
- 学完「函数」后可选 → [ex02 计算器](../exercises/ex02_calculator.py)（加练）
- 下一篇：[Python条件与循环.md](Python条件与循环.md)
""",
    "stage-1-basics/notes/Python条件与循环.md": """
- **练习安排：过关**
  - [ex04 九九表](../exercises/ex04_multiplication_table.py)（建议先做）
  - [ex01 猜数字](../exercises/ex01_guess_number.py)
- 新手说明：[../exercises/新手怎么做.md](../exercises/新手怎么做.md)
""",
    "stage-1-basics/notes/Python复合类型.md": """
- **练习安排**
  - **过关** [ex03 成绩统计](../exercises/ex03_score_stats.py)
  - **加练** [ex06 通讯录](../exercises/ex06_contacts.py)
- 须先读完本篇再做；不要在「基本数据类型」篇后硬做
""",
    "stage-1-basics/notes/Python字符串方法与格式化.md": """
- **练习安排：无独立练习**（写九九表、猜数字时自然会用到字符串）
- 继续：[Python函数.md](Python函数.md)
""",
    "stage-1-basics/notes/Python函数.md": """
- **练习安排**
  - **过关** [ex05 函数重构](../exercises/ex05_refactor_functions.py)
  - **加练** [ex02 计算器](../exercises/ex02_calculator.py)
- 作用域无需单独做题，读 [Python作用域.md](Python作用域.md) 即可
""",
    "stage-1-basics/notes/Python作用域.md": """
- **练习安排：无独立练习**（理解即可，结合函数篇的 ex05）
- 阶段 1 过关题汇总：ex04、ex01、ex03、ex05 → [../exercises/README.md](../exercises/README.md)
""",
    "stage-2-stdlib/notes/Python文件读写.md": """
- **练习安排：本篇读完先不急着做综合题**
- 与「异常处理」一起读完后 **过关** → [ex02 安全读文件](../exercises/ex02_safe_read.py)
- JSON 待办是综合题，**加练** → [ex01](../exercises/ex01_todo_json.py)
""",
    "stage-2-stdlib/notes/Python异常处理.md": """
- **练习安排：过关** [ex02 安全读文件](../exercises/ex02_safe_read.py)  
  （请已读完「文件读写」）
""",
    "stage-2-stdlib/notes/Python模块与包.md": """
- **练习安排：过关** [ex03 小模块](../exercises/ex03_mini_package/)
""",
    "stage-2-stdlib/notes/Python常用标准库.md": """
- **练习安排：加练** [ex04 列目录](../exercises/ex04_list_files.py)  
  批量重命名 **加练** → [ex06](../exercises/ex06_batch_rename.py)
- 不是每章标准库都要交作业，会查文档更重要
""",
    "stage-2-stdlib/notes/Python推导式.md": """
- **练习安排：无独立练习**（了解写法即可，代码里见到能读懂）
""",
    "stage-2-stdlib/notes/Python面向对象入门.md": """
- **练习安排：过关** [ex05 Book 类](../exercises/ex05_book_class.py)
""",
    "stage-3-engineering/notes/Python虚拟环境.md": """
- **练习安排：建议做** [ex01 venv 实践](../exercises/ex01_venv_practice.md)（跟着命令勾选即可）
""",
    "stage-3-engineering/notes/Python包管理工具.md": """
- **练习安排：无独立新题**（与虚拟环境篇的 ex01 一起完成即可）
- 综合工程 **加练** → [ex05 迷你工程](../exercises/ex05_mini_project/)
""",
    "stage-3-engineering/notes/Python代码风格PEP8.md": """
- **练习安排：无仓库题**（对照自己写过的练习改命名/空格即可）
- 参考：[docs/faq-common-mistakes.md](../../docs/faq-common-mistakes.md)
""",
    "stage-3-engineering/notes/Python类型注解入门.md": """
- **练习安排：加练** [ex02 类型注解](../exercises/ex02_typed_functions.py)  
  新手可整题跳过，不影响学 Python 主线
""",
    "stage-3-engineering/notes/Python调试技巧.md": """
- **练习安排：建议做** [ex04 调试日记](../exercises/ex04_debug_journal.md)（写一篇记录即可）
""",
    "stage-3-engineering/notes/Python测试入门.md": """
- **练习安排：加练** [ex03 pytest](../exercises/ex03_pytest_stats/)  
  **可以整段不做**；测试不是语法入门必选项
""",
    "stage-3-engineering/notes/Git基础入门.md": """
- **练习安排：无强制仓库题**（在本仓库 `git add` / `commit` 练即可）
""",
}


def replace_nav(path: Path, body: str) -> bool:
    text = path.read_text(encoding="utf-8")
    marker = "## 本仓库学习导航"
    if marker not in text:
        # append
        new = text.rstrip() + "\n\n---\n\n" + marker + "\n" + body.strip() + "\n"
        path.write_text(new, encoding="utf-8")
        return True
    head, _sep, _rest = text.partition(marker)
    # drop old nav until end (assume nav is last section)
    new = head.rstrip() + "\n\n" + marker + "\n" + body.strip() + "\n"
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for rel, body in FOOTERS.items():
        path = ROOT / rel
        if not path.exists():
            print("MISS", rel)
            continue
        if replace_nav(path, body):
            n += 1
            print("OK", rel)
        else:
            print("SAME", rel)
    print("updated", n)


if __name__ == "__main__":
    main()
