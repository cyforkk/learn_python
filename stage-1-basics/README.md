# 阶段 1 · 语法核心

**目标**：不看笔记也能写出 list/dict 遍历、if/for、自定义函数。  
**建议时间**：1～2 周（每天 1～2 小时）。  
**地图**：[docs/learning-map.md](../docs/learning-map.md)

## 本阶段顺序（必须遵守）

```
① 按下方顺序读 notes/（先学）
② 相关笔记读完后，再做 exercises/（再练）
③ 做完再看 solutions/（后对）
```

不要一进本目录就打开 `exercises/`。

## 学什么

变量与类型、输入输出、运算符、条件与循环、列表/字典等容器、字符串、函数、作用域。

## ① 阅读顺序（notes/ · 第一站）

每篇文末有「对应练习」链接——**读完该篇再点**。

| 顺序 | 笔记 | 练习？ |
|------|------|--------|
| 1 | [基本数据类型](notes/Python基本数据类型.md) | **无**（只了解） |
| 2 | [输入输出](notes/Python输入输出.md) | **无** |
| 3 | [运算符与表达式](notes/Python运算符与表达式.md) | **无** |
| 4 | [条件与循环](notes/Python条件与循环.md) | **过关** ex04、ex01 |
| 5 | [复合类型](notes/Python复合类型.md) | **过关** ex03；加练 ex06 |
| 6 | [字符串方法与格式化](notes/Python字符串方法与格式化.md) | **无** |
| 7 | [函数](notes/Python函数.md) | **过关** ex05；加练 ex02 |
| 8 | [作用域](notes/Python作用域.md) | **无** |

原则：[docs/exercise-policy.md](../docs/exercise-policy.md)  
第一天：读 1～4 → 只做 **ex04 九九表**。

## ② 练习（读完对应笔记后 · 全是最简单脚本）

**新手必读**：[exercises/新手怎么做.md](exercises/新手怎么做.md)

- 作业里**没有**测试代码；自检若有，在 `exercises/checks/`（可忽略）  
- 九九表就是两层 `for` + `print`，没有花活  

```bash
cd stage-1-basics/exercises
python ex04_multiplication_table.py
python ex01_guess_number.py
```

## ③ 答案（做完再看）

[solutions/](solutions/) — 与练习同样是简单写法。

## 验收标准（新手版）

- 笔记能口述要点  
- **过关 4 题**跑通即可  
- **不要求** pytest、assert、类型注解  

## 下一步

[../stage-2-stdlib/README.md](../stage-2-stdlib/README.md)
