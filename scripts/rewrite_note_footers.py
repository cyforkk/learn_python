"""统一各笔记文末：本课衔接（上/下篇 + 本篇练习），不链到 exercises/README。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# path -> full footer markdown after replacing from first ## 本仓库 or ## 读完本篇
FOOTERS: dict[str, str] = {
    "stage-1-basics/notes/Python基本数据类型.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | （阶段 1 起点） |
| **下一篇** | [Python输入输出.md](Python输入输出.md) |
| **本篇练习** | **无**。本篇只认识类型；容器真正练在后面 [复合类型](Python复合类型.md)。 |

可选：在交互里敲几行 `type(1)`、`type("a")` 感受一下即可，**不算仓库作业**。
""",
    "stage-1-basics/notes/Python输入输出.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python基本数据类型.md](Python基本数据类型.md) |
| **下一篇** | [Python运算符与表达式.md](Python运算符与表达式.md) |
| **本篇练习** | **无独立作业**。`print` / `input` 会用在后面的猜数字题里。 |

继续读下一篇；做练习要等学完 [条件与循环](Python条件与循环.md)。
""",
    "stage-1-basics/notes/Python运算符与表达式.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python输入输出.md](Python输入输出.md) |
| **下一篇** | [Python条件与循环.md](Python条件与循环.md) |
| **本篇练习** | **无独立作业**。比较、算术会用在循环题和加练计算器里。 |
""",
    "stage-1-basics/notes/Python条件与循环.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python运算符与表达式.md](Python运算符与表达式.md) |
| **下一篇** | [Python复合类型.md](Python复合类型.md) |
| **本篇练习** | **过关 2 题**（先做九九表，再做猜数字） |

### 过关 1 · 九九乘法表

**题目：** 两层 `for` 打印下三角九九表；不要手写 81 行 `print`。

- 作业（空白）：[exercises/ex04_multiplication_table.py](../exercises/ex04_multiplication_table.py)
- 答案（做完再看）：[solutions/ex04_multiplication_table.py](../solutions/ex04_multiplication_table.py)

### 过关 2 · 猜数字

**题目：** 随机 1～100，最多 7 次；提示太大/太小/猜对；用尽次数公布答案。

- 作业（空白）：[exercises/ex01_guess_number.py](../exercises/ex01_guess_number.py)
- 答案（做完再看）：[solutions/ex01_guess_number.py](../solutions/ex01_guess_number.py)

做完再读下一篇「复合类型」。
""",
    "stage-1-basics/notes/Python复合类型.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python条件与循环.md](Python条件与循环.md)（应已做过九九表、猜数字） |
| **下一篇** | [Python字符串方法与格式化.md](Python字符串方法与格式化.md) |
| **本篇练习** | **过关 1 题** + **加练 1 题（可选）** |

### 过关 · 成绩统计

**题目：** 字典存至少 4 名学生成绩；打印平均分、最高/最低及姓名、不低于平均分的学生。

- 作业（空白）：[exercises/ex03_score_stats.py](../exercises/ex03_score_stats.py)
- 答案（做完再看）：[solutions/ex03_score_stats.py](../solutions/ex03_score_stats.py)

### 加练（可选）· 通讯录

**题目：** 字典存姓名→电话；能添加、查找、列出。难度与成绩题接近，多练一遍字典。

- 作业（空白）：[exercises/ex06_contacts.py](../exercises/ex06_contacts.py)
- 答案（做完再看）：[solutions/ex06_contacts.py](../solutions/ex06_contacts.py)
""",
    "stage-1-basics/notes/Python字符串方法与格式化.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python复合类型.md](Python复合类型.md) |
| **下一篇** | [Python函数.md](Python函数.md) |
| **本篇练习** | **无独立作业**。 |

**和前后的关系：** 九九表、猜数字、成绩题里用到的 `f"..."`、字符串拼接，就是本篇内容。可回头打开你写过的作业，标出用到了哪些字符串写法。
""",
    "stage-1-basics/notes/Python函数.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python字符串方法与格式化.md](Python字符串方法与格式化.md) |
| **下一篇** | [Python作用域.md](Python作用域.md) |
| **本篇练习** | **过关 1 题** + **加练 1 题（可选）** |

### 过关 · 成绩等级函数

**题目：** 写 `level(score)` 返回 A/B/C/D；对几个分数调用并打印。

- 作业（空白）：[exercises/ex05_refactor_functions.py](../exercises/ex05_refactor_functions.py)
- 答案（做完再看）：[solutions/ex05_refactor_functions.py](../solutions/ex05_refactor_functions.py)

### 加练（可选）· 计算器

**题目：** 循环读 `数字 运算符 数字`，支持 + - * /，除零提示，`q` 退出。

- 作业（空白）：[exercises/ex02_calculator.py](../exercises/ex02_calculator.py)
- 答案（做完再看）：[solutions/ex02_calculator.py](../solutions/ex02_calculator.py)

建议：做完过关题后，立刻读 [作用域](Python作用域.md)，对照 `level` 里的 `score` 想「局部变量」。
""",
    "stage-1-basics/notes/Python作用域.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python函数.md](Python函数.md)（应已做过等级函数 ex05） |
