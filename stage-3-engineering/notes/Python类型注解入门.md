# Python 类型注解入门：让代码意图更清晰

## 为什么需要类型注解

Python 是动态类型语言，变量不需要声明类型，解释器自动推断。这写起来很爽，但**读代码时不知道参数该传什么类型、函数返回什么类型**。类型注解就是给变量、参数、返回值加上类型标记，让代码意图更明确，同时让 IDE 能更好地提示和检查。

**类型注解不强制执行**——写错了类型程序照常运行。它的价值在于**可读性和工具支持**，而不是运行时约束。

## 基本语法

### 函数参数和返回值

**语法格式：**

```python
def 函数名(参数: 类型) -> 返回类型:
    函数体
```

```python
def greet(name: str) -> str:
    return f"hello, {name}"
```

`name: str` 表示参数 `name` 应该是字符串，`-> str` 表示函数返回字符串。

### 变量注解

**语法格式：**

```python
变量名: 类型 = 值
```

```python
name: str = "张三"
age: int = 25
score: float = 85.5
is_active: bool = True
```

变量名后加冒号和类型，再赋值。

## 基本类型

### 常用类型

```python
# 基本类型
name: str = "张三"
age: int = 25
score: float = 85.5
is_admin: bool = True
nothing: None = None

# 函数参数和返回值
def add(a: int, b: int) -> int:
    return a + b

def format_price(price: float) -> str:
    return f"¥{price:.2f}"

def is_adult(age: int) -> bool:
    return age >= 18
```

### 容器类型

Python 3.9+ 可以直接用 `list`、`dict`、`set`、`tuple` 加方括号标注元素类型：

**语法格式：**

```python
变量名: list[元素类型] = 值
变量名: dict[键类型, 值类型] = 值
变量名: tuple[类型1, 类型2] = 值
变量名: set[元素类型] = 值
```

```python
# 列表
names: list[str] = ["张三", "李四"]
scores: list[int] = [85, 92, 78]

# 字典
person: dict[str, str] = {"name": "张三", "city": "北京"}
config: dict[str, int] = {"port": 8080, "timeout": 30}

# 元组
point: tuple[int, int] = (3, 5)

# 集合
tags: set[str] = {"python", "django"}
```

Python 3.8 及更早版本需要从 `typing` 模块导入：

```python
from typing import List, Dict, Tuple, Set

names: List[str] = ["张三", "李四"]
person: Dict[str, str] = {"name": "张三"}
point: Tuple[int, int] = (3, 5)
```

**新项目用 Python 3.9+ 直接写 `list[str]`，老项目用 `List[str]`。**

### Optional — 可选类型

参数可能是某种类型，也可能是 `None`：

**语法格式：**

```python
# 写法一：Optional
变量名: Optional[类型] = None

# 写法二：类型 | None（Python 3.10+）
变量名: 类型 | None = None
```

```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "hello, stranger"
    return f"hello, {name}"

greet()          # "hello, stranger"
greet("张三")    # "hello, 张三"
```

`Optional[str]` 等价于 `str | None`（Python 3.10+ 可以直接写 `str | None`）：

```python
# Python 3.10+
def greet(name: str | None = None) -> str:
    if name is None:
        return "hello, stranger"
    return f"hello, {name}"
```

### Union — 多种类型

参数可能是多种类型之一：

**语法格式：**

```python
# 写法一：Union
变量名: Union[类型1, 类型2] = 值

# 写法二：类型1 | 类型2（Python 3.10+）
变量名: 类型1 | 类型2 = 值
```

```python
from typing import Union

def process(data: Union[str, int]) -> str:
    if isinstance(data, str):
        return data.upper()
    return str(data)

# Python 3.10+ 用 | 更简洁
def process(data: str | int) -> str:
    if isinstance(data, str):
        return data.upper()
    return str(data)
```

### Any — 任意类型

不确定类型时用 `Any`，等于不限制：

```python
from typing import Any

def print_anything(data: Any) -> None:
    print(data)
```

**尽量少用 `Any`**，用多了等于没加类型注解。

## 容器类型的详细标注

### 列表

```python
# 字符串列表
names: list[str] = ["张三", "李四"]

# 整数列表
scores: list[int] = [85, 92, 78]

# 字典列表
users: list[dict[str, str]] = [
    {"name": "张三", "city": "北京"},
    {"name": "李四", "city": "上海"},
]
```

### 字典

```python
# 键和值都标注类型
person: dict[str, str] = {"name": "张三", "city": "北京"}

# 键是字符串，值可以是字符串或整数
config: dict[str, str | int] = {"host": "localhost", "port": 8080}
```

### 元组

```python
# 固定长度和类型
point: tuple[int, int] = (3, 5)

# 混合类型
record: tuple[str, int, bool] = ("张三", 25, True)

# 变长元组（同类型）
nums: tuple[int, ...] = (1, 2, 3, 4, 5)
```

## 函数签名示例

### 简单函数

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, greeting: str = "hello") -> str:
    return f"{greeting}, {name}"
```

### 带容器参数

```python
def average(scores: list[float]) -> float:
    return sum(scores) / len(scores)

def find_student(students: dict[str, int], name: str) -> int | None:
    return students.get(name)
```

### 多种返回类型

```python
from typing import Optional

def parse_int(s: str) -> Optional[int]:
    try:
        return int(s)
    except ValueError:
        return None
