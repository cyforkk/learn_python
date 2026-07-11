# Python 文件读写：open、with 与文本/CSV 基础

## 为什么需要文件操作

程序运行时数据都在内存里，程序一关就没了。**文件读写让数据持久化**——把结果存到硬盘上，下次程序启动还能读回来。配置文件、日志记录、数据导出，都离不开文件操作。

## open — 打开文件

### 基本用法

```python
# 语法
文件对象 = open(文件路径, 模式, encoding="编码")
```

```python
f = open("test.txt", "r")    # 打开文件
content = f.read()            # 读取内容
f.close()                     # 关闭文件
```

`open` 第一个参数是文件路径，第二个是**模式**：

| 模式 | 含义 | 文件不存在时 |
|---|---|---|
| `"r"` | 只读（默认） | 报错 |
| `"w"` | 只写（覆盖） | 创建新文件 |
| `"a"` | 追加（末尾添加） | 创建新文件 |
| `"r+"` | 读写 | 报错 |
| `"w+"` | 写读（先清空） | 创建新文件 |

### 不用手动 close

上面的写法有个问题：如果 `read()` 出错，`close()` 不会执行，文件一直开着占资源。Python 推荐用 `with` 语句自动管理。

## with — 自动关闭文件

### 基本用法

```python
# 语法
with open(文件路径, 模式, encoding="编码") as 变量名:
    使用变量名操作文件
```

```python
with open("test.txt", "r") as f:
    content = f.read()
# 离开 with 块后，文件自动关闭，不用手动 close
```

**无论中间是否出错，`with` 块结束时都会自动关闭文件。** 这是最推荐的写法。

### 为什么推荐 with

```python
# 不推荐：忘了 close 或中间出错导致文件没关闭
f = open("data.txt", "r")
content = f.read()
# 如果上面这行报错，close 永远不会执行
f.close()

# 推荐：with 自动处理
with open("data.txt", "r") as f:
    content = f.read()
# 到这里文件已经关闭了
```

**记住一条规则：用 open 就用 with，不要手动 close。**

## 读文件

### 读取整个文件

```python
# 语法
内容 = 文件对象.read()
```

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()    # 一次性读取全部内容，返回字符串
print(content)
```

### 逐行读取

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())    # strip 去掉每行末尾的换行符
```

文件对象本身是可迭代的，`for line in f` 逐行读取，**内存友好**，大文件也能处理。

### 读取所有行到列表

```python
# 语法
行列表 = 文件对象.readlines()
```

```python
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()   # 返回列表，每个元素是一行
print(lines)   # ['第一行\n', '第二行\n', '第三行\n']
```

`readlines()` 一次性把所有行读进列表，大文件不建议用。

### 三种读取方式对比

```python
# 语法
内容 = 文件对象.read()        # 读取全部，返回字符串
一行 = 文件对象.readline()    # 每次读一行，返回字符串
行列表 = 文件对象.readlines() # 读取所有行，返回列表
```

```python
# 方式一：read() — 读取全部，返回一个字符串
content = f.read()

# 方式二：readline() — 每次读一行，返回字符串
line = f.readline()

# 方式三：直接遍历 — 每次读一行，最省内存
for line in f:
    print(line)
```

**小文件用 `read()`，大文件用 `for line in f`。**

## 写文件

### 覆盖写入（w 模式）

```python
# 语法
文件对象.write(字符串)
```

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

`"w"` 模式会**清空原文件内容**再写入。如果文件已存在，内容被覆盖。

### 追加写入（a 模式）

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("新的一条日志\n")
```

`"a"` 模式在文件**末尾追加**，不改原有内容。文件不存在时自动创建。

### 写入多行

```python
# 语法
文件对象.writelines(字符串列表)
```

```python
lines = ["张三\n", "李四\n", "王五\n"]
with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

**注意：** `writelines` 不会自动加换行符，每行内容需要自己包含 `\n`。

### write 和 print 的区别

```python
# write：需要手动加换行符
f.write("hello\n")

# print：可以指定 file 参数，自动加换行符
print("hello", file=f)
```

**`print` 配合 `file` 参数写文件更方便**，不用手动管换行符。

## encoding 参数

读写中文文件时一定要加 `encoding="utf-8"`：

```python
# 不加 encoding 可能乱码
with open("data.txt", "r") as f:
    content = f.read()   # Windows 上可能报错或乱码

# 加 encoding 确保编码一致
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()   # 正确读取中文
```

Windows 默认用 GBK 编码，如果文件是 UTF-8 保存的，不加 `encoding="utf-8"` 会报错或乱码。**养成习惯：读写文件都加 `encoding="utf-8"`。**

## CSV 文件操作

CSV 是用逗号分隔的表格文件，数据处理中最常见的格式之一。

### 读取 CSV

```python
# 语法
import csv
reader = csv.reader(文件对象)
for 行 in reader:
    # 行是列表，每个元素是一列的值
```

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)   # row 是列表，每个元素是一列的值
```

假设 `students.csv` 内容：

```
姓名,分数,等级
张三,85,B
李四,92,A
王五,78,C
```

输出：

```
['姓名', '分数', '等级']
['张三', '85', 'B']
['李四', '92', 'A']
['王五', '78', 'C']
```

### 读取为字典

```python
# 语法
import csv
reader = csv.DictReader(文件对象)
for 行 in reader:
    # 行是字典，键为表头字段名
