# 学习地图：先学文章 → 再练习 → 再项目

> 难度：⭐ 入门 · ⭐⭐ 巩固 · ⭐⭐⭐ 综合  
> **默认已有 Python**；主线从阶段 1 开始。  
> 表中链接可点：先点左侧 **笔记**，学完再点右侧 **练习**。

---

## 正确用法（不要反了）

```
❌ 错误：一打开仓库就刷 exercises / --check
✅ 正确：notes 文章读懂（能复述要点）→ 再 exercises → 最后 projects
```

| 步骤 | 做什么 | 打开哪里 |
|------|--------|----------|
| 1 学 | 读笔记，跑文中小例子 | 下表「笔记」列 |
| 2 练 | 独立做题，**先保证能运行、行为对** | 下表「练习」列 |
| 3 对 | 对照答案，记踩坑 | 同阶段 `solutions/` |
| 4 项 | 综合项目 / 方向作品 | 阶段 4～5、`projects/` |

新手练习说明：[stage-1 新手怎么做](../stage-1-basics/exercises/新手怎么做.md)  
`--check` / `assert` / pytest：**选做**，不是入门门槛。

每一行建议：**当天先只读笔记**；同一主题练不完可以第二天再练。

---

## 阶段 0 · 环境附录（可选 · 默认可跳过）

| 文档 | 说明 |
|------|------|
| [stage-0-setup/README.md](../stage-0-setup/README.md) | 附录入口 |
| [安装与编辑器.md](../stage-0-setup/notes/安装与编辑器.md) | 装不上再看 |
| [编码与控制台.md](../stage-0-setup/notes/编码与控制台.md) | 乱码 / 路径 |
| [windows-setup.md](windows-setup.md) | Windows 细节 |

---

## 阶段 1 · 语法核心（主线起点）

**本阶段入口（先读说明再读笔记）**：[stage-1-basics/README.md](../stage-1-basics/README.md)

推荐阅读顺序 = 下表从上到下。**读完一篇再做右侧对应练习**（不必一天刷完所有题）。

| 顺序 | ① 先学笔记（文章） | ② 再做练习（能跑就行） | 难度 |
|------|-------------------|------------------------|------|
| 1 | [Python基本数据类型](../stage-1-basics/notes/Python基本数据类型.md) | 先只读，稍后成绩题再用 | ⭐ |
| 2 | [Python输入输出](../stage-1-basics/notes/Python输入输出.md) | 为猜数字做准备 | ⭐ |
| 3 | [Python运算符与表达式](../stage-1-basics/notes/Python运算符与表达式.md) | 稍后计算器（学完函数再做） | ⭐ |
| 4 | [Python条件与循环](../stage-1-basics/notes/Python条件与循环.md) | **优先** [ex04 九九表](../stage-1-basics/exercises/ex04_multiplication_table.py)、[ex01 猜数字](../stage-1-basics/exercises/ex01_guess_number.py) | ⭐⭐ |
| 5 | [Python复合类型](../stage-1-basics/notes/Python复合类型.md) | [ex03 成绩统计](../stage-1-basics/exercises/ex03_score_stats.py) | ⭐⭐ |
| 6 | [Python字符串方法与格式化](../stage-1-basics/notes/Python字符串方法与格式化.md) | 巩固上面的题 | ⭐ |
| 7 | [Python函数](../stage-1-basics/notes/Python函数.md) | 再做 [ex02](../stage-1-basics/exercises/ex02_calculator.py)、[ex05](../stage-1-basics/exercises/ex05_refactor_functions.py) | ⭐⭐ |
| 8 | [Python作用域](../stage-1-basics/notes/Python作用域.md) | 复习函数题 | ⭐ |

- **新手怎么做**：[新手怎么做.md](../stage-1-basics/exercises/新手怎么做.md)  
- 练习总表：[exercises/README.md](../stage-1-basics/exercises/README.md)  
- 答案（**做完再看**）：[solutions/](../stage-1-basics/solutions/)

---

## 阶段 2 · 标准库

**入口**：[stage-2-stdlib/README.md](../stage-2-stdlib/README.md) → 先按阅读顺序读 `notes/`。

| 顺序 | ① 先学笔记 | ② 再做练习 | 难度 |
|------|------------|------------|------|
| 1 | [Python文件读写](../stage-2-stdlib/notes/Python文件读写.md) | [ex01 待办 JSON](../stage-2-stdlib/exercises/ex01_todo_json.py)、[ex02 安全读](../stage-2-stdlib/exercises/ex02_safe_read.py) | ⭐⭐ |
| 2 | [Python异常处理](../stage-2-stdlib/notes/Python异常处理.md) | [ex02 安全读](../stage-2-stdlib/exercises/ex02_safe_read.py) | ⭐⭐ |
| 3 | [Python模块与包](../stage-2-stdlib/notes/Python模块与包.md) | [ex03 小模块](../stage-2-stdlib/exercises/ex03_mini_package/) | ⭐⭐ |
| 4 | [Python常用标准库](../stage-2-stdlib/notes/Python常用标准库.md) | [ex04 列目录](../stage-2-stdlib/exercises/ex04_list_files.py)、[ex06 批量重命名](../stage-2-stdlib/exercises/ex06_batch_rename.py) | ⭐⭐ |
| 5 | [Python推导式](../stage-2-stdlib/notes/Python推导式.md) | 巩固 ex04 / ex06 | ⭐ |
| 6 | [Python面向对象入门](../stage-2-stdlib/notes/Python面向对象入门.md) | [ex05 Book 类](../stage-2-stdlib/exercises/ex05_book_class.py) | ⭐⭐ |

