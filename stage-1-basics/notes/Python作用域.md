# Python 作用域：变量在哪里能被访问

## 核心问题：变量不是哪都能用的

你定义了一个变量 `x = 10`，是不是在代码的任何地方都能访问它？不是。Python 中的变量有**可见范围**的限制——在函数内部定义的变量，函数外面拿不到；在函数外部定义的变量，函数里面能不能改？这些问题都由**作用域**来决定。

理解作用域，才能避免"变量找不到"和"变量被意外修改"这两类最常见的 bug。

## 局部作用域

在函数内部定义的变量，**只在函数内有效**，函数执行完就销毁。这叫局部变量。

语法结构：在函数体内直接赋值，变量即为局部变量

```python
# 语法
def 函数名():
    变量名 = 值   # 局部变量，函数外无法访问

# 示例
def my_func():
    name = "张三"
    age = 25
    print(name, age)

my_func()        # 张三 25
print(name)      # 报错！NameError: name 'name' is not defined
```

函数执行时创建局部变量，执行完毕后这些变量就不存在了。外部无法访问。

### 不同函数的局部变量互相独立

```python
def func_a():
    x = 10
    print(f"func_a 里 x = {x}")

def func_b():
    x = 20       # 这里的 x 和 func_a 里的 x 完全无关
    print(f"func_b 里 x = {x}")

func_a()   # func_a 里 x = 10
func_b()   # func_b 里 x = 20
```

即使名字一样，也是**两个完全独立的变量**，互不影响。

## 全局作用域

在函数外部、模块顶层定义的变量，叫全局变量。**整个文件都能读取**。

语法结构：在模块顶层（函数外）直接赋值，变量即为全局变量

```python
# 语法
变量名 = 值   # 全局变量，定义在函数外

def 函数名():
    函数体   # 可以读取全局变量

# 示例
message = "我是全局变量"

def my_func():
    print(message)   # 可以读取全局变量

my_func()   # 我是全局变量
print(message)   # 我是全局变量
```

### 函数内能读但不能直接改

函数内部可以**读取**全局变量，但如果尝试**赋值**，Python 会认为你在创建一个同名的局部变量，而不是修改全局变量：

```python
count = 0

def increment():
    count = count + 1   # 报错！UnboundLocalError

increment()
```

Python 看到 `count = ...` 就认为 `count` 是局部变量，但局部变量还没赋值就要读取，所以报错。

### global 关键字

确实需要在函数内修改全局变量时，用 `global` 声明：

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
increment()
print(count)   # 2
```

`global` 告诉 Python：这个变量用的是外层的全局变量，不是新建局部变量。

### 尽量别用 global

虽然 `global` 能用，但**不推荐**。全局变量谁都能改，代码一长就不知道哪里改了它，debug 非常痛苦。更好的做法是通过**参数传入、return 返回**：

```python
# 不推荐
count = 0

def increment():
    global count
    count += 1

# 推荐
def increment(count):
    return count + 1

count = 0
count = increment(count)   # 1
```

函数应该是**输入 → 处理 → 输出**的黑盒，不依赖外部状态，不修改外部状态。这样代码才容易理解和维护。

## 嵌套作用域

函数里面再定义函数时，内层函数可以读取外层函数的变量：

```python
def outer():
    msg = "hello"

    def inner():
        print(msg)   # 能读取外层函数的变量

    inner()

outer()   # hello
```

但如果内层函数要**修改**外层函数的变量，需要用 `nonlocal`：

语法结构：`nonlocal 变量名`

```python
# 语法
def 外层函数():
    变量名 = 值

    def 内层函数():
        nonlocal 变量名   # 声明使用外层函数的变量
        变量名 = 新值

    内层函数()

# 示例
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    inner()
    print(f"最终 count = {count}")

outer()
# 1
# 2
# 最终 count = 2
```

`nonlocal` 和 `global` 的区别：`global` 改的是模块级变量，`nonlocal` 改的是**最近一层外层函数**的变量。日常开发中 `nonlocal` 用得很少，知道有这个概念就行。

## LEGB 规则

Python 查找变量时按 **LEGB** 顺序从内到外查找：

- **L** (Local) — 当前函数内的局部变量
- **E** (Enclosing) — 外层嵌套函数的变量
- **G** (Global) — 模块级的全局变量
- **B** (Built-in) — Python 内置的名称，如 `print`、`len`、`True`

```python
x = "全局变量"

