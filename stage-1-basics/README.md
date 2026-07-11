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
| 4 | [条件与循环](notes/Python条件与循环.md) | **必做** ex04、ex01 |
| 5 | [复合类型](notes/Python复合类型.md) | **必做** ex03；选做 ex06 |
| 6 | [字符串方法与格式化](notes/Python字符串方法与格式化.md) | **无** |
| 7 | [函数](notes/Python函数.md) | **必做** ex05；选做 ex02 |
| 8 | [作用域](notes/Python作用域.md) | **无** |

原则：[docs/exercise-policy.md](../docs/exercise-policy.md)  
第一天：读 1～4 → 只做 **ex04 九九表**。

## ② 练习（notes 读完对应篇后再做）

**新手必读**：[exercises/新手怎么做.md](exercises/新手怎么做.md)

- 清单：[exercises/README.md](exercises/README.md)  
- **先保证** `python ex0x_xxx.py` 能玩/能打印对  
- `--check`、文件里的 `_selfcheck` / `assert`：**可选**，入门可整段忽略  

```bash
cd stage-1-basics/exercises
python ex04_multiplication_table.py   # 建议第一题
python ex01_guess_number.py           # 交互游戏
```

## ③ 答案（做完再看）

[solutions/](solutions/)  
答案写得更「工程」一些（多函数、自检），你的第一版可以更简单。

## 验收标准（新手版）

- 笔记要点能口述  
- **必做 4 题**：ex04 九九表、ex01 猜数字、ex03 成绩、ex05 函数重构  
- **选做**：ex02 计算器、ex06 通讯录  
- **不要求** 每篇笔记都做题；不要求 pytest / `--check`  

## 下一步

[../stage-2-stdlib/README.md](../stage-2-stdlib/README.md)
