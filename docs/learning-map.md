# 学习地图：先学文章 → 再练习 → 再项目

> **默认已有 Python**；主线从阶段 1 开始。  
> **不是每篇笔记都有练习**——见 [exercise-policy.md](exercise-policy.md)。

---

## 正确用法

```
❌ 每读完一篇就焦虑「练习在哪」
✅ 有「必做」才做题；标「无」的文章读懂即可往下

① 学 notes → ② 仅做标注的练习 → ③ 对照 solutions → ④ 项目
```

| 标记 | 含义 |
|------|------|
| **无** | 本篇不布置仓库练习 |
| **必做** | 建议完成，算阶段过关 |
| **选做** | 学有余力再做 |
| **建议** | 动手成本低，推荐做但不强求工程难度 |

新手练习说明：[stage-1 新手怎么做](../stage-1-basics/exercises/新手怎么做.md)  
练习 = **最简单脚本**（作业里无 assert）；自检若有只在 `exercises/checks/`。

---

## 阶段 0 · 环境附录（可选）

| 文档 | 练习 |
|------|------|
| [stage-0-setup](../stage-0-setup/README.md) 等 | **无**（装好 Python 即跳过） |

---

## 阶段 1 · 语法核心

**入口**：[stage-1-basics/README.md](../stage-1-basics/README.md)

| 顺序 | ① 笔记 | ② 练习安排 | 难度 |
|------|--------|------------|------|
| 1 | [基本数据类型](../stage-1-basics/notes/Python基本数据类型.md) | **无**（只了解） | ⭐ |
| 2 | [输入输出](../stage-1-basics/notes/Python输入输出.md) | **无**（并入猜数字） | ⭐ |
| 3 | [运算符与表达式](../stage-1-basics/notes/Python运算符与表达式.md) | **无** | ⭐ |
| 4 | [条件与循环](../stage-1-basics/notes/Python条件与循环.md) | **必做** [ex04 九九表](../stage-1-basics/exercises/ex04_multiplication_table.py)、[ex01 猜数字](../stage-1-basics/exercises/ex01_guess_number.py) | ⭐⭐ |
| 5 | [复合类型](../stage-1-basics/notes/Python复合类型.md) | **必做** [ex03 成绩](../stage-1-basics/exercises/ex03_score_stats.py)；**选做** [ex06 通讯录](../stage-1-basics/exercises/ex06_contacts.py) | ⭐⭐ |
| 6 | [字符串方法与格式化](../stage-1-basics/notes/Python字符串方法与格式化.md) | **无** | ⭐ |
| 7 | [函数](../stage-1-basics/notes/Python函数.md) | **必做** [ex05 函数重构](../stage-1-basics/exercises/ex05_refactor_functions.py)；**选做** [ex02 计算器](../stage-1-basics/exercises/ex02_calculator.py) | ⭐⭐ |
| 8 | [作用域](../stage-1-basics/notes/Python作用域.md) | **无** | ⭐ |

**阶段 1 过关（新手）**：笔记读完 + 必做 **ex04、ex01、ex03、ex05**。

- [新手怎么做](../stage-1-basics/exercises/新手怎么做.md) · [练习清单](../stage-1-basics/exercises/README.md) · [答案](../stage-1-basics/solutions/)

---

## 阶段 2 · 标准库

**入口**：[stage-2-stdlib/README.md](../stage-2-stdlib/README.md)

| 顺序 | ① 笔记 | ② 练习安排 | 难度 |
|------|--------|------------|------|
| 1 | [文件读写](../stage-2-stdlib/notes/Python文件读写.md) | 先读，题与异常篇合并 | ⭐⭐ |
| 2 | [异常处理](../stage-2-stdlib/notes/Python异常处理.md) | **必做** [ex02 安全读](../stage-2-stdlib/exercises/ex02_safe_read.py)（两篇都读完再做） | ⭐⭐ |
| 3 | [模块与包](../stage-2-stdlib/notes/Python模块与包.md) | **必做** [ex03 小模块](../stage-2-stdlib/exercises/ex03_mini_package/) | ⭐⭐ |
| 4 | [常用标准库](../stage-2-stdlib/notes/Python常用标准库.md) | **选做** [ex04 列目录](../stage-2-stdlib/exercises/ex04_list_files.py) | ⭐ |
| 5 | [推导式](../stage-2-stdlib/notes/Python推导式.md) | **无** | ⭐ |
| 6 | [面向对象入门](../stage-2-stdlib/notes/Python面向对象入门.md) | **必做** [ex05 Book 类](../stage-2-stdlib/exercises/ex05_book_class.py) | ⭐⭐ |
| — | （综合选做） | [ex01 JSON 待办](../stage-2-stdlib/exercises/ex01_todo_json.py)、[ex06 批量重命名](../stage-2-stdlib/exercises/ex06_batch_rename.py) | ⭐⭐ |

