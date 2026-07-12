# 踩坑记录：list/dict 大小写约定与 dict 视图必须 list() 实体化

- **日期**：2026-07-12  
- **阶段**：stage-1（复合类型 / 函数）及以后写题时通用  
- **环境**：Python 3.x  

## 现象

1. 题目/注释里写了 `List`、`Dict`，代码里却写 `List()`、`Dict()` → `NameError`，或类型注解风格混乱。  
2. 题目要求**返回列表**，却直接 `return d.keys()` / `return d.values()` → 类型不对（是 dict 视图，不是 `list`），判题或调用方会挂。

## 约定（本仓库写题统一遵守）

### 1. 内部建数据：用内置小写

```python
# 正确：运行时用内置类型
names = []
scores = {}
# 或
names = list()
scores = dict()
```

不要：

```python
names = List()   # 错：List 不是内置构造器（除非 from typing 且用法也不对）
scores = Dict()
```

### 2. 函数签名写在注释里：可用大写 List / Dict 表示「类型说明」

注释/文档里描述接口时可以用大写，方便和类型注解习惯对齐：

```python
# 入参 scores: Dict[str, int]
# 返回: List[str]  学生姓名列表
def top_names(scores):
    ...
```

若写真正的类型注解（中后期）：

```python
from typing import Dict, List   # 或 from collections.abc import ...

def top_names(scores: Dict[str, int]) -> List[str]:
    ...
```

新手作业**不必**写 `from typing import ...`，注释说明即可。

### 3. 要从字典的 keys/values 得到「真正的列表」：最外层必须 list()

`dict.keys()`、`dict.values()`、`dict.items()` 返回的是**视图（view）**，不是 `list`。

题目要求返回列表时：

```python
# 错误：返回的不是 list
return scores.keys()
return scores.values()

# 正确：最外层 list() 实体化
return list(scores.keys())
return list(scores.values())
return list(scores)          # 等价于 list(scores.keys())
```

组合场景同样：

```python
# 只要最终类型是 list，就在最外层转
return list(sorted(scores.keys()))
return list(filter(...))     # 若 filter 结果也要 list
```

## 原因

| 写法 | 实际类型 | 说明 |
|------|----------|------|
| `list` / `dict` | 内置类型 | 用来 `list()`、`{}` 构造 |
| `List` / `Dict`（typing） | 类型标注用 | 不能当 `List()` 构造数据 |
| `d.keys()` | `dict_keys` 视图 | 可遍历，但不是 `list` |

## 解决办法（检查清单）

写返回列表的函数时问自己：

1. [ ] 内部建容器是否用了小写 `list`/`dict`/`[]`/`{}`？  
2. [ ] 注释/签名若写类型，是否用了 `List`/`Dict` 且**没有**写成 `List()` 构造？  
3. [ ] 若数据来自 `.keys()` / `.values()` / `.items()`，返回前是否包了 `list(...)`？  

## 以后如何避免

- 作业与 solutions 统一按本约定  
- 判题或自检若要求 `isinstance(x, list)`，必须 `list()` 实体化  
- FAQ 见 [docs/faq-common-mistakes.md](../docs/faq-common-mistakes.md)  

## 相关笔记

- [Python复合类型.md](../stage-1-basics/notes/Python复合类型.md)  
- [Python函数.md](../stage-1-basics/notes/Python函数.md)  
