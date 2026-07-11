# Python 代码风格：PEP 8 核心约定

## 为什么需要代码风格

代码写出来是给人看的，顺便给机器执行。如果每个人的命名方式、缩进习惯、空行规则都不一样，读别人的代码就特别费劲。**PEP 8 是 Python 官方的代码风格指南**，规定了命名、缩进、空行等约定。遵循 PEP 8 的代码风格统一，团队协作时不需要争论"用 tab 还是空格"。

不需要背下整份 PEP 8 文档。**掌握命名、缩进、空行这三项约定，日常代码就能写得规范整洁。**

## 命名约定

### 总览

| 类型 | 命名风格 | 示例 |
|---|---|---|
| 变量、函数 | 全小写，单词间用下划线 | `student_name`、`get_score()` |
| 类名 | 大驼峰，每个单词首字母大写 | `StudentInfo`、`BankAccount` |
| 常量 | 全大写，单词间用下划线 | `MAX_RETRIES`、`DEFAULT_PORT` |
| 模块名 | 全小写，简短 | `utils`、`data_processor` |
| 私有成员 | 前面加一个下划线 | `_internal_method()` |

### 变量和函数名

用**小写字母加下划线**，单词间用下划线分隔：

通用格式：

```python
variable_name = value
def function_name():
    ...
```

具体示例：

```python
# 推荐
student_name = "张三"
total_score = 0
def get_user_info():
    pass

# 不推荐
studentName = "张三"   # 驼峰命名，不符合 Python 风格
TOTAL_SCORE = 0       # 全大写看起来像常量
def getuserinfo():     # 没有下划线，难读
    pass
```

### 类名

用**大驼峰**（每个单词首字母大写，不用下划线）：

通用格式：

```python
class ClassName:
    ...
```

具体示例：

```python
# 推荐
class Student:
    pass

class BankAccount:
    pass

class CSVDataProcessor:
    pass

# 不推荐
class student:        # 首字母没大写
    pass

class bank_account:   # 用了下划线，不符合类名风格
    pass
```

### 常量

用**全大写加下划线**，表示不应该被修改的值：

通用格式：

```python
CONSTANT_NAME = value
```

具体示例：

```python
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159265358979
DATABASE_URL = "localhost:5432"
```

常量通常放在模块顶部，函数外部。

### 私有成员

前面加**一个下划线**表示"这是内部使用的，外部别碰"：

```python
class Student:
    def __init__(self, name):
        self.name = name        # 公开属性
        self._id = generate_id()  # 私有属性，约定不外部访问

    def study(self):
        self._review_notes()   # 内部方法

    def _review_notes(self):    # 私有方法
        pass
```

**Python 没有真正的私有**，`_` 只是约定。但社区都遵守这个约定，看到 `_` 开头的就知道不该外部调用。

两个下划线 `__` 开头会触发名称修饰，一般不需要用，一个 `_` 就够了。

### 命名要有意义

```python
# 推荐：名字说明用途
def calculate_average(scores):
    pass

student_count = 30
is_valid = True

# 不推荐：名字无意义
def func(x):
    pass

n = 30           # n 是什么？
flag = True      # flag 表示什么？

# 例外：循环变量和数学计算
for i in range(10):
    pass

x, y = 10, 20    # 数学场景
```

**名字长一点没关系，可读性最重要。** `student_count` 比 `n` 好，`is_valid` 比 `flag` 好。

### 布尔变量用 is / has 开头

```python
# 推荐
is_active = True
is_admin = False
has_permission = True
can_edit = False

# 不推荐
active = True     # 不知道是"是否活跃"还是"活跃状态"
admin = False     # 看不出是布尔值
```

`is_` 和 `has_` 前缀让布尔变量一目了然。

## 缩进

### 用 4 个空格

每一层缩进使用 **4 个空格**，不要用 tab：

```python
# 推荐
def greet(name):
    print(f"hello, {name}")

# 不推荐
def greet(name):
  print(f"hello, {name}")    # 2 个空格
```

**4 个空格是 Python 社区的标准**，编辑器默认就是这个。不要用 tab。

### 续行缩进

一行写不下时，换行后用括号对齐或 4 个空格缩进：

```python
# 方括号对齐
result = some_function(
    arg1, arg2, arg3,
    arg4, arg5
)

# 换行后缩进
total = first_variable + second_variable + \
    third_variable + fourth_variable

# 推荐用括号包裹（隐式续行）
total = (
    first_variable
    + second_variable
    + third_variable
)
```

### 层级缩进一致

```python
if score >= 60:
    if score >= 90:
        print("优秀")
    else:
        print("及格")
```

每一层缩进 4 个空格，嵌套多少层就缩进多少次。

## 空行

通用格式：**顶层函数之间、顶层类之间、函数与类之间，均留 2 个空行；类内方法之间留 1 个空行。**

### 函数和类之间

**两个空行**分隔顶层函数和类：

```python
def func_a():
    pass


def func_b():
    pass


class Student:
    pass
```

### 方法之间

类里面方法之间用**一个空行**分隔：

```python
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
```

### 函数内部

逻辑段落之间用空行分隔，但不要过多：

