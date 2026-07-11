# Python 输入输出：print 和 input 的全部用法

程序要和人交互，最基本的两个动作就是**输出信息给人看**和**接收人输入的数据**。Python 中这两件事由 `print` 和 `input` 完成。

## print — 输出

### 基本用法

**语法结构：** `print(值1, 值2, ..., sep="分隔符", end="结尾符")`

```python
print("hello world")   # hello world
print(42)              # 42
print(3.14)            # 3.14
```

`print` 可以输出任何类型的数据，不止字符串。

### 输出多个值

用逗号分隔多个值，默认用空格连接：

```python
name = "张三"
age = 25
print("姓名:", name, "年龄:", age)   # 姓名: 张三 年龄: 25
```

用 `sep` 参数自定义分隔符：

```python
print("2025", "01", "01", sep="-")   # 2025-01-01
print("a", "b", "c", sep="")         # abc
```

### 控制结尾

`print` 默认在末尾加换行符 `\n`。用 `end` 参数修改：

```python
print("加载中", end="")
print("...")              # 加载中...（同一行）

print("进度", end=" -> ")
print("完成")             # 进度 -> 完成
```

### 格式化输出

三种方式，从老到新：

**1. f-string（推荐，Python 3.6+）**

**语法结构：** `f"文本{变量名}"`

```python
name = "张三"
age = 25
print(f"我叫{name}，今年{age}岁")   # 我叫张三，今年25岁
```

直接在大括号里写变量名，简洁直观。还支持表达式：

```python
print(f"明年{age + 1}岁")        # 明年26岁
print(f"价格: {9.99:.2f}元")     # 价格: 9.99元（保留两位小数）
print(f"{'居中':^20}")           #        居中（宽度20，居中对齐）
```

**2. format 方法**

**语法结构：** `"文本{}文本".format(值1, 值2)`

```python
print("我叫{}，今年{}岁".format(name, age))
print("我叫{0}，{0}今年{1}岁".format(name, age))  # 可以引用同一个参数
```

**3. 百分号（老式，了解即可）**

**语法结构：** `"文本%格式符" % (值1, 值2)`

```python
print("我叫%s，今年%d岁" % (name, age))
```

日常开发中**优先用 f-string**，最简洁、最直观。

### 输出到文件

`file` 参数指定输出目标：

```python
with open("log.txt", "w") as f:
    print("记录日志", file=f)
```

## input — 输入

### 基本用法

`input()` 会暂停程序，等待用户输入并按回车，返回一个**字符串**：

**语法结构：** `变量 = input("提示语")`

```python
name = input("请输入你的名字: ")
print(f"你好, {name}")
```

括号里的字符串是提示语，会显示给用户看。

### 关键点：返回值永远是字符串

不管用户输入的是数字还是文字，`input` 返回的都是 **str 类型**：

```python
age = input("请输入年龄: ")   # 输入 25
print(type(age))              # <class 'str'>，不是 int
```

要用数字运算，必须**手动转换**：

```python
age = int(input("请输入年龄: "))    # 转成整数
price = float(input("请输入价格: "))  # 转成浮点数
```

不转换直接做数学运算会报错：

```python
age = input("请输入年龄: ")   # 输入 25
age + 1                      # TypeError: can only concatenate str
```

### 处理多输入

一行输入多个值，用 `split` 拆分：

```python
# 用户输入: 张三 25 北京
name, age, city = input("请输入姓名 年龄 城市: ").split()
```

一行输入多个数字：

```python
# 用户输入: 1 2 3 4 5
nums = list(map(int, input("请输入数字: ").split()))
```

### 输入校验

用户可能输入非法数据，配合 `try` 做容错处理：

```python
while True:
    try:
        age = int(input("请输入年龄: "))
        break
    except ValueError:
        print("请输入数字")
```

## 速查表

| 操作 | 代码 |
|---|---|
| 输出文本 | `print("hello")` |
| 输出多个值 | `print("a", "b", "c")` |
| 自定义分隔符 | `print("a", "b", sep="-")` |
| 不换行 | `print("hello", end="")` |
| 格式化输出 | `f"我叫{name}"` |
| 保留小数 | `f"{3.14159:.2f}"` |
| 接收输入 | `input("提示语")` |
| 输入转整数 | `int(input("提示语"))` |
| 一行输入多个值 | `input().split()` |
| 输入多个数字 | `list(map(int, input().split()))` |

## 两个容易踩的坑

**第一，input 返回的永远是字符串。** 需要数字时记得 `int()` 或 `float()` 转换，否则程序不会报语法错误但运行时出问题。

**第二，f-string 中的表达式可以写得很复杂但不建议。** 保持简单，复杂逻辑先算好变量再放进 f-string，代码更可读。

---

## 本仓库学习导航
对应练习： [ex01](../exercises/ex01_guess_number.py) [ex02](../exercises/ex02_calculator.py)
