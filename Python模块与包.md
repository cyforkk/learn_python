# Python 模块与包：从 import 到拆分自己的代码文件

## 为什么需要模块

一个文件写一千行代码，找东西难、改东西怕碰别的、没法复用。**模块就是把代码拆成多个文件**，每个文件负责一块功能，需要时再导入使用。Python 本身自带了大量模块，比如 `random`、`os`、`csv`，前面文章中已经在用了。

## import — 导入模块

### 基本用法

**语法格式：**

```python
import 模块名
```

```python
import random

answer = random.randint(1, 100)
```

`import random` 把整个 random 模块导入，使用时用 `random.函数名` 访问。

### 导入多个模块

```python
import os
import sys
import csv
import json
```

一行导入一个，也可以一行导入多个（不推荐，可读性差）：

```python
import os, sys, csv
```

### from ... import — 只导入需要的

**语法格式：**

```python
from 模块名 import 函数名
```

```python
from random import randint

answer = randint(1, 100)   # 不用写 random. 前缀
```

只导入 `randint` 函数，调用时直接用函数名，不用加模块名前缀。

```python
from random import randint, choice, shuffle
```

一次导入多个。

### import ... as — 取别名

**语法格式：**

```python
import 模块名 as 别名
from 模块名 import 函数名 as 别名
```

```python
import numpy as np          # numpy 太长，取个短的别名
from datetime import datetime as dt

print(np.array([1, 2, 3]))
print(dt.now())
```

别名让代码更简洁，社区有约定俗成的缩写，比如 `numpy as np`、`pandas as pd`。

## 常用标准库

Python 自带的模块，不需要安装，直接 import 就能用：

| 模块 | 用途 |
|---|---|
| `os` | 操作系统接口（路径、环境变量） |
| `sys` | Python 解释器相关（命令行参数、路径） |
| `random` | 随机数 |
| `math` | 数学函数（sin、cos、sqrt 等） |
| `datetime` | 日期时间处理 |
| `json` | JSON 读写 |
| `csv` | CSV 文件读写 |
| `pathlib` | 路径操作（推荐替代 os.path） |
| `collections` | 高级容器（Counter、defaultdict 等） |
| `itertools` | 迭代工具 |
| `functools` | 函数工具（reduce、lru_cache 等） |

**标准库是 Python 的核心竞争力之一。** 能用标准库解决的就不用第三方库，少一个依赖少一个麻烦。

## 自己拆文件 — 创建模块

### 最简单的例子

项目目录：

```
my_project/
├── main.py
└── utils.py
```

`utils.py` 里写工具函数：

```python
# utils.py
def greet(name):
    return f"你好，{name}"

def add(a, b):
    return a + b
```

`main.py` 里导入使用：

```python
# main.py
import utils

print(utils.greet("张三"))   # 你好，张三
print(utils.add(3, 5))       # 8
```

**同一个目录下的 .py 文件就是模块**，文件名就是模块名（去掉 .py）。`utils.py` 就是 `utils` 模块。

### from ... import 导入自己的模块

```python
# main.py
from utils import greet, add

print(greet("张三"))   # 不需要 utils. 前缀
print(add(3, 5))
```

### 导入整个模块

```python
# main.py
import utils

print(utils.greet("张三"))
print(utils.add(3, 5))
```

两种方式的选择：**用得多就 import 模块名，只用一两个函数就 from import。**

## __name__ == "__main__"

### 问题：导入时代码自动执行

```python
# utils.py
def greet(name):
    return f"你好，{name}"

print("utils 模块被加载了")   # 这行在 import 时会执行
greet("测试")                # 这行也会执行
```

```python
# main.py
import utils   # 会打印 "utils 模块被加载了" 和执行 greet("测试")
```

导入模块时，模块里的**顶层代码会自动执行**。但很多时候我们只想用里面的函数，不想让它自动执行东西。

### 解决方案

**语法格式：**

```python
if __name__ == "__main__":
    # 直接运行时执行的代码
    pass
```

```python
# utils.py
def greet(name):
    return f"你好，{name}"

def main():
    greet("测试")

if __name__ == "__main__":
    main()
```

`__name__` 在模块被直接运行时等于 `"__main__"`，被导入时等于模块名 `"utils"`。

- **直接运行 `python utils.py`** → `__name__` 是 `"__main__"` → `main()` 执行
- **`import utils`** → `__name__` 是 `"utils"` → `main()` 不执行

**这个判断是 Python 模块的标配写法**，让文件既能被导入使用，又能独立运行测试。

## 包 — 多个模块组织在一起

### 目录结构

```
my_project/
├── main.py
└── mypackage/           # 包就是一个有 __init__.py 的目录
    ├── __init__.py      # 标识这是一个包
    ├── math_tools.py
    └── string_tools.py
```