**阶段 2 过关（新手）**：**ex02、ex03、ex05**。

---

## 阶段 3 · 工程习惯

**入口**：[stage-3-engineering/README.md](../stage-3-engineering/README.md)  
语法新手不必赶进度。

| 顺序 | ① 笔记 | ② 练习安排 | 难度 |
|------|--------|------------|------|
| 1 | [虚拟环境](../stage-3-engineering/notes/Python虚拟环境.md) | **建议** [ex01](../stage-3-engineering/exercises/ex01_venv_practice.md) | ⭐ |
| 2 | [包管理工具](../stage-3-engineering/notes/Python包管理工具.md) | **无**新题（跟 ex01） | ⭐ |
| 3 | [PEP8](../stage-3-engineering/notes/Python代码风格PEP8.md) | **无** | ⭐ |
| 4 | [类型注解](../stage-3-engineering/notes/Python类型注解入门.md) | **选做** [ex02](../stage-3-engineering/exercises/ex02_typed_functions.py) | ⭐ |
| 5 | [调试技巧](../stage-3-engineering/notes/Python调试技巧.md) | **建议** [ex04 调试日记](../stage-3-engineering/exercises/ex04_debug_journal.md) | ⭐⭐ |
| 6 | [测试入门](../stage-3-engineering/notes/Python测试入门.md) | **选做** pytest（可整段跳过） | ⭐⭐ |
| 7 | [Git 基础](../stage-3-engineering/notes/Git基础入门.md) | **无**强制题 | ⭐ |
| 选学 | [装饰器](../stage-3-engineering/notes/进阶-装饰器.md) 等 | **无**仓库题 | ⭐⭐⭐ |

---

## 阶段 4 · 方向

先读路线文章，再 starter/demo（不是「每篇外部文档都交作业」）。

| 方向 | ① 路线文章 | ② 动手 |
|------|------------|--------|
| 自动化 | [path-automation.md](stage4-paths/path-automation.md) | [starter](../stage-4-tracks/automation/starter/) · [demo](../stage-4-tracks/automation/demo/) |
| 数据 | [path-data.md](stage4-paths/path-data.md) | [starter](../stage-4-tracks/data/starter/) · [demo](../stage-4-tracks/data/demo/) |
| Web | [path-web.md](stage4-paths/path-web.md) | [starter](../stage-4-tracks/web/starter/) · [demo](../stage-4-tracks/web/demo/) |
| AI | [path-ai.md](stage4-paths/path-ai.md) | [starter](../stage-4-tracks/ai/starter/) · [demo](../stage-4-tracks/ai/demo/) |

[GitHub 清单](stage4-github-projects.md) · [方向索引](stage4-paths/README.md)

---

## 阶段 5 · 项目

先读笔记/规格，再实现（三选一即可，不必全做）。

| ① 笔记 | ② 规格 | ③ 实现 |
|--------|--------|--------|
| [实战练习](../stage-5-projects/notes/Python实战练习.md) | [规格 01](../stage-5-projects/exercises/project_spec_01_todo_cli.md) | [todo-cli](../projects/todo-cli/) |
| [综合实战](../stage-5-projects/notes/Python综合实战.md) | [规格 02](../stage-5-projects/exercises/project_spec_02_file_organizer.md) / [03](../stage-5-projects/exercises/project_spec_03_api_cli.md) | [file-organizer](../projects/file-organizer/) · [api-cli](../projects/api-cli/) |

---

## 其它

| 文档 | 链接 |
|------|------|
| 练习原则（本文依据） | [exercise-policy.md](exercise-policy.md) |
| 总路线 | [roadmap.md](roadmap.md) |
| FAQ | [faq-common-mistakes.md](faq-common-mistakes.md) |
| 进度 | [progress.md](../progress.md) |