| **下一篇** | 阶段 1 结束 → [阶段 2 入口](../../stage-2-stdlib/README.md) |
| **本篇练习** | **无独立新作业**（不链练习总表） |

**和前后的关系（重要）：**

1. 打开你写的 [ex05 等级函数作业](../exercises/ex05_refactor_functions.py)（或 [答案](../solutions/ex05_refactor_functions.py)）  
2. 想一想：`score` 是局部变量还是全局？在函数外能不能直接用？  
3. 若做过加练 [计算器](../exercises/ex02_calculator.py)，循环里的 `a`/`b` 也只在那次循环逻辑里有意义  

本篇是对「函数」的加深理解，**不另出题**；阶段 1 过关仍是：ex04、ex01、ex03、ex05。

阶段 1 做完后进入 → [stage-2-stdlib/README.md](../../stage-2-stdlib/README.md)
""",
    "stage-2-stdlib/notes/Python文件读写.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | （阶段 2 起点）← [阶段 1](../../stage-1-basics/README.md) |
| **下一篇** | [Python异常处理.md](Python异常处理.md) |
| **本篇练习** | **本篇读完先不做题**；与下一篇异常一起做「安全读文件」。 |

先继续读异常处理，两篇都读完再写作业。
""",
    "stage-2-stdlib/notes/Python异常处理.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python文件读写.md](Python文件读写.md) |
| **下一篇** | [Python模块与包.md](Python模块与包.md) |
| **本篇练习** | **过关 1 题**（文件 + 异常合练） |

### 过关 · 安全读文件

**题目：** 输入路径 → 读文件打印；不存在则提示且不崩溃。

- 作业（空白）：[exercises/ex02_safe_read.py](../exercises/ex02_safe_read.py)
- 答案（做完再看）：[solutions/ex02_safe_read.py](../solutions/ex02_safe_read.py)

### 加练（可选）· JSON 待办

**题目：** JSON 存待办；命令 add / list / quit。

- 作业（空白）：[exercises/ex01_todo_json.py](../exercises/ex01_todo_json.py)
- 答案（做完再看）：[solutions/ex01_todo_json.py](../solutions/ex01_todo_json.py)
""",
    "stage-2-stdlib/notes/Python模块与包.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python异常处理.md](Python异常处理.md) |
| **下一篇** | [Python常用标准库.md](Python常用标准库.md) |
| **本篇练习** | **过关 1 题** |

### 过关 · 小模块

**题目：** 同目录 `greeter.py` + `main.py`；`greet(name)`；main 里 import 调用。

- 作业（空白）：[exercises/ex03_mini_package/](../exercises/ex03_mini_package/)
- 答案（做完再看）：[solutions/ex03_mini_package/](../solutions/ex03_mini_package/)
""",
    "stage-2-stdlib/notes/Python常用标准库.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python模块与包.md](Python模块与包.md) |
| **下一篇** | [Python推导式.md](Python推导式.md) |
| **本篇练习** | **无过关题**；以下为加练（可选，难度接近过关题） |

### 加练（可选）· 列目录

**题目：** 列出当前目录的文件/文件夹。

- 作业（空白）：[exercises/ex04_list_files.py](../exercises/ex04_list_files.py)
- 答案（做完再看）：[solutions/ex04_list_files.py](../solutions/ex04_list_files.py)

### 加练（可选）· 重命名计划

**题目：** 打印「旧名 → 新名」计划（可不真改文件）。

- 作业（空白）：[exercises/ex06_batch_rename.py](../exercises/ex06_batch_rename.py)
- 答案（做完再看）：[solutions/ex06_batch_rename.py](../solutions/ex06_batch_rename.py)
""",
    "stage-2-stdlib/notes/Python推导式.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python常用标准库.md](Python常用标准库.md) |
| **下一篇** | [Python面向对象入门.md](Python面向对象入门.md) |
| **本篇练习** | **无独立作业**。 |

**和前后的关系：** 能读懂 `[x for x in ...]` 即可。以后写列表过滤时用得到；过关不要求单独交推导式作业。继续读面向对象。
""",
    "stage-2-stdlib/notes/Python面向对象入门.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python推导式.md](Python推导式.md) |
| **下一篇** | 阶段 2 结束 → [阶段 3 入口](../../stage-3-engineering/README.md) |
| **本篇练习** | **过关 1 题** |

### 过关 · Book 类

**题目：** 类 `Book`（书名、作者、页数）；`info()`；`is_long()`（页数≥300）；创建至少 2 本并打印。