`mypackage` 是一个包，里面有两个模块文件。

### 使用包中的模块

**语法格式：**

```python
from 包名 import 模块名
from 包名.模块名 import 函数名
```

```python
# main.py
from mypackage import math_tools, string_tools

print(math_tools.add(3, 5))
print(string_tools.reverse("hello"))
```

或者：

```python
from mypackage.math_tools import add

print(add(3, 5))
```

### __init__.py

`__init__.py` 文件标识一个目录是 Python 包。可以是空文件，也可以写初始化代码：

```python
# mypackage/__init__.py
from .math_tools import add
from .string_tools import reverse
```

有了这个 `__init__.py` 后，导入方式可以简化：

```python
# main.py
from mypackage import add, reverse   # 直接从包名导入
```

**Python 3.3+ 支持没有 `__init__.py` 的命名空间包**，但初学者不用管，**建包时加上 `__init__.py` 就行**。

### 完整项目示例

```
student_system/
├── main.py
├── models.py          # 数据模型
├── utils.py           # 工具函数
├── storage.py         # 数据存取
└── tests/             # 测试
    ├── __init__.py
    └── test_utils.py
```

`models.py`：

```python
# models.py
def create_student(name, score):
    return {"name": name, "score": score}
```

`storage.py`：

```python
# storage.py
import csv

def save_students(students, filename="students.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(students)

def load_students(filename="students.csv"):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({"name": row["name"], "score": int(row["score"])})
    return students
```

`main.py`：

```python
# main.py
from models import create_student
from storage import save_students, load_students

def main():
    students = [
        create_student("张三", 85),
        create_student("李四", 92),
    ]
    save_students(students)
    
    loaded = load_students()
    for s in loaded:
        print(f"{s['name']}: {s['score']}分")

if __name__ == "__main__":
    main()
```

每个文件负责一块功能，`main.py` 导入其他模块，组合起来运行。**这就是模块化的基本思路：按功能拆文件，通过 import 组合。**

## pip install 的第三方库

标准库不够用时，用 pip 安装第三方库：

```bash
pip install requests
```

安装后直接 import：

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

第三方库存放在 PyPI（Python Package Index）上，`pip install` 从那里下载安装。

## import 的搜索路径

Python 找模块时按顺序搜索以下路径：

1. **当前目录**（你运行脚本的目录）
2. **PYTHONPATH 环境变量**中的目录
3. **标准库**目录
4. **site-packages**（pip 安装的第三方库）

```python
import sys
print(sys.path)   # 查看搜索路径
```

**常见坑：** 自己写的模块名和标准库重名。比如你写了一个 `random.py`，`import random` 会导入你的文件而不是标准库。**避免给文件取标准库的名字。**

## 常见用法速查

```python
# 导入整个模块
import os

# 导入模块中的特定内容
from random import randint

# 导入并取别名
import numpy as np

# 导入自己的模块（同目录下）
import utils
from utils import greet, add

# 导入包中的模块
from mypackage import math_tools
from mypackage.math_tools import add

# 标准库
import random, math, datetime, json, csv, os
```

## 最佳实践

**文件名不要和标准库重名。** 不要写 `random.py`、`os.py`、`csv.py`，否则 `import` 会导入你的文件而不是标准库。

**用 `if __name__ == "__main__":` 保护直接运行的代码。** 模块里有测试代码时，放在这个判断里，避免导入时自动执行。

**按功能拆分模块。** 一个文件不要超过几百行，功能相关的函数放一起，不相关的拆到不同文件。学生的成绩管理可以拆成 `models.py`（数据结构）、`storage.py`（存取）、`main.py`（入口）。

**`from module import *` 不要用。** 它会把模块里所有内容导入，容易造成命名冲突，而且看不出某个名字是从哪个模块来的。

## 速查表

| 操作 | 代码 |
|---|---|
| 导入标准库 | `import os` |
| 导入特定函数 | `from random import randint` |
| 取别名 | `import numpy as np` |
| 自己的模块 | `import utils`（同目录下） |
| 包中导入 | `from mypackage import module` |
| 保护直接运行 | `if __name__ == "__main__":` |
| 安装第三方库 | `pip install requests` |

## 要点

模块和包的核心就两件事：**用 import 导入别人的代码，把自己的代码拆成多个文件**。`import 模块名` 导入整个模块，`from 模块名 import 函数名` 只导入需要的部分。同一个目录下的 .py 文件互相 import 就能组成项目。包就是带 `__init__.py` 的文件夹。`if __name__ == "__main__":` 让文件既能被导入又能独立运行。记住不要和标准库重名、不要用 `import *`，日常开发就够用了。
