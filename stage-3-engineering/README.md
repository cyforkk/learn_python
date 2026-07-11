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

## 练习

清单：[exercises/README.md](exercises/README.md)（含 ex05 迷你工程样板）

```bash
cd stage-3-engineering/exercises/ex03_pytest_stats
pytest -q
cd ../ex05_mini_project
pytest -q
python -m greeter_app
```

## 进阶笔记（可选）

- [进阶-装饰器.md](notes/进阶-装饰器.md)  
- [进阶-生成器.md](notes/进阶-生成器.md)  
- [进阶-异步入门.md](notes/进阶-异步入门.md)  

## 验收标准

- venv + requirements 能复现环境  
- 会读 Traceback；`bugs/` 有记录  
- pytest 用例通过（ex03 / ex05）  

## 下一步

[../stage-4-tracks/README.md](../stage-4-tracks/README.md)