def outer():
    x = "外层函数变量"

    def inner():
        x = "内层函数变量"
        print(x)

    inner()
    print(x)

outer()
print(x)
# 内层函数变量
# 外层函数变量
# 全局变量
```

每一层优先用自己的变量，只有自己没有时才往外层找。

**别故意制造同名的嵌套变量**，代码会很混乱。不同层用不同的变量名，大家都清晰。

## 闭包

嵌套函数的一个经典应用——**内层函数记住外层函数的变量**，即使外层函数已经执行完毕：

语法结构：外层函数返回内层函数，内层函数引用外层变量

```python
# 语法
def 外层函数(参数):
    变量名 = 值

    def 内层函数():
        nonlocal 变量名   # 引用外层变量
        函数体
        return 返回值

    return 内层函数   # 返回内层函数

变量 = 外层函数(参数)   # 外层函数执行完毕，但变量被内层函数记住

# 示例
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

my_counter = make_counter()
print(my_counter())   # 1
print(my_counter())   # 2
print(my_counter())   # 3
```

`make_counter` 执行完毕后，`count` 变量本该销毁，但因为 `counter` 函数还引用着它，所以它"活"了下来。这就是**闭包**——函数携带了它定义时的环境。

闭包是进阶概念，日常开发用得不多，理解原理就行。

## 实际场景

### 避免全局变量

```python
# 不好的做法：用全局变量在函数间传递数据
user_name = ""

def set_name():
    global user_name
    user_name = "张三"

def greet():
    global user_name
    print(f"你好，{user_name}")

set_name()
greet()   # 你好，张三

# 好的做法：用参数和返回值
def set_name():
    return "张三"

def greet(name):
    print(f"你好，{name}")

name = set_name()
greet(name)   # 你好，张三
```

### 函数内的变量不要和全局同名

```python
# 容易混淆
data = [1, 2, 3]

def process():
    data = [4, 5, 6]   # 这是局部变量，和全局的 data 无关
    print(data)

process()      # [4, 5, 6]
print(data)    # [1, 2, 3]（全局变量没被修改）
```

### 配置常量可以用全局变量

不修改的全局变量是可以接受的，常用来做配置常量：

```python
MAX_RETRIES = 3
TIMEOUT = 30
DEFAULT_ENCODING = "utf-8"

def fetch_data(url):
    for i in range(MAX_RETRIES):
        # 尝试获取数据
        pass
```

只读不写的全局变量没问题，问题出在**多个函数都能修改同一个全局变量**。

## 速查表

| 概念 | 说明 |
|---|---|
| 局部变量 | 函数内定义，函数外不可见 |
| 全局变量 | 函数外定义，函数内可读 |
| `global` | 函数内声明使用全局变量 |
| `nonlocal` | 内层函数声明使用外层函数变量 |
| LEGB | 查找顺序：Local → Enclosing → Global → Built-in |
| 闭包 | 内层函数携带外层函数的变量 |

## 要点

作用域的核心就两条规则：**函数内的变量外部拿不到，函数外的变量内部能读但不能直接改**。需要改时用 `global`，但能用参数和返回值替代就别用。LEGB 是 Python 查找变量的顺序，理解了就不会对"变量怎么找到的"感到困惑。日常开发中，**尽量用参数传入、return 返回，少依赖全局变量**，代码会更清晰、更少 bug。

---

## 本课衔接

| | |
|--|--|
| **上一篇** | [Python函数.md](Python函数.md)（应已做过等级函数 ex05） |
| **下一篇** | 阶段 1 结束 → [阶段 2 入口](../../stage-2-stdlib/README.md) |
| **本篇练习** | **无独立新作业**（不链练习总表） |

**和前后的关系（重要）：**

1. 打开你写的 [ex05 等级函数作业](../exercises/ex05_refactor_functions.py)（或 [答案](../solutions/ex05_refactor_functions.py)）  
2. 想一想：`score` 是局部变量还是全局？在函数外能不能直接用？  
3. 若做过加练 [计算器](../exercises/ex02_calculator.py)，循环里的 `a`/`b` 也只在那次循环逻辑里有意义  

本篇是对「函数」的加深理解，**不另出题**；阶段 1 过关仍是：ex04、ex01、ex03、ex05。

阶段 1 做完后进入 → [stage-2-stdlib/README.md](../../stage-2-stdlib/README.md)
