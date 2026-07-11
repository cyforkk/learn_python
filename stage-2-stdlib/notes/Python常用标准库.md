# Python 常用标准库：pathlib、json、datetime、os/sys、re、collections

## 为什么学标准库

Python 自带了大量模块，不需要安装就能用。**能用标准库解决的就不要装第三方库**——少一个依赖少一个麻烦。下面这几个是日常开发中用得最多的，先会用就行，深入用法用到再查。

## pathlib — 路径操作

### 为什么用它

以前拼接路径要用 `os.path.join("dir", "file.txt")`，字符串操作容易出错。`pathlib` 用面向对象的方式处理路径，**更直观、更安全**。

### 基本用法

**语法格式：**

```python
from pathlib import Path

路径对象 = Path(路径字符串)
拼接路径 = Path("目录") / "文件名"
```

```python
from pathlib import Path

# 当前目录
p = Path(".")
print(p)   # .

# 拼接路径
file = Path("data") / "students.csv"
print(file)   # data/students.csv（自动处理分隔符）

# 绝对路径
file = Path("E:/talkAI/learn_python/data/students.csv")

# 当前文件的目录
current_dir = Path(__file__).parent
```

### 常用操作

```python
from pathlib import Path

p = Path("data/students.csv")

# 判断
p.exists()       # True/False 是否存在
p.is_file()      # True/False 是否是文件
p.is_dir()       # True/False 是否是目录

# 获取属性
p.name           # "students.csv"（文件名）
p.stem           # "students"（不含扩展名）
p.suffix         # ".csv"（扩展名）
p.parent         # Path("data")（父目录）
p.absolute()     # 绝对路径

# 创建和删除
p.mkdir()        # 创建目录
p.touch()        # 创建空文件
p.unlink()       # 删除文件
```

### 遍历目录

```python
from pathlib import Path

# 列出目录下所有文件
for f in Path(".").iterdir():
    print(f)

# 递归查找所有 .py 文件
for f in Path(".").rglob("*.py"):
    print(f)
```

### 读写文件

Path 对象自带读写方法，不用 `open`：

**语法格式：**

```python
路径对象.write_text(文本内容, encoding="编码")
内容 = 路径对象.read_text(encoding="编码")
```

```python
from pathlib import Path

p = Path("data.txt")

# 写
p.write_text("hello world", encoding="utf-8")

# 读
content = p.read_text(encoding="utf-8")
print(content)
```

## json — JSON 读写

### 为什么用它

JSON 是最常用的数据交换格式，API 返回数据、配置文件都用它。Python 字典和 JSON 对象几乎一一对应。

### 基本操作

**语法格式：**

```python
import json

json字符串 = json.dumps(对象, ensure_ascii=False, indent=2)
对象 = json.loads(json字符串)
```

```python
import json

# Python 字典 → JSON 字符串
data = {"name": "张三", "age": 25, "scores": [85, 92, 78]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
# {
#   "name": "张三",
#   "age": 25,
#   "scores": [85, 92, 78]
# }

# JSON 字符串 → Python 字典
parsed = json.loads(json_str)
print(parsed["name"])   # 张三
```

**两个关键参数：**

`ensure_ascii=False` — 中文不转义成 `\uXXXX`，直接显示中文。**处理中文必须加。**

`indent=2` — 缩进美化输出，方便人看。程序读取不用的可以省略。

### 文件读写

**语法格式：**

```python
json.dump(对象, 文件对象, ensure_ascii=False, indent=2)
对象 = json.load(文件对象)
```

```python
import json
from pathlib import Path

data = {"name": "张三", "age": 25, "city": "北京"}

# 写入文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 从文件读取
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded["name"])   # 张三
```

**`dumps/loads` 处理字符串，`dump/load` 处理文件。** 带 s 的操作字符串，不带 s 的操作文件。

### 类型对应

| Python | JSON |
|---|---|
| dict | object |
| list / tuple | array |
| str | string |
| int / float | number |
| True / False | true / false |
| None | null |

JSON 不支持 Python 的 set（会报错），tuple 会被转为 array（和列表一样）。

## datetime — 日期时间

### 基本对象

**语法格式：**

```python
from datetime import datetime

当前时间 = datetime.now()
指定时间 = datetime(年, 月, 日, 时, 分, 秒)
```

```python
from datetime import datetime, date, time, timedelta

# 当前时间
now = datetime.now()
print(now)   # 2025-07-11 14:30:00.123456

# 当前日期
today = date.today()
print(today)   # 2025-07-11

# 指定日期时间
dt = datetime(2025, 7, 11, 14, 30, 0)
print(dt)   # 2025-07-11 14:30:00
```