```

## 类的属性注解

```python
class Student:
    # 类级别注解（不赋值，只标注类型）
    name: str
    age: int
    score: float

    def __init__(self, name: str, age: int, score: float = 0.0) -> None:
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self) -> str:
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        return "C"
```

`__init__` 的返回值类型是 `None`，因为初始化方法不返回值。

## 类型注解不强制执行

**写了类型注解，传错类型程序照样能跑。** 类型注解只是给人和工具看的：

```python
def add(a: int, b: int) -> int:
    return a + b

# 传字符串也不会报错
result = add("hello", "world")   # "helloworld"
print(result)   # helloworld
```

Python 运行时不检查类型。要检查类型需要用工具：

**mypy** — 静态类型检查工具：

```bash
pip install mypy
mypy my_code.py
```

mypy 会扫描代码，报告类型不匹配的地方：

```
my_code.py:5: error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

**实际开发中用 mypy 检查类型，但不强制在运行时报错。**

## 类型注解的价值

### 提升可读性

```python
# 没有注解：参数和返回值类型全靠猜
def process(data, options):
    result = []
    for item in data:
        if item in options:
            result.append(item)
    return result

# 有注解：一目了然
def process(data: list[str], options: set[str]) -> list[str]:
    result = []
    for item in data:
        if item in options:
            result.append(item)
    return result
```

### IDE 智能提示

VS Code、PyCharm 等编辑器会根据类型注解提供自动补全：

```python
def greet(name: str) -> str:
    return f"hello, {name}"

# 写 name. 时 IDE 会提示 str 的方法
greet("张三").upper()   # IDE 知道返回 str，提示 .upper()
```

### 提前发现问题

```python
def calculate_bmi(height: float, weight: float) -> float:
    return weight / (height ** 2)

# mypy 检查时会报错：传了 str，期望 float
calculate_bmi("1.75", 70)   # TypeError 提示
```

## Callable — 函数类型

函数作为参数时，用 `Callable` 标注：

**语法格式：**

```python
变量名: Callable[[参数类型], 返回类型] = 值
```

```python
from typing import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def double(x: int) -> int:
    return x * 2

def square(x: int) -> int:
    return x ** 2

print(apply(double, 5))   # 10
print(apply(square, 5))   # 25
```

`Callable[[int], int]` 表示：接收一个 `int` 参数，返回 `int` 的函数。

Python 3.10+ 也可以用 `collections.abc.Callable`。

## 实际使用建议

### 渐进式添加

不需要一次给所有代码加注解。**从新代码开始，老代码需要时再加**：

```python
# 新写的函数加注解
def get_user(user_id: int) -> dict[str, str]:
    return {"name": "张三", "email": "test@test.com"}

# 老代码暂时不加也行
def old_function(data):
    return data
```

### 简单函数可以不加

逻辑很简单的函数不注解也能一眼看懂：

```python
# 不注解也清晰
def is_even(n):
    return n % 2 == 0

# 注解后更规范
def is_even(n: int) -> bool:
    return n % 2 == 0
```

### 公开 API 优先注解

**对外暴露的函数（模块级函数、类的公开方法）优先加注解**，内部辅助函数可以不加。

## 类型别名

类型太长可以取别名：

```python
from typing import Dict, List

# 类型别名
JSON = Dict[str, "str | int | float | bool | None"
StudentScores = Dict[str, int]

def parse_config(data: JSON) -> StudentScores:
    pass
```

Python 3.12+ 可以用 `type` 关键字：

```python
type JSON = dict[str, str | int | float | bool | None]
```

## 速查表

| 注解 | 含义 | 示例 |
|---|---|---|
| `x: int` | 整数 | `age: int = 25` |
| `x: str` | 字符串 | `name: str = "张三"` |
| `x: float` | 浮点数 | `price: float = 9.99` |
| `x: bool` | 布尔值 | `is_admin: bool = True` |
| `-> int` | 返回整数 | `def f() -> int:` |
| `-> None` | 无返回值 | `def f() -> None:` |
| `list[str]` | 字符串列表 | `names: list[str]` |
| `dict[str, int]` | 键值类型 | `config: dict[str, int]` |
| `str \| None` | 可选 | `name: str \| None` |
| `str \| int` | 多类型 | `data: str \| int` |
| `Any` | 任意类型 | `data: Any` |
| `Callable` | 函数类型 | `func: Callable[[int], int]` |

## 要点

类型注解的核心就两件事：**给参数标类型、给返回值标类型**。变量加 `: 类型`，函数返回值加 `-> 类型`。容器类型用 `list[str]`、`dict[str, int]` 标注元素类型。可选值用 `str | None`，多类型用 `str | int`。类型注解不强制执行，但配合 mypy 可以静态检查。**不必一开始就给所有代码加注解**，从新函数开始，公开 API 优先，简单函数可以不加。先认识、能看懂别人的注解就行，熟练了再给自己的代码加。

---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python代码风格PEP8.md](Python代码风格PEP8.md) |
| **下一篇** | [Python调试技巧.md](Python调试技巧.md) |
| **本篇练习** | **加练（可选）**，可整题跳过 |

### 加练 · 类型注解

**题目：** 给若干函数补参数/返回值注解，行为不变。

- 作业（空白）：[exercises/ex02_typed_functions.py](../exercises/ex02_typed_functions.py)
