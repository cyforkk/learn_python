# 常见问题与错题 FAQ

配合 `bugs/` 踩坑记录使用。遇到报错先看 **Traceback 最后一行**。

## 语法与类型

### 1. `IndentationError` / `TabError`

缩进必须一致，统一 **4 空格**，不要 Tab 混用。

### 2. `NameError: name 'xxx' is not defined`

变量/函数名拼错，或在定义前使用；注意大小写。

### 3. `TypeError: can only concatenate str (not "int") to str`

```python
# 错
age = 18
print("年龄" + age)
# 对
print("年龄" + str(age))
print(f"年龄{age}")
```

### 4. `True` / `False` 写成 `true`

Python 布尔首字母必须大写。

## 容器

### 5. `KeyError`

字典没有该键。用 `d.get("k", default)` 或先 `if k in d`。

### 6. `IndexError: list index out of range`

下标越界；先 `len(lst)` 或判断空列表。

### 7. 可变默认参数

```python
# 错
def f(a=[]):
    a.append(1)
    return a
# 对
def f(a=None):
    if a is None:
        a = []
    ...
```

### 7b. `list`/`dict` 与 `List`/`Dict`；`keys()` 必须 `list()` 实体化

**内部建数据用小写内置类型：**

```python
names = []       # 或 list()
scores = {}      # 或 dict()
# 不要: List() / Dict()  —— 那不是内置构造器
```

**注释/函数签名说明类型时可用大写（文档习惯）：**

```python
# 入参 scores: Dict[str, int]
# 返回: List[str]
```

**题目要求返回 list，且数据来自字典 keys/values 时，最外层必须 `list()`：**

```python
# 错：返回的是 dict_keys / dict_values 视图，不是 list
return scores.keys()
return scores.values()

# 对
return list(scores.keys())
return list(scores.values())
```

踩坑全文：[bugs/2026-07-12-list-dict大小写与list实体化.md](../bugs/2026-07-12-list-dict大小写与list实体化.md)

## 文件与编码

### 8. `FileNotFoundError`

路径不对或文件不存在；用 `Path.exists()` 检查；Windows 注意盘符与工作目录。

### 9. `UnicodeDecodeError`

读写时指定 `encoding="utf-8"`。

## 模块与环境

### 10. `ModuleNotFoundError`

- 没装包：`pip install xxx`（先激活 venv）  
- 跑错目录：`ex03_mini_package` 要在包目录内 `python main.py`  
- 文件名与标准库冲突（不要命名 `random.py`）

### 11. 装到系统 Python，项目里 import 不到

先 `Activate` 虚拟环境再 `pip install`。

## 逻辑类（自检失败）

### 12. `grade_level` 顺序写反

必须从高到低判断（先 `>=90` 再 `>=80`）。

### 13. 除法除零

`calculate` 中 `/` 要先判断 `b == 0`，返回 `None` 或友好提示。

### 14. 九九表行数不对

外层 `for i in range(1, 10)`，内层 `for j in range(1, i+1)`。

## 网络与第三方

### 15. `requests` 超时 / 连接错误

检查网络；设 `timeout=`；用 `try/except requests.RequestException`。

### 16. Flask / pandas 未安装

进入对应 `starter/` 执行 `pip install -r requirements.txt`。

## 调试口诀

1. 复现最小例子  
2. 读完整 Traceback  
3. 定位**自己的文件:行号**  
4. 改一处再跑  
5. 写入 `bugs/` 防止再踩  

更多路线问题见 [roadmap.md](roadmap.md)。
