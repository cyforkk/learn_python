# 阶段 1 · 语法核心

**目标**：不看笔记也能写出 list/dict 遍历、if/for、自定义函数。  
**建议时间**：1～2 周（每天 1～2 小时）。

## 学什么

变量与类型、输入输出、运算符、条件与循环、列表/字典等容器、字符串、函数、作用域。

## 阅读顺序（notes/）

1. [Python基本数据类型.md](notes/Python基本数据类型.md)
2. [Python输入输出.md](notes/Python输入输出.md)
3. [Python运算符与表达式.md](notes/Python运算符与表达式.md)
4. [Python条件与循环.md](notes/Python条件与循环.md)
5. [Python复合类型.md](notes/Python复合类型.md)
6. [Python字符串方法与格式化.md](notes/Python字符串方法与格式化.md)
7. [Python函数.md](notes/Python函数.md)
8. [Python作用域.md](notes/Python作用域.md)

笔记中有完整示例，可运行理解；**练习请独立完成**。

## 练习（exercises/）

| 文件 | 内容 |
|------|------|
| [ex01_guess_number.py](exercises/ex01_guess_number.py) | 猜数字（限制次数） |
| [ex02_calculator.py](exercises/ex02_calculator.py) | 简易计算器 |
| [ex03_score_stats.py](exercises/ex03_score_stats.py) | 学生成绩字典统计 |
| [ex04_multiplication_table.py](exercises/ex04_multiplication_table.py) | 九九乘法表 |
| [ex05_refactor_functions.py](exercises/ex05_refactor_functions.py) | 重复逻辑抽成函数 |

运行示例：

```bash
cd stage-1-basics/exercises
python ex01_guess_number.py
```

参考答案在 [solutions/](solutions/)，**做完再看**。

## 验收标准

- 能手写：for 遍历列表、字典读写、带参数和返回值的函数
- 能解释：list 可变 vs tuple/str 不可变（基本概念）
- 5 道练习均可运行且符合题目要求

## 下一步

[../stage-2-stdlib/README.md](../stage-2-stdlib/README.md)