- 练习总表：[exercises/README.md](../stage-2-stdlib/exercises/README.md)  
- 答案：[solutions/](../stage-2-stdlib/solutions/)

---

## 阶段 3 · 工程习惯

**入口**：[stage-3-engineering/README.md](../stage-3-engineering/README.md) → 先读笔记再做工程向练习。

| 顺序 | ① 先学笔记 | ② 再做练习 | 难度 |
|------|------------|------------|------|
| 1 | [Python虚拟环境](../stage-3-engineering/notes/Python虚拟环境.md) | [ex01 venv 实践](../stage-3-engineering/exercises/ex01_venv_practice.md) | ⭐ |
| 2 | [Python包管理工具](../stage-3-engineering/notes/Python包管理工具.md) | [ex01](../stage-3-engineering/exercises/ex01_venv_practice.md)、[ex05 迷你工程](../stage-3-engineering/exercises/ex05_mini_project/) | ⭐ |
| 3 | [Python代码风格PEP8](../stage-3-engineering/notes/Python代码风格PEP8.md) | 对照自己代码 · [FAQ](faq-common-mistakes.md) | ⭐ |
| 4 | [Python类型注解入门](../stage-3-engineering/notes/Python类型注解入门.md) | [ex02 类型注解](../stage-3-engineering/exercises/ex02_typed_functions.py) | ⭐ |
| 5 | [Python调试技巧](../stage-3-engineering/notes/Python调试技巧.md) | [ex04 调试日记](../stage-3-engineering/exercises/ex04_debug_journal.md) | ⭐⭐ |
| 6 | [Python测试入门](../stage-3-engineering/notes/Python测试入门.md) | [ex03 pytest](../stage-3-engineering/exercises/ex03_pytest_stats/) | ⭐⭐ |
| 7 | [Git基础入门](../stage-3-engineering/notes/Git基础入门.md) | 本地 commit | ⭐ |
| 选学 | [进阶-装饰器](../stage-3-engineering/notes/进阶-装饰器.md) · [生成器](../stage-3-engineering/notes/进阶-生成器.md) · [异步](../stage-3-engineering/notes/进阶-异步入门.md) | 读懂再写小例子 | ⭐⭐⭐ |

- 练习总表：[exercises/README.md](../stage-3-engineering/exercises/README.md)

---

## 阶段 4 · 方向（先读路线文章，再动手）

**入口**：[stage-4-tracks/README.md](../stage-4-tracks/README.md)

```
① 读该方向 path-*.md（学什么、资源、周计划）
② 再跑 starter / demo
③ 再按 GitHub 清单读码、做自己的 projects/
```

| 方向 | ① 先学：路线文章 | ② 再练：代码入口 | 说明页 |
|------|------------------|------------------|--------|
| 自动化 | [path-automation.md](stage4-paths/path-automation.md) | [starter](../stage-4-tracks/automation/starter/) · [demo](../stage-4-tracks/automation/demo/) | [automation/README](../stage-4-tracks/automation/README.md) |
| 数据 | [path-data.md](stage4-paths/path-data.md) | [starter](../stage-4-tracks/data/starter/) · [demo](../stage-4-tracks/data/demo/) | [data/README](../stage-4-tracks/data/README.md) |
| Web | [path-web.md](stage4-paths/path-web.md) | [starter](../stage-4-tracks/web/starter/) · [demo](../stage-4-tracks/web/demo/) | [web/README](../stage-4-tracks/web/README.md) |
| AI | [path-ai.md](stage4-paths/path-ai.md) | [starter](../stage-4-tracks/ai/starter/) · [demo](../stage-4-tracks/ai/demo/) | [ai/README](../stage-4-tracks/ai/README.md) |

- 方向索引：[stage4-paths/README.md](stage4-paths/README.md)  
- GitHub 清单（学完路线再打开）：[stage4-github-projects.md](stage4-github-projects.md)

---

## 阶段 5 · 项目（先读笔记/规格，再写项目）

**入口**：[stage-5-projects/README.md](../stage-5-projects/README.md)

```
① 读实战笔记，建立「项目长什么样」的概念
② 读 project_spec_*.md 规格
③ 在 projects/ 自己实现（可对照已有实现，但先按规格做）
```

| ① 先学笔记 | ② 再读规格 | ③ 再实现 |
|------------|------------|----------|
| [Python实战练习](../stage-5-projects/notes/Python实战练习.md) | [规格 01 待办](../stage-5-projects/exercises/project_spec_01_todo_cli.md) | [projects/todo-cli](../projects/todo-cli/) |
| [Python综合实战](../stage-5-projects/notes/Python综合实战.md) | [规格 02 文件整理](../stage-5-projects/exercises/project_spec_02_file_organizer.md) | [projects/file-organizer](../projects/file-organizer/) |
| （同上） | [规格 03 API CLI](../stage-5-projects/exercises/project_spec_03_api_cli.md) | [projects/api-cli](../projects/api-cli/) |

---

## 其它文档

| 文档 | 链接 |
|------|------|
| 总路线 | [roadmap.md](roadmap.md) |
| FAQ | [faq-common-mistakes.md](faq-common-mistakes.md) |
| 仓库首页 | [README.md](../README.md) |
| 进度 | [progress.md](../progress.md) |

## 自学节奏（再次强调）

1. **只点笔记链接**，读完能用自己的话讲 3 个要点  
2. **再点练习链接** 动手，`python xxx.py --check`  
3. 对照 `solutions/`，坑记到 [bugs/](../bugs/)  
4. [progress.md](../progress.md) 先勾「笔记已读」，再勾「练习已完成」  
