# Python 函数：从 def 到参数与返回值

## 为什么需要函数

写代码时你会发现，有些逻辑在反复出现——计算成绩等级、格式化日期、读取用户输入。如果每次都把相同的代码抄一遍，文件越来越长，改一个地方要改好几处。**函数就是把一段逻辑打包起来，取个名字，需要的时候调用它**。

函数的核心思想：**输入数据、处理数据、输出结果**。对应到代码上就是：接收参数、执行逻辑、返回结果。

## def — 定义函数

### 基本结构

语法结构：`def 函数名(参数):`

```python
# 语法
def 函数名(参数):
    函数体

# 示例
def greet(name):
    print(f"你好，{name}")

greet("张三")   # 你好，张三
```

`def` 是定义函数的关键字，后面跟函数名和圆括号里的参数，冒号下面缩进的代码块就是函数体。

### 执行逻辑

函数**定义时不执行，调用时才执行**：

```python
def say_hello():
    print("hello")

# 这里函数还没执行，只是定义了
say_hello()   # 调用时才执行，打印 hello
```

## 参数 — 函数的输入

参数是函数接收外部数据的方式。Python 的参数机制非常灵活，从简单到复杂逐步来看。

### 位置参数

最基本的参数类型，**按位置一一对应**：

语法结构：`函数名(参数1, 参数2)`

```python
# 语法
def 函数名(参数1, 参数2):
    函数体

函数名(值1, 值2)   # 按位置对应：值1→参数1，值2→参数2

# 示例
def add(a, b):
    return a + b

add(3, 5)   # 8（3 传给 a，5 传给 b）
add(5, 3)   # 8（但换位置不影响加法结果）
```

顺序很重要。`subtract(5, 3)` 得 2，`subtract(3, 5)` 得 -2，结果不同。

### 关键字参数

调用时用 `参数名=值` 的方式传递，**不需要按顺序**：

语法结构：`函数名(参数名=值)`

```python
# 语法
def 函数名(参数1, 参数2, 参数3):
    函数体

函数名(参数1=值1, 参数2=值2, 参数3=值3)   # 顺序无所谓

# 示例
def describe(name, age, city):
    print(f"{name}，{age}岁，住在{city}")

describe(name="张三", age=25, city="北京")  # 张三，25岁，住在北京
describe(city="上海", name="李四", age=30)  # 顺序无所谓
```

**位置参数和关键字参数可以混用**，但位置参数必须在前面：

```python
describe("张三", age=25, city="北京")     # 正确
describe("张三", 25, city="北京")          # 正确
describe(name="张三", 25, city="北京")     # 报错！位置参数不能在关键字参数后面
```

### 默认参数

给参数设定默认值，**调用时不传就用默认值**：

语法结构：`def 函数名(参数=默认值):`

```python
# 语法
def 函数名(参数1, 参数2=默认值):
    函数体

# 示例
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}")

greet("张三")              # 你好，张三（用默认值）
greet("张三", "嗨")        # 嗨，张三（覆盖默认值）
greet("张三", greeting="早上好")  # 早上好，张三
```

默认参数让函数更灵活——简单场景少传参数，复杂场景可以覆盖默认值。

### 默认参数的位置规则

**默认参数必须放在非默认参数后面**，否则 Python 不知道哪个参数没传：

```python
def greet(greeting="你好", name):   # 报错！默认参数不能在普通参数前面
    pass

def greet(name, greeting="你好"):   # 正确
    pass
```

### 默认参数的陷阱

**默认值用可变对象会踩坑**，这是 Python 最经典的陷阱之一：

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item("a"))   # ["a"]
print(add_item("b"))   # ["a", "b"]（不是 ["b"]！）
print(add_item("c"))   # ["a", "b", "c"]（默认列表被污染了）
```

原因：默认值在函数定义时创建一次，之后所有调用共享同一个列表。

**正确写法：** 用 `None` 作默认值，函数内部创建新对象：

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item("a"))   # ["a"]
print(add_item("b"))   # ["b"]（每次都是新列表）
```

### *args — 接收任意数量的位置参数

参数名前加 `*`，可以接收任意数量的位置参数，打包成**元组**：

语法结构：`def 函数名(*args):`