- 作业（空白）：[exercises/ex05_book_class.py](../exercises/ex05_book_class.py)
- 答案（做完再看）：[solutions/ex05_book_class.py](../solutions/ex05_book_class.py)

阶段 2 过关题：ex02、ex03、ex05。然后进入 → [stage-3-engineering/README.md](../../stage-3-engineering/README.md)
""",
    "stage-3-engineering/notes/Python虚拟环境.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | （阶段 3 起点）← [阶段 2](../../stage-2-stdlib/README.md) |
| **下一篇** | [Python包管理工具.md](Python包管理工具.md) |
| **本篇练习** | **建议** 做一遍 ex01（跟命令勾选，不是编程大题） |

### 建议 · 虚拟环境实践

**题目：** 创建 venv、激活、装包；知道 `.venv` 不要提交 Git。

- 作业步骤：[exercises/ex01_venv_practice.md](../exercises/ex01_venv_practice.md)
""",
    "stage-3-engineering/notes/Python包管理工具.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python虚拟环境.md](Python虚拟环境.md) |
| **下一篇** | [Python代码风格PEP8.md](Python代码风格PEP8.md) |
| **本篇练习** | **无新作业**（与虚拟环境的 ex01 一起完成即可） |

### 加练（可选）· 迷你工程

**题目：** 小包 + 依赖说明 + 能跑通。

- 作业：[exercises/ex05_mini_project/](../exercises/ex05_mini_project/)
""",
    "stage-3-engineering/notes/Python代码风格PEP8.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python包管理工具.md](Python包管理工具.md) |
| **下一篇** | [Python类型注解入门.md](Python类型注解入门.md) |
| **本篇练习** | **无仓库新题** |

**和前后的关系：** 打开你阶段 1～2 写过的作业（如猜数字、成绩），对照本篇改命名/空格即可，不必交新文件。
""",
    "stage-3-engineering/notes/Python类型注解入门.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python代码风格PEP8.md](Python代码风格PEP8.md) |
| **下一篇** | [Python调试技巧.md](Python调试技巧.md) |
| **本篇练习** | **加练（可选）**，可整题跳过 |

### 加练 · 类型注解

**题目：** 给若干函数补参数/返回值注解，行为不变。

- 作业（空白）：[exercises/ex02_typed_functions.py](../exercises/ex02_typed_functions.py)
""",
    "stage-3-engineering/notes/Python调试技巧.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python类型注解入门.md](Python类型注解入门.md) |
| **下一篇** | [Python测试入门.md](Python测试入门.md) |
| **本篇练习** | **建议** 写一篇调试日记 |

### 建议 · 调试日记

**题目：** 遇到或制造一次报错 → 读 Traceback → 修好 → 写记录。

- 作业：[exercises/ex04_debug_journal.md](../exercises/ex04_debug_journal.md)
""",
    "stage-3-engineering/notes/Python测试入门.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python调试技巧.md](Python调试技巧.md) |
| **下一篇** | [Git基础入门.md](Git基础入门.md) |
| **本篇练习** | **加练（可选）**，语法主线可整段不做 |

### 加练 · pytest

**题目：** 实现 `stats.py`；可用 `test_*.py` 测试（`test_` 文件是测试不是业务）。

- 作业目录：[exercises/ex03_pytest_stats/](../exercises/ex03_pytest_stats/)
""",
    "stage-3-engineering/notes/Git基础入门.md": """
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python测试入门.md](Python测试入门.md) |
| **下一篇** | 阶段 3 结束 → [阶段 4 入口](../../stage-4-tracks/README.md) |
| **本篇练习** | **无强制新题** |

**和前后的关系：** 在本仓库对你改过的作业 `git add` / `commit` 练即可。  
然后进入方向学习 → [stage-4-tracks/README.md](../../stage-4-tracks/README.md)
""",
}


def strip_old_footer(text: str) -> str:
    markers = [
        "\n---\n\n## 本课衔接",
        "\n## 本课衔接",
        "\n---\n\n## 本仓库练习",
        "\n## 本仓库练习",
        "\n---\n\n## 本仓库学习导航",
        "\n## 本仓库学习导航",
        "\n---\n\n## 读完本篇做什么",
        "\n## 读完本篇做什么",
    ]
    cut = len(text)
    for m in markers:
        i = text.find(m)
        if i != -1 and i < cut:
            cut = i
    return text[:cut].rstrip() + "\n"


def main() -> None:
    for rel, footer in FOOTERS.items():
        path = ROOT / rel
        if not path.exists():
            print("MISS", rel)
            continue
        body = strip_old_footer(path.read_text(encoding="utf-8"))
        path.write_text(body + "\n" + footer.strip() + "\n", encoding="utf-8")
        print("OK", rel)


if __name__ == "__main__":
    main()
