# Python 字符串：常用方法与 f-string 格式化

字符串是 Python 中处理文本的核心类型。几乎每个程序都会涉及文字操作——拼接、查找、替换、格式化输出。掌握字符串方法和 f-string，日常文本处理就够用了。

## 字符串基础

字符串是不可变类型。所有方法都**返回新字符串**，不修改原字符串：

```python
s = "hello"
new_s = s.upper()
print(s)      # hello（原字符串没变）
print(new_s)  # HELLO
```

这一点很重要，所有方法调用后要**接收返回值**，否则结果就丢了。

## 大小写转换

**语法结构：** `字符串.方法名()`

```python
"hello".upper()        # HELLO   全大写
"HELLO".lower()        # hello   全小写
"hello world".title()  # Hello World  每个单词首字母大写
"hello world".capitalize()  # Hello world  仅首字母大写
"hello".swapcase()     # HELLO   大小写互换
```

**实际用途：** 用户输入做大小写无关的比较时，统一转成小写再比较。

## 查找与判断

### 查找位置

**语法结构：** `字符串.find(子串, 起始, 结束)`

```python
s = "hello world"

s.find("world")    # 6（返回首次出现的索引，找不到返回 -1）
s.find("o")        # 4（返回第一个 o 的位置）
s.find("xyz")      # -1（找不到）
s.rfind("o")       # 7（从右侧开始查找）
s.index("world")   # 6（和 find 类似，但找不到会报错）
s.count("l")       # 3（统计出现次数）
```

**find 和 index 的区别：** `find` 找不到返回 -1，`index` 找不到抛 ValueError。优先用 `find`，更安全。

### 判断类型

```python
"hello".isalpha()       # True   是否全字母
"12345".isdigit()       # True   是否全数字
"hello123".isalnum()    # True   是否全字母或数字
"  ".isspace()          # True   是否全空白
"Hello".istitle()       # True   是否每个单词首字母大写
"HELLO".isupper()       # True   是否全大写
"hello".islower()       # True   是否全小写
"hello".startswith("he") # True  是否以指定字符串开头
"hello".endswith("lo")    # True  是否以指定字符串结尾
```

**实际用途：** 校验用户输入是否合法——电话号码 `isdigit()`、姓名 `isalpha()`。

## 替换与分割

### 替换

**语法结构：** `字符串.replace(旧子串, 新子串, 替换次数)`

```python
"hello world".replace("world", "python")  # hello python
"a-b-c".replace("-", " ")                  # a b c
"a-b-c".replace("-", " ", 1)              # a b-c（只替换第一个）
```

### 分割

`split` 把字符串按分隔符切成列表：

**语法结构：** `字符串.split(分隔符, 分割次数)`

```python
"a,b,c".split(",")        # ['a', 'b', 'c']
"hello world".split()     # ['hello', 'world']（默认按空白分割）
"a-b-c".split("-", 1)    # ['a', 'b-c']（只分割一次）
"  hello  world  ".split()  # ['hello', 'world']（自动忽略多余空格）
```

### 拼接

`join` 把可迭代对象合并成字符串，是 `split` 的逆操作：

**语法结构：** `分隔符.join(列表)`

```python
",".join(["a", "b", "c"])     # a,b,c
"-".join(["2025", "01", "01"]) # 2025-01-01
"".join(["a", "b", "c"])      # abc
"".join(["hello", "world"])   # helloworld
```

**join 比 + 更高效。** 大量字符串拼接时，用 `"分隔符".join(list)` 而不是 `a + b + c`，因为字符串不可变，+ 每次都创建新对象。

### 去除空白

**语法结构：** `字符串.strip(要去除的字符)`

```python
"  hello  ".strip()     # "hello"（去掉两端空白）
"  hello  ".lstrip()    # "hello  "（只去左端）
"  hello  ".rstrip()    # "  hello"（只去右端)
```

也可以指定要去掉的字符：

```python
"###hello###".strip("#")   # hello
"abchelloabc".strip("abc") # hello（去掉两端所有 a、b、c 字符）
```

**实际用途：** 处理用户输入时去掉首尾空格，`input().strip()` 是常见写法。

## 其他常用方法

### 重复与填充

```python
"hello".center(11)        # "   hello   "（居中，总宽度11）
"hello".center(11, "-")   # "---hello---"（用 - 填充）
"hello".ljust(10)         # "hello     "（左对齐）
"hello".rjust(10)         # "     hello"（右对齐）
"5".zfill(3)              # "005"（左侧补零）
```

### 编码与转换