```python
# 语法
def 函数名(*args):
    函数体   # args 是元组

# 示例
def sum_all(*args):
    print(args)        # (1, 2, 3, 4)
    print(type(args))  # <class 'tuple'>
    return sum(args)

sum_all(1, 2, 3, 4)   # 10
sum_all(1, 2)         # 3
sum_all()             # 0
```

**实际用途：** `print` 函数就是用 `*args` 实现的，所以可以接收任意多个参数。

### **kwargs — 接收任意数量的关键字参数

参数名前加 `**`，接收关键字参数，打包成**字典**：

语法结构：`def 函数名(**kwargs):`

```python
# 语法
def 函数名(**kwargs):
    函数体   # kwargs 是字典

# 示例
def show_info(**kwargs):
    print(kwargs)       # {'name': '张三', 'age': 25}
    print(type(kwargs)) # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="张三", age=25, city="北京")
# name: 张三
# age: 25
# city: 北京
```

### 参数混合使用

各种参数可以组合使用，但必须遵循**固定顺序**：

```python
def func(a, b, c=10, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, 5, name="张三")
# a=1, b=2, c=3
# args=(4, 5)
# kwargs={'name': '张三'}
```

顺序：**位置参数 → 默认参数 → *args → **kwargs**。实际开发中很少全部混用，了解顺序规则就行。

### 参数解包

调用函数时，可以用 `*` 和 `**` 把可迭代对象和字典解包成参数：

语法结构：`函数名(*列表)` 或 `函数名(**字典)`

```python
# 语法
def 函数名(参数1, 参数2, 参数3):
    函数体

列表 = [值1, 值2, 值3]
函数名(*列表)        # 等价于 函数名(值1, 值2, 值3)

字典 = {"参数1": 值1, "参数2": 值2, "参数3": 值3}
函数名(**字典)       # 等价于 函数名(参数1=值1, 参数2=值2, 参数3=值3)

# 示例
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add(*nums)          # 6，等价于 add(1, 2, 3)

info = {"a": 1, "b": 2, "c": 3}
add(**info)         # 6，等价于 add(a=1, b=2, c=3)
```

## 返回值 — 函数的输出

### return

`return` 把结果交给调用者，函数到此结束：

语法结构：`return 返回值`

```python
# 语法
def 函数名(参数):
    函数体
    return 返回值

# 示例
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8
```

**没有 return 的函数返回 None：**

```python
def greet(name):
    print(f"你好，{name}")

result = greet("张三")   # 你好，张三
print(result)            # None
```

### 返回多个值

Python 函数可以返回多个值，实际返回的是**元组**，可以用多变量接收：

语法结构：`return 值1, 值2, 值3`

```python
# 语法
def 函数名(参数):
    函数体
    return 值1, 值2, 值3   # 返回元组 (值1, 值2, 值3)

变量1, 变量2, 变量3 = 函数名(参数)   # 解包赋值

# 示例
def get_user_info():
    name = "张三"
    age = 25
    city = "北京"
    return name, age, city   # 实际返回 ("张三", 25, "北京")

name, age, city = get_user_info()   # 解包赋值
print(name)   # 张三
print(age)    # 25
print(city)   # 北京
```

### return 和 print 的区别

初学者最容易混淆这两个：

```python
# print 版本
def add_print(a, b):
    print(a + b)

result = add_print(3, 5)   # 打印 8，但 result 是 None

# return 版本
def add_return(a, b):
    return a + b

result = add_return(3, 5)  # result 是 8，可以继续用
print(result * 2)          # 16
```

**print 是给人看的，return 是给程序用的。** 需要对结果做后续处理时必须用 return。

### 函数作为参数

Python 中函数是一等对象，可以作为参数传递给其他函数：

```python
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

apply(double, 5)   # 10
apply(square, 5)   # 25
```

## lambda — 匿名函数

不需要给函数取名字时，用 `lambda` 一行写完：

```python
# 普通函数
def double(x):
    return x * 2

# 等价的 lambda
double = lambda x: x * 2

double(5)   # 10
```

lambda 的语法：`lambda 参数: 表达式`，只能写一个表达式，不能写多行语句。

