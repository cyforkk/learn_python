# 阶段 3 · 工程习惯

**目标**：会用 venv、写清依赖、会调试、会写少量测试、会基本 Git。  
**建议时间**：约 1 周（可与阶段 2 后期并行）。

## 学什么

虚拟环境、pip/包管理、PEP 8、类型注解入门、调试、pytest 入门、Git 基础。

## 阅读顺序（notes/）

1. [Python虚拟环境.md](notes/Python虚拟环境.md)
2. [Python包管理工具.md](notes/Python包管理工具.md)
3. [Python代码风格PEP8.md](notes/Python代码风格PEP8.md)
4. [Python类型注解入门.md](notes/Python类型注解入门.md)
5. [Python调试技巧.md](notes/Python调试技巧.md)
6. [Python测试入门.md](notes/Python测试入门.md)
7. [Git基础入门.md](notes/Git基础入门.md)

## 练习（exercises/）

| 文件 | 内容 |
|------|------|
| [ex01_venv_practice.md](exercises/ex01_venv_practice.md) | 创建 venv 与 requirements 实践 |
| [ex02_typed_functions.py](exercises/ex02_typed_functions.py) | 补全类型注解 |
| [ex03_pytest_stats/](exercises/ex03_pytest_stats/) | 为统计函数写 pytest |
| [ex04_debug_journal.md](exercises/ex04_debug_journal.md) | 调试一次并记入 bugs/ |

参考答案：[solutions/](solutions/)

## 验收标准

- 新环境能：`venv` → `pip install -r requirements.txt` → 跑通脚本
- 出 bug 时会读 Traceback、会设断点或 `breakpoint()`
- 至少写过 3 个 pytest 用例并通过

## 下一步

[../stage-4-tracks/README.md](../stage-4-tracks/README.md) 选方向，或直接看 [../stage-5-projects/README.md](../stage-5-projects/README.md)
