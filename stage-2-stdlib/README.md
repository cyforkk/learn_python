# 阶段 2 · 标准库与代码结构

**目标**：会安全读写文件、处理异常、拆模块、用简单 class。  
**建议时间**：1～2 周。

## 学什么

文件读写、`try/except`、`import` 与包、pathlib/json/datetime 等、推导式、面向对象入门。

## 阅读顺序（notes/）

1. [Python文件读写.md](notes/Python文件读写.md)
2. [Python异常处理.md](notes/Python异常处理.md)
3. [Python模块与包.md](notes/Python模块与包.md)
4. [Python常用标准库.md](notes/Python常用标准库.md)
5. [Python推导式.md](notes/Python推导式.md)
6. [Python面向对象入门.md](notes/Python面向对象入门.md)

## 练习（exercises/）

| 文件 | 内容 |
|------|------|
| [ex01_todo_json.py](exercises/ex01_todo_json.py) | JSON 待办增查存 |
| [ex02_safe_read.py](exercises/ex02_safe_read.py) | 安全读文件 + 异常 |
| [ex03_mini_package/](exercises/ex03_mini_package/) | 多文件小模块 |
| [ex04_list_files.py](exercises/ex04_list_files.py) | pathlib 列目录 |
| [ex05_book_class.py](exercises/ex05_book_class.py) | 简单 Book 类 |

参考答案：[solutions/](solutions/)

## 验收标准

- 会用 `with open` / `pathlib` 读写，并指定 `encoding="utf-8"`
- 能处理文件不存在等常见异常
- 能把逻辑拆到 2～3 个 `.py` 文件并用 import 连接

## 下一步

[../stage-3-engineering/README.md](../stage-3-engineering/README.md)