**实际用途：** 通常用在需要临时传一个简单函数的场景，不需要专门定义：

```python
# 按绝对值排序
nums = [3, -1, -5, 2, 4]
sorted(nums, key=lambda x: abs(x))   # [-1, 2, 3, 4, -5]

# 按字典的某个键排序
users = [{"name": "张三", "age": 25}, {"name": "李四", "age": 20}]
sorted(users, key=lambda u: u["age"])
# [{"name": "李四", "age": 20}, {"name": "张三", "age": 25}]
```

## 变量作用域

函数内部定义的变量，外部访问不到：

```python
def my_func():
    x = 10        # 局部变量
    print(x)

my_func()    # 10
print(x)     # 报错！NameError: name 'x' is not defined
```

函数内部可以**读取**外部的变量，但不能直接修改：

```python
count = 0

def increment():
    count = count + 1   # 报错！UnboundLocalError

increment()
```

需要修改外部变量时，用 `global` 关键字：

语法结构：`global 变量名`

```python
# 语法
变量名 = 值

def 函数名():
    global 变量名   # 声明使用全局变量
    变量名 = 新值

# 示例
count = 0

def increment():
    global count
    count += 1

increment()
print(count)   # 1
```

**但不推荐频繁用 global。** 更好的做法是通过参数传入、return 返回，让函数保持纯粹的输入输出。

## 实战示例

### 计算器

```python
def calculate(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "除数不能为零"
    else:
        return "不支持的操作"

print(calculate(10, 5))        # 15（默认加法）
print(calculate(10, 5, "-"))   # 5
print(calculate(10, 5, "*"))   # 50
```

### 生成用户名片

```python
def make_card(name, age, city="未知", email=None):
    card = f"""
    姓名：{name}
    年龄：{age}
    城市：{city}
    """
    if email:
        card += f"邮箱：{email}\n"
    return card

print(make_card("张三", 25))
print(make_card("李四", 30, city="上海", email="test@test.com"))
```

### 日志函数

```python
def log(message, level="INFO"):
    print(f"[{level}] {message}")

log("程序启动")              # [INFO] 程序启动
log("文件未找到", "ERROR")   # [ERROR] 文件未找到
log("操作完成", "DEBUG")     # [DEBUG] 操作完成
```

## 速查表

| 语法 | 用途 |
|---|---|
| `def func(a, b):` | 定义函数 |
| `func(1, 2)` | 位置参数调用 |
| `func(a=1, b=2)` | 关键字参数调用 |
| `def func(a, b=10):` | 默认参数 |
| `def func(*args):` | 接收任意数量位置参数 |
| `def func(**kwargs):` | 接收任意数量关键字参数 |
| `return value` | 返回值 |
| `return a, b, c` | 返回多个值（元组） |
| `lambda x: x * 2` | 匿名函数 |
| `global x` | 声明全局变量 |
| `func(*iterable)` | 可迭代对象解包成参数 |
| `func(**dict)` | 字典解包成参数 |

## 要点

函数的核心就三件事：**定义（def）、传参（位置/关键字/默认值）、返回（return）**。初学先会 `def` + 参数 + `return` 即可；`*args` / `**kwargs` / `lambda` 以后用到再查。

---

## 本仓库练习（只列题目 · 答案在链接里）

### 过关 · 成绩等级函数

**题目：**

1. 写函数 `level(score)`：≥90 返回 A，≥80 返回 B，≥60 返回 C，否则 D  
2. 对几个分数调用并打印结果  

**打开作业：** [ex05_refactor_functions.py](../exercises/ex05_refactor_functions.py)  
**参考答案（做完再看）：** [solutions/ex05_refactor_functions.py](../solutions/ex05_refactor_functions.py)

### 加练（可选）· 简易计算器

**题目：** 循环读入 `数字 运算符 数字`（如 `3 + 4`），支持 `+ - * /`，除零要提示，输入 `q` 退出。  

**打开作业：** [ex02_calculator.py](../exercises/ex02_calculator.py)  
**参考答案（做完再看）：** [solutions/ex02_calculator.py](../solutions/ex02_calculator.py)

作用域无需单独做题，读 [Python作用域.md](Python作用域.md) 即可。