```python
def process_data(data):
    # 第一步：过滤
    valid = [d for d in data if d is not None]

    # 第二步：转换
    result = [transform(d) for d in valid]

    # 第三步：排序
    result.sort()
    return result
```

**不要在函数里随便加空行。** 一个函数超过 3-4 个空行说明逻辑分块太多，考虑拆成更小的函数。

## 空格的使用

### 运算符两边加空格

```python
# 推荐
x = 1 + 2
y = x * 3
name = "hello"

# 不推荐
x=1+2
y=x*3
name="hello"
```

### 逗号后面加空格

```python
# 推荐
nums = [1, 2, 3]
def func(a, b, c):
    pass

# 不推荐
nums = [1,2,3]
def func(a,b,c):
    pass
```

### 括号内部不要加多余空格

```python
# 推荐
nums = [1, 2, 3]
info = {"name": "张三"}

# 不推荐
nums = [ 1, 2, 3 ]         # 列表内不要首尾空格
info = { "name": "张三" }  # 字典内不要首尾空格
```

### 不要在括号前加空格

```python
# 推荐
print("hello")
func(a, b)

# 不推荐
print ("hello")    # 函数名和括号之间不要空格
func (a, b)       # 同上
```

### 冒号前不要空格

```python
# 推荐
if x > 0:
    pass

# 不推荐
if x > 0 :
    pass

# 推荐
info = {"name": "张三"}

# 不推荐
info = {"name" : "张三"}   # 冒号前不要空格
```

## 导入顺序

按**标准库、第三方库、本地模块**分组，组间空行：

通用格式：

```python
# 1. 标准库
import <标准库模块>
# 2. 第三方库
import <第三方库模块>
# 3. 本地模块
from <本地模块> import <名称>
```

具体示例：

```python
# 标准库
import os
import sys
import json

# 第三方库
import requests
import numpy as np

# 本地模块
from myproject.utils import helper
from myproject.models import Student
```

**每组内按字母顺序排列。**

### 每行一个导入

```python
# 推荐
import os
import sys

# 不推荐
import os, sys
```

但 `from ... import` 可以一行导入多个：

```python
from math import sqrt, pi, ceil
```

### 避免通配符导入

```python
# 不推荐
from os import *

# 推荐
import os
from os import path, getcwd, listdir
```

## 其他约定

### 每行不超过 79 字符

通用格式：**每行不超过 79 个字符。**

PEP 8 建议每行不超过 79 个字符。现代开发中可以放宽到 99 或 120，但太长的行还是会影响阅读。

```python
# 太长，一行写不下
result = some_function(argument_one, argument_two, argument_three, argument_four, argument_five)

# 括号换行
result = some_function(
    argument_one, argument_two, argument_three,
    argument_four, argument_five
)
```

### 字符串引号

PEP 8 不强制单引号还是双引号。**保持项目内一致就行**。

```python
# 都可以
name = '张三'
name = "张三"

# 字符串里有引号时选另一种
message = "He said 'hello'"
message = 'He said "hello"'
```

### 行尾不要有空格

```python
# 不推荐
name = "张三"   
#              ↑ 行尾有空格，编辑器可能看不出来但会留坑

# 推荐
name = "张三"
```

### 文件末尾空一行

每个 Python 文件末尾保留一个空行。

## 工具辅助

手动遵守所有规则太累，实际开发用工具自动检查和格式化：

**flake8** — 检查代码是否符合 PEP 8：

```bash
pip install flake8
flake8 my_code.py
```

**black** — 自动格式化代码为 PEP 8 风格：

```bash
pip install black
black my_code.py
```

**isort** — 自动排序 import 语句：

```bash
pip install isort
isort my_code.py
```

**VS Code / PyCharm** 内置 PEP 8 检查，写代码时实时提示。**推荐配置 black + isort 保存时自动格式化**，就不用手动管这些了。

## 速查表

| 项目 | 约定 |
|---|---|
| 变量/函数 | 小写加下划线 `my_func` |
| 类名 | 大驼峰 `MyClass` |
| 常量 | 全大写 `MAX_SIZE` |
| 私有 | 前缀下划线 `_private` |
| 布尔变量 | `is_` / `has_` 开头 |
| 缩进 | 4 个空格，不用 tab |
| 顶层函数间 | 2 个空行 |
| 类方法间 | 1 个空行 |
| 运算符两边 | 加空格 |
| 逗号后 | 加空格 |
| 括号前 | 不加空格 |
| 导入顺序 | 标准库 → 第三方 → 本地 |
| 每行长度 | 不超过 79（可放宽到 99-120） |

## 要点

PEP 8 的核心就三件事：**命名有规律（小写下划线给变量函数、大驼峰给类、全大写给常量）、缩进用 4 个空格、空行分清层级（顶层 2 行、方法间 1 行）**。加上空格规则（运算符两边加、逗号后加、括号前不加）和导入顺序（标准库 → 第三方 → 本地），日常代码就能写规范。实际开发用 **black + isort** 自动格式化，机器帮你遵守规则，人专注写逻辑就行。

---

## 本仓库学习导航
对照自己的 exercises 代码；见 [FAQ](../../docs/faq-common-mistakes.md)
