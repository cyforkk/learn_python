# 参考：调试记录应包含什么

示例结构：

```markdown
# 踩坑记录：KeyError 取字典键

- 日期：2026-04-01
- 阶段：stage-1
- 环境：Python 3.12 / Windows

## 现象
user["email"] 报 KeyError: 'email'

## 原因
字典里只有 name，没有 email

## 解决办法
改用 user.get("email", "N/A")

## 以后如何避免
访问可选字段统一用 get；或先校验 key in dict
```

Traceback 阅读顺序：先看最后一行异常类型 → 再看你自己文件的行号。
