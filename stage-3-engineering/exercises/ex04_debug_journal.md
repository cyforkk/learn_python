# 练习 04：调试一次真实报错

## 目标

刻意制造或遇到一次报错，走完「复现 → 读 Traceback → 修复 → 记录」。

## 步骤

1. 写一个会报错的小脚本（例如字典取不存在的键、int("abc")、除以 0）
2. 运行，复制 **完整 Traceback**
3. 用下面任一方式定位：
   - 读最后一行异常类型
   - VS Code 断点
   - 代码中插入 `breakpoint()`
4. 修复后确认能跑通
5. 复制 [../../bugs/_template.md](../../bugs/_template.md) 到 `bugs/` 下写成一篇真实记录

## 验收

- [x] `bugs/` 下有一篇非模板的踩坑记录 → [../../bugs/2026-07-11-KeyError演示.md](../../bugs/2026-07-11-KeyError演示.md)
- [x] 记录中包含现象、原因、解决办法

参考：`solutions/ex04_debug_journal.md`