### 格式化和解析

**语法格式：**

```python
from datetime import datetime

字符串 = datetime对象.strftime(格式字符串)
datetime对象 = datetime.strptime(字符串, 格式字符串)
```

```python
from datetime import datetime

# datetime → 字符串
now = datetime.now()
print(now.strftime("%Y-%m-%d"))        # 2025-07-11
print(now.strftime("%Y/%m/%d %H:%M"))   # 2025/07/11 14:30
print(now.strftime("%Y年%m月%d日"))      # 2025年07月11日

# 字符串 → datetime
dt = datetime.strptime("2025-07-11", "%Y-%m-%d")
print(dt)   # 2025-07-11 00:00:00
```

**常用格式化代码：**

| 代码 | 含义 | 示例 |
|---|---|---|
| `%Y` | 四位年份 | 2025 |
| `%m` | 月份 | 07 |
| `%d` | 日 | 11 |
| `%H` | 时（24小时制） | 14 |
| `%M` | 分 | 30 |
| `%S` | 秒 | 00 |
| `%A` | 星期名 | Friday |
| `%w` | 星期数字 | 5（周一为1） |

### 时间差 timedelta

**语法格式：**

```python
from datetime import timedelta

时间差 = timedelta(days=1, hours=3, weeks=1)
新时间 = datetime对象 + 时间差
```

```python
from datetime import datetime, timedelta

now = datetime.now()

# 加减时间
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
in_3_hours = now + timedelta(hours=3)

print(tomorrow)
print(last_week)

# 两个日期的差
d1 = datetime(2025, 7, 11)
d2 = datetime(2025, 1, 1)
diff = d1 - d2
print(diff.days)   # 191（相差多少天）
```

### 实际用途

```python
from datetime import datetime

# 日志时间戳
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

log("程序启动")
log("处理完成")
```

## os / sys — 系统接口

### os — 操作系统接口

```python
import os

# 当前工作目录
print(os.getcwd())

# 列出目录内容
print(os.listdir("."))

# 环境变量
print(os.environ.get("PATH"))

# 路径操作
print(os.path.join("dir", "file.txt"))   # dir/file.txt
print(os.path.exists("data.txt"))         # True/False
print(os.path.isfile("data.txt"))         # True/False
```

**pathlib 可以替代大部分 os.path 的功能，新项目优先用 pathlib。**

### sys — Python 运行环境

```python
import sys

# 命令行参数
print(sys.argv)
# python main.py --input data.txt --output result.txt
# sys.argv = ["main.py", "--input", "data.txt", "--output", "result.txt"]

# Python 搜索路径
print(sys.path)

# 退出程序
sys.exit(0)   # 正常退出
sys.exit(1)   # 异常退出
```

**最常用的是 `sys.argv`**，获取命令行参数。写命令行工具时会用到。

## re — 正则表达式

### 为什么用它

字符串的 `find` 和 `replace` 只能做精确匹配。正则表达式可以**模式匹配**——验证邮箱格式、提取所有数字、替换所有以字母 a 开头的单词。

### 基本匹配

**语法格式：**

```python
import re

匹配对象 = re.search(模式, 字符串)
匹配列表 = re.findall(模式, 字符串)
新字符串 = re.sub(模式, 替换, 字符串)
```

```python
import re

# 查找第一个匹配
result = re.search(r"\d+", "价格是250元")
print(result.group())   # 250

# 查找所有匹配
results = re.findall(r"\d+", "买了3个苹果，花了15元，还剩20元")
print(results)   # ['3', '15', '20']

# 替换
new_text = re.sub(r"\d+", "X", "买了3个苹果，花了15元")
print(new_text)   # 买了X个苹果，花了X元
```

### 常用正则符号

| 符号 | 含义 | 示例 |
|---|---|---|
| `\d` | 数字 | `\d+` 匹配一个或多个数字 |
| `\w` | 字母数字下划线 | `\w+` 匹配单词 |
| `\s` | 空白字符 | 空格、tab、换行 |
| `.` | 任意字符（除换行） | `a.b` 匹配 acb、aab |
| `+` | 前一个至少一次 | `\d+` 一个或多个数字 |
| `*` | 前一个零次或多次 | `a*` 零个或多个 a |
| `?` | 前一个零次或一次 | `colou?r` 匹配 color、colour |
| `{n}` | 精确 n 次 | `\d{4}` 四位数字 |
| `{n,m}` | n 到 m 次 | `\d{1,3}` 一到三位数字 |
| `[abc]` | 字符集 | `[aeiou]` 匹配元音 |
| `^` | 开头 | `^hello` 以 hello 开头 |
| `$` | 结尾 | `world$` 以 world 结尾 |

