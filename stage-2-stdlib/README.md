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

## 练习

完整清单（含难度/时长/ex06 批量重命名）：[exercises/README.md](exercises/README.md)

```bash
cd stage-2-stdlib/exercises
python ex01_todo_json.py --check
python ex06_batch_rename.py --check
```

参考答案：[solutions/](solutions/)

## 验收标准

- 会用 `pathlib` + UTF-8 读写  
- 会处理文件不存在等异常  
- 能拆 2～3 个模块并用 import  
- ex01～ex06 `--check` 通过  

## 下一步

[../stage-3-engineering/README.md](../stage-3-engineering/README.md)