```python
"hello".encode("utf-8")  # b'hello'（字符串转 bytes）
b"hello".decode("utf-8") # "hello"（bytes 转字符串）

ord("A")   # 65（字符转 Unicode 码点）
chr(65)    # "A"（Unicode 码点转字符）
```

## f-string 格式化输出

f-string 是 Python 3.6+ 引入的格式化语法，**目前最推荐的字符串格式化方式**。在大括号 `{}` 中直接写变量名或表达式。

### 基本用法

**语法结构：** `f"文本{变量名}"`

```python
name = "张三"
age = 25
print(f"我叫{name}，今年{age}岁")   # 我叫张三，今年25岁
```

### 表达式

大括号里可以写任意表达式：

```python
print(f"明年{age + 1}岁")           # 明年26岁
print(f"{'hello'.upper()}")         # HELLO
print(f"{len('hello')} 个字符")     # 5 个字符
```

### 数字格式化

**语法结构：** `f"{变量:格式说明}"`

```python
pi = 3.14159265
print(f"{pi:.2f}")          # 3.14（保留两位小数）
print(f"{pi:.4f}")          # 3.1416（保留四位小数）
print(f"{1000000:,}")       # 1,000,000（千位分隔符）
print(f"{0.15:.1%}")        # 15.0%（百分比格式）
```

### 对齐与填充

**语法结构：** `f"{变量:对齐符宽度}"`（对齐符：`<` 左对齐、`>` 右对齐、`^` 居中）

```python
text = "hello"
print(f"{text:>10}")   # "     hello"（右对齐，宽度10）
print(f"{text:<10}")   # "hello     "（左对齐，宽度10）
print(f"{text:^10}")   # "  hello   "（居中，宽度10）
print(f"{text:*^10}")  # "**hello***"（居中，用 * 填充）
```

### 日期格式化

**语法结构：** `f"{日期对象:%格式符}"`

```python
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d}")           # 2025-07-11
print(f"{now:%Y年%m月%d日}")        # 2025年07月11日
print(f"{now:%H:%M:%S}")            # 14:30:00
print(f"{now:%Y-%m-%d %H:%M}")     # 2025-07-11 14:30
```

### 调试写法（Python 3.8+）

变量名后加 `=`，会同时输出变量名和值，调试时非常方便：

```python
name = "张三"
age = 25
print(f"{name=}, {age=}")   # name='张三', age=25
```

### 多行字符串

```python
name = "张三"
age = 25
city = "北京"

info = f"""
姓名：{name}
年龄：{age}
城市：{city}
"""
print(info)
```

### 格式化速查

| 需求 | 写法 | 示例结果 |
|---|---|---|
| 保留两位小数 | `{pi:.2f}` | 3.14 |
| 千位分隔符 | `{num:,}` | 1,000,000 |
| 百分比 | `{ratio:.1%}` | 15.0% |
| 右对齐 | `{text:>10}` | "     hello" |
| 左对齐 | `{text:<10}` | "hello     " |
| 居中 | `{text:^10}` | "  hello   " |
| 补零 | `{num:05d}` | 00042 |
| 日期 | `{now:%Y-%m-%d}` | 2025-07-11 |

## 速查表

| 方法 | 用途 |
|---|---|
| `s.upper()` / `s.lower()` | 大小写转换 |
| `s.find(sub)` | 查找子串位置，找不到返回 -1 |
| `s.count(sub)` | 统计子串出现次数 |
| `s.replace(old, new)` | 替换 |
| `s.split(sep)` | 分割成列表 |
| `sep.join(iterable)` | 可迭代对象合并成字符串 |
| `s.strip()` | 去除两端空白 |
| `s.startswith(sub)` | 判断是否以指定字符串开头 |
| `s.endswith(sub)` | 判断是否以指定字符串结尾 |
| `s.isdigit()` | 判断是否全数字 |
| `s.isalpha()` | 判断是否全字母 |
| `s.zfill(n)` | 左侧补零到指定宽度 |
| `f"{var}"` | f-string 格式化 |

## 要点

字符串方法中真正高频使用的是：**split 分割、join 拼接、strip 去空白、replace 替换、find 查找、upper/lower 大小写转换**。f-string 格式化掌握**变量插值、数字格式化、对齐填充、日期格式化**这四项就够日常用了。字符串是不可变的，所有方法都返回新字符串，记得接收返回值。

---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python复合类型.md](Python复合类型.md) |
| **下一篇** | [Python函数.md](Python函数.md) |
| **本篇练习** | **无独立作业**。 |

**和前后的关系：** 九九表、猜数字、成绩题里用到的 `f"..."`、字符串拼接，就是本篇内容。可回头打开你写过的作业，标出用到了哪些字符串写法。
