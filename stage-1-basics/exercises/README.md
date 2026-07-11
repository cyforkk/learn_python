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
| ③ | [ex03_score_stats.py](ex03_score_stats.py) | 成绩字典 | 复合类型 | 练字典 |

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

文件里可能有 `_selfcheck`、`--check`，那是**可选巩固**，不是入门门槛：

```bash
# 会了再跑；不会就跳过
python ex04_multiplication_table.py --check
```

- 看不懂 `assert` → 忽略文件后半段  
- 看不懂类型注解 `-> str` → 当普通 `def` 写  
- 答案里拆了很多函数 → 你第一版写在一个 `main` 里完全可以  

答案目录：`../solutions/`（**做完再看**）  
错题：[../../docs/faq-common-mistakes.md](../../docs/faq-common-mistakes.md)