### 实用示例

```python
import re

# 验证手机号
phone = "13812345678"
if re.match(r"^1\d{10}$", phone):
    print("手机号格式正确")

# 提取邮箱
text = "联系我: zhangsan@test.com 或 lisi@hello.cn"
emails = re.findall(r"[\w.]+@[\w.]+", text)
print(emails)   # ['zhangsan@test.com', 'lisi@hello.cn']

# 分割字符串
parts = re.split(r"[,\s]+", "张三, 李四, 王五")
print(parts)   # ['张三', '李四', '王五']
```

**原始字符串 `r""`：** 正则表达式里反斜杠很多，用 `r"\d"` 而不是 `"\\d"`，避免转义混乱。

## collections — 扩展容器

### Counter — 计数器

**语法格式：**

```python
from collections import Counter

计数器 = Counter(可迭代对象)
```

```python
from collections import Counter

# 统计每个元素出现次数
text = "hello world"
counter = Counter(text)
print(counter)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 取出现最多的
print(counter.most_common(3))
# [('l', 3), ('o', 2), ('h', 1)]

# 统计列表
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(fruits)
print(counter["apple"])   # 3
print(counter.most_common(2))   # [('apple', 3), ('banana', 2)]
```

**实际用途：** 统计词频、统计商品销量排名、投票计数。

### defaultdict — 带默认值的字典

**语法格式：**

```python
from collections import defaultdict

字典 = defaultdict(默认工厂)
```

```python
from collections import defaultdict

# 普通 dict 键不存在会报错
scores = {}
# scores["张三"] += 10   # KeyError

# defaultdict 键不存在时自动创建默认值
scores = defaultdict(int)   # 默认值为 0
scores["张三"] += 10
scores["李四"] += 20
print(scores)   # defaultdict(<class 'int'>, {'张三': 10, '李四': 20})

# 默认值为空列表
groups = defaultdict(list)
students = [("A班", "张三"), ("B班", "李四"), ("A班", "王五")]
for class_name, name in students:
    groups[class_name].append(name)

print(groups)
# defaultdict(<class 'list'>, {'A班': ['张三', '王五'], 'B班': ['李四']})
```

**实际用途：** 分组、累加计数、避免每次都要判断键是否存在。

## 速查表

| 库 | 核心用途 | 最常用 |
|---|---|---|
| `pathlib` | 路径操作 | `Path("a") / "b"`、`.read_text()`、`.exists()` |
| `json` | JSON 读写 | `json.dumps()` / `json.loads()` |
| `datetime` | 日期时间 | `.now()`、`.strftime()`、`timedelta()` |
| `os` | 操作系统 | `os.getcwd()`、`os.listdir()` |
| `sys` | 运行环境 | `sys.argv`、`sys.exit()` |
| `re` | 正则匹配 | `re.search()`、`re.findall()`、`re.sub()` |
| `collections` | 扩展容器 | `Counter()`、`defaultdict()` |

## 要点

标准库的核心就一句话：**能标准库解决的不装第三方库**。pathlib 替代 os.path 处理路径、json 处理数据交换、datetime 处理时间、re 处理模式匹配、Counter 和 defaultdict 处理统计和分组。这六个库覆盖了日常 80% 的工具需求。**先记住每个库的核心函数，用到时再查详细用法，不用一次全背。**

---

## 本仓库学习导航
## 本仓库练习（只列题目 · 答案在链接里）

### 加练（可选）· 列目录

**题目：** 列出当前目录下的文件和文件夹。  

**打开作业：** [ex04_list_files.py](../exercises/ex04_list_files.py)  
**参考答案（做完再看）：** [solutions/ex04_list_files.py](../solutions/ex04_list_files.py)

### 加练（可选）· 批量重命名计划

**题目：** 给定一组文件名，按规则打印「旧名 → 新名」（可只打印不真改）。  

**打开作业：** [ex06_batch_rename.py](../exercises/ex06_batch_rename.py)  
**参考答案（做完再看）：** [solutions/ex06_batch_rename.py](../solutions/ex06_batch_rename.py)

不是每章标准库都要交作业，会查文档更重要。
