# 阶段 3 练习清单

> 阶段 3 偏「工程习惯」，**语法新手不必急着做完**。  
> 建议 stage-1～2 主力练习都跑通过后，再慢慢来。

## 新手可先做（简单）

| 顺序 | 文件 | 主题 | 说明 |
|------|------|------|------|
| ① | [ex04_debug_journal.md](ex04_debug_journal.md) | 调试日记 | 写一篇踩坑记录即可，几乎不写代码 |
| ② | [ex01_venv_practice.md](ex01_venv_practice.md) | 虚拟环境 | 跟着命令做，按清单勾选 |
| ③ | [ex02_typed_functions.py](ex02_typed_functions.py) | 类型注解 | **可整题跳过**；注解不熟没关系 |

## 明显更难 · 后做 / 选做

| 文件 | 主题 | 说明 |
|------|------|------|
| [ex03_pytest_stats/](ex03_pytest_stats/) | **pytest 测试** | 名字吓人：是「自动验算」工具，**不是 stage-1 内容**。等你愿意再学 |
| [ex05_mini_project/](ex05_mini_project/) | 迷你工程 | 多文件 + 测试，综合题，选做 |

### 关于 pytest（给好奇的人）

- 作用：自动检查函数算得对不对  
- **不会 pytest 也能学好 Python**  
- 想了解时：先读 [../notes/Python测试入门.md](../notes/Python测试入门.md)，再进 ex03  
- 不会写测试时：可以只实现 `stats.py` 里的函数，用 `print` 自己验

```bash
# 仅在你学测试时再运行
cd ex03_pytest_stats
pytest -q
```

进阶阅读（非必须）：[../notes/进阶-装饰器.md](../notes/进阶-装饰器.md) 等。