```

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']}: {row['分数']}分")
# 张三: 85分
# 李四: 92分
# 王五: 78分
```

`DictReader` 把每行读成字典，键是第一行的表头。比 `reader` 更直观。

### 写入 CSV

```python
# 语法
import csv
writer = csv.writer(文件对象)
writer.writerow(一行列表)    # 写入一行
writer.writerows(多行列表)    # 写入多行
```

```python
import csv

data = [
    ["姓名", "分数", "等级"],
    ["张三", 85, "B"],
    ["李四", 92, "A"],
    ["王五", 78, "C"],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

**注意：** 写 CSV 时要加 `newline=""`，否则 Windows 上会出现空行。

### 以字典形式写入

```python
# 语法
import csv
writer = csv.DictWriter(文件对象, fieldnames=字段名列表)
writer.writeheader()        # 写表头
writer.writerow(字典)       # 写入一行
writer.writerows(字典列表)  # 写入多行
```

```python
import csv

data = [
    {"姓名": "张三", "分数": 85, "等级": "B"},
    {"姓名": "李四", "分数": 92, "等级": "A"},
    {"姓名": "王五", "分数": 78, "等级": "C"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["姓名", "分数", "等级"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()      # 写表头
    writer.writerows(data)   # 写数据
```

`DictWriter` 适合处理结构化数据，每行是一个字典，字段名用 `fieldnames` 指定。

## 实用示例

### 统计文件行数

```python
with open("data.txt", "r", encoding="utf-8") as f:
    count = sum(1 for line in f)
print(f"共 {count} 行")
```

`sum(1 for line in f)` 是统计行数的简洁写法，比 `len(f.readlines())` 省内存。

### 读取配置文件

假设有配置文件 `config.txt`：

```
host=127.0.0.1
port=8080
debug=True
```

```python
config = {}
with open("config.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line:
            key, value = line.split("=", 1)
            config[key] = value

print(config)
# {'host': '127.0.0.1', 'port': '8080', 'debug': 'True'}
```

### 简易日志

```python
from datetime import datetime

def log(message, file="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

log("程序启动")
log("用户登录: 张三")
log("操作完成")
```

`"a"` 追加模式保证每次写入不覆盖之前的日志。

### 批量处理学生成绩

```python
import csv

def save_students(students, filename="students.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["姓名", "分数"])
        writer.writeheader()
        for name, score in students.items():
            writer.writerow({"姓名": name, "分数": score})

def load_students(filename="students.csv"):
    students = {}
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students[row["姓名"]] = int(row["分数"])
    return students

# 保存
students = {"张三": 85, "李四": 92, "王五": 78}
save_students(students)

# 读取
loaded = load_students()
print(loaded)   # {'张三': 85, '李四': 92, '王五': 78}
```

程序退出前保存到 CSV，下次启动再读回来，数据就持久化了。

## 速查表

| 操作 | 代码 |
|---|---|
| 读整个文件 | `f.read()` |
| 逐行读取 | `for line in f:` |
| 读所有行到列表 | `f.readlines()` |
| 写字符串 | `f.write("text\n")` |
| 写入多行 | `f.writelines(list)` |
| print 写文件 | `print("text", file=f)` |
| 读 CSV | `csv.reader(f)` |
| 读 CSV 为字典 | `csv.DictReader(f)` |
| 写 CSV | `csv.writer(f)` |
| 写 CSV 字典 | `csv.DictWriter(f, fieldnames=...)` |
| 自动关闭 | `with open(...) as f:` |
| 指定编码 | `encoding="utf-8"` |

## 要点

文件读写的核心就四个动作：**开（open）、读/写（read/write）、关（close）**。用 `with` 语句把"关"这件事自动化，永远不用手动 close。读小文件用 `read()`，读大文件用 `for line in f`。写文件注意 `"w"` 覆盖和 `"a"` 追加的区别。CSV 操作记住 `csv.reader` / `csv.DictReader` / `csv.writer` 三个工具。**中文文件一定加 `encoding="utf-8"`**，否则乱码问题会浪费你很多时间。

---

## 本仓库练习（只列题目 · 答案在链接里）

本篇读完先不急着做题；与「异常处理」一起读完再做。

### 过关 · 安全读文件（在异常篇后做）

**题目：** 输入路径 → 读文件打印；不存在则提示不崩溃。  

**打开作业：** [ex02_safe_read.py](../exercises/ex02_safe_read.py)  
**参考答案（做完再看）：** [solutions/ex02_safe_read.py](../solutions/ex02_safe_read.py)

### 加练（可选）· JSON 待办

**题目：** 用 JSON 文件保存待办，支持 add / list / quit。  

**打开作业：** [ex01_todo_json.py](../exercises/ex01_todo_json.py)  
**参考答案（做完再看）：** [solutions/ex01_todo_json.py](../solutions/ex01_todo_json.py)
