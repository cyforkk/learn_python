"""Append learning navigation footers to topic notes. Run from repo root."""

from pathlib import Path

MARKER = "\n\n---\n\n## 本仓库学习导航\n"

FOOTERS = {
    "stage-1-basics/notes/Python基本数据类型.md": "本篇无仓库练习（只了解）；容器练习见复合类型 · 地图：[docs/learning-map.md](../../docs/learning-map.md)",
    "stage-1-basics/notes/Python输入输出.md": "对应练习： [ex01](../exercises/ex01_guess_number.py) [ex02](../exercises/ex02_calculator.py)",
    "stage-1-basics/notes/Python运算符与表达式.md": "对应练习： [ex02_calculator](../exercises/ex02_calculator.py)",
    "stage-1-basics/notes/Python条件与循环.md": "对应练习： [ex01](../exercises/ex01_guess_number.py) [ex04](../exercises/ex04_multiplication_table.py)",
    "stage-1-basics/notes/Python复合类型.md": "对应练习： [ex03](../exercises/ex03_score_stats.py) [ex06 通讯录](../exercises/ex06_contacts.py)",
    "stage-1-basics/notes/Python字符串方法与格式化.md": "对应练习： [ex04](../exercises/ex04_multiplication_table.py) [ex05](../exercises/ex05_refactor_functions.py)",
    "stage-1-basics/notes/Python函数.md": "对应练习： [ex02](../exercises/ex02_calculator.py) [ex05](../exercises/ex05_refactor_functions.py) [ex06](../exercises/ex06_contacts.py)",
    "stage-1-basics/notes/Python作用域.md": "对应练习： [ex05_refactor_functions](../exercises/ex05_refactor_functions.py)",
    "stage-2-stdlib/notes/Python文件读写.md": "对应练习： [ex01](../exercises/ex01_todo_json.py) [ex02](../exercises/ex02_safe_read.py)",
    "stage-2-stdlib/notes/Python异常处理.md": "对应练习： [ex02_safe_read](../exercises/ex02_safe_read.py)",
    "stage-2-stdlib/notes/Python模块与包.md": "对应练习： [ex03_mini_package](../exercises/ex03_mini_package/)",
    "stage-2-stdlib/notes/Python常用标准库.md": "对应练习： [ex01](../exercises/ex01_todo_json.py) [ex04](../exercises/ex04_list_files.py) [ex06](../exercises/ex06_batch_rename.py)",
    "stage-2-stdlib/notes/Python推导式.md": "对应练习： [ex04_list_files](../exercises/ex04_list_files.py) [ex06](../exercises/ex06_batch_rename.py)",
    "stage-2-stdlib/notes/Python面向对象入门.md": "对应练习： [ex05_book_class](../exercises/ex05_book_class.py)",
    "stage-3-engineering/notes/Python虚拟环境.md": "对应练习： [ex01_venv_practice](../exercises/ex01_venv_practice.md) [ex05_mini_project](../exercises/ex05_mini_project/)",
    "stage-3-engineering/notes/Python包管理工具.md": "对应练习： [ex01](../exercises/ex01_venv_practice.md) [ex05](../exercises/ex05_mini_project/)",
    "stage-3-engineering/notes/Python代码风格PEP8.md": "对照自己的 exercises 代码；见 [FAQ](../../docs/faq-common-mistakes.md)",
    "stage-3-engineering/notes/Python类型注解入门.md": "对应练习： [ex02_typed_functions](../exercises/ex02_typed_functions.py)",
    "stage-3-engineering/notes/Python调试技巧.md": "对应练习： [ex04_debug_journal](../exercises/ex04_debug_journal.md)",
    "stage-3-engineering/notes/Python测试入门.md": "对应练习： [ex03_pytest_stats](../exercises/ex03_pytest_stats/) [ex05](../exercises/ex05_mini_project/)",
    "stage-3-engineering/notes/Git基础入门.md": "在本仓库练习 add/commit；见根目录 CONTRIBUTING.md",
    "stage-5-projects/notes/Python实战练习.md": "项目实现： [projects/todo-cli](../../projects/todo-cli/) 等",
    "stage-5-projects/notes/Python综合实战.md": "项目规格： [../exercises/](../exercises/) · 实现 [../../projects/](../../projects/)",
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    for rel, tip in FOOTERS.items():
        path = root / rel
        if not path.exists():
            print("MISS", rel)
            continue
        text = path.read_text(encoding="utf-8")
        if "## 本仓库学习导航" in text:
            print("SKIP", rel)
            continue
        path.write_text(text.rstrip() + MARKER + tip + "\n", encoding="utf-8")
        print("OK", rel)


if __name__ == "__main__":
    main()
