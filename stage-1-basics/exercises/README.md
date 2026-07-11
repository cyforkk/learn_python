# 阶段 1 练习清单

> **先学后练**：先读 [../notes/](../notes/)，再做题。  
> **新手请先看** → [新手怎么做.md](新手怎么做.md)（比本表更重要）

## 过关标准（新手）

- 程序能运行，行为符合题目文字要求  
- **不要求** 一上来会 `--check`、会写 `assert`、会 pytest  

## 新手建议路线（只做这些就够）

| 顺序 | 文件 | 主题 | 先读笔记 | 说明 |
|------|------|------|----------|------|
| ① | [ex04_multiplication_table.py](ex04_multiplication_table.py) | 九九表 | 条件与循环 | 最简单，优先 |
| ② | [ex01_guess_number.py](ex01_guess_number.py) | 猜数字 | 输入输出、循环 | 完整小游戏 |
| ③ | [ex03_score_stats.py](ex03_score_stats.py) | 成绩字典 | **复合类型**（不是「基本数据类型」篇） | 读完复合类型再做 |

运行（交互 / 看结果）：

```bash
python ex04_multiplication_table.py
python ex01_guess_number.py
python ex03_score_stats.py
```

## 学完「函数」后再做

| 文件 | 主题 | 先读笔记 |
|------|------|----------|
| [ex02_calculator.py](ex02_calculator.py) | 计算器 | 运算符、函数 |
| [ex05_refactor_functions.py](ex05_refactor_functions.py) | 拆函数 | 函数、作用域 |
| [ex06_contacts.py](ex06_contacts.py) | 通讯录 | 复合类型、函数 · **选做** |

## 关于「自检 / 测试」（可后学）

每个练习文件底部都有醒目注释：

```text
# 【测试 / 自检函数 · 新手请跳过，不必读、不必改】
def _selfcheck() -> None:
```

| 名字 | 是不是测试 | 新手 |
|------|------------|------|
| `main` / 题目里的业务函数 | 否，这是作业 | 要写 |
| `_selfcheck` | **是测试/自检** | 跳过 |
| `python xxx.py --check` | 才会跑测试 | 不要加这个参数 |

```bash
# 新手这样运行即可
python ex04_multiplication_table.py

# 可选（以后再说）
# python ex04_multiplication_table.py --check
```

答案目录：`../solutions/`（**做完再看**）  
错题：[../../docs/faq-common-mistakes.md](../../docs/faq-common-mistakes.md)
