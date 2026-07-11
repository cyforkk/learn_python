# Python 实战练习：五个小项目吃透基础语法

学语法是为了用。前面学了变量、条件、循环、函数、字符串、容器，把这些组合起来能做什么？下面五个小项目从易到难，每个都只用基础语法，做完之后你对 Python 的核心概念会有完全不同的理解。

## 一、猜数字游戏

**练习点：** `input`、类型转换、`if/elif/else`、`while` 循环、`break`

### 代码

```python
import random

answer = random.randint(1, 100)
print("我想了一个 1-100 之间的数字，你来猜")

while True:
    guess = int(input("请输入你的猜测: "))

    if guess < answer:
        print("太小了")
    elif guess > answer:
        print("太大了")
    else:
        print("猜对了！")
        break
```

### 代码解读

`random.randint(1, 100)` 随机生成一个整数。`while True` 创建无限循环，直到用户猜对时用 `break` 跳出。`input` 返回的是字符串，必须用 `int()` 转成数字才能比较大小。

### 加限制次数

```python
import random

answer = random.randint(1, 100)
print("我想了一个 1-100 之间的数字，你有 5 次机会")

for attempt in range(1, 6):
    guess = int(input(f"第 {attempt} 次猜测: "))

    if guess < answer:
        print("太小了")
    elif guess > answer:
        print("太大了")
    else:
        print(f"猜对了！用了 {attempt} 次")
        break
else:
    print(f"机会用完了，答案是 {answer}")
```

`for...else` 的 else 在循环**正常结束（没被 break）**时执行，用来处理"用完所有机会还没猜对"的情况。

## 二、简单计算器

**练习点：** 函数定义、参数、返回值、`if/elif/else`、默认参数

### 代码

```python
def calculate(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "除数不能为零"
        return a / b
    else:
        return f"不支持的操作: {op}"

print(calculate(10, 5))         # 15（默认加法）
print(calculate(10, 5, "-"))    # 5
print(calculate(10, 5, "*"))    # 50
print(calculate(10, 5, "/"))    # 2.0
print(calculate(10, 0, "/"))    # 除数不能为零
```

### 代码解读

`op="+"` 是默认参数，不传第三个参数时默认做加法。每个运算符对应一个 `if` 分支，返回计算结果。除法时额外检查除数是否为零。

### 加交互循环

```python
def calculate(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "除数不能为零"
        return a / b
    else:
        return f"不支持的操作: {op}"

print("输入 q 退出")
while True:
    op = input("操作符 (+ - * /): ")
    if op == "q":
        break
    a = float(input("第一个数: "))
    b = float(input("第二个数: "))
    result = calculate(a, b, op)
    print(f"结果: {result}\n")
```

## 三、学生成绩管理

**练习点：** 字典的增删查、列表、`for` 遍历、函数、`sum` 求平均

### 代码

```python
students = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
}

# 查看所有学生
def show_all():
    print("\n--- 学生列表 ---")
    for name, score in students.items():
        print(f"{name}: {score}分")
    print()

# 添加学生
def add_student(name, score):
    students[name] = score
    print(f"已添加: {name} {score}分")

# 删除学生
def remove_student(name):
    if name in students:
        students.pop(name)
        print(f"已删除: {name}")
    else:
        print(f"没找到: {name}")

# 查找学生
def find_student(name):
    if name in students:
        print(f"{name}: {students[name]}分")
    else:
        print(f"没找到: {name}")

# 求平均分
def average():
    if not students:
        print("没有学生数据")
        return
    avg = sum(students.values()) / len(students)
    print(f"平均分: {avg:.1f}")

# 测试
show_all()
add_student("赵六", 88)
show_all()
remove_student("王五")
find_student("张三")
average()
```

### 代码解读

`students` 是全局字典，键是姓名、值是分数。每个操作封装成函数，通过参数接收数据、通过 return 返回结果。`students.items()` 遍历键值对，`students.values()` 拿所有分数，`sum()` 求和再除以人数得平均分。

### 改成交互式菜单

```python
students = {}

def show_all():
    if not students:
        print("暂无学生数据")
        return
    print("\n--- 学生列表 ---")
    for name, score in students.items():
        print(f"{name}: {score}分")

def add_student():
    name = input("姓名: ")
    score = int(input("分数: "))
    students[name] = score
    print(f"已添加: {name} {score}分")

def remove_student():
    name = input("要删除的姓名: ")
    if name in students:
        students.pop(name)
        print(f"已删除: {name}")
    else:
        print("没找到")

def average():
    if not students:
        print("没有学生数据")
        return
    avg = sum(students.values()) / len(students)
    print(f"平均分: {avg:.1f}")

while True:
    print("\n1.查看  2.添加  3.删除  4.平均分  5.退出")
    choice = input("选择操作: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        add_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average()
    elif choice == "5":
        print("再见")
        break
    else:
        print("无效选择")
```

## 四、经典小算法

### 九九乘法表

**练习点：** 嵌套 `for` 循环、`f-string` 对齐、`range`

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={j*i:<4}", end="")
    print()
```

输出：

```
1×1=1   
1×2=2   2×2=4   
1×3=3   2×3=6   3×3=9   
...
1×9=9   2×9=18  3×9=27  4×9=36  5×9=45  6×9=54  7×9=63  8×9=72  9×9=81  
```

`{j*i:<4}` 左对齐占 4 个字符宽度，`end=""` 让一行内的算式不换行，外层 `print()` 在每行末尾换行。

### 斐波那契数列

**练习点：** `while` 循环、多变量赋值

```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

`a, b = b, a + b` 是 Python 的多变量同时赋值，右边的值先全部算好再赋值，不需要临时变量。这是写斐波那契最简洁的方式。

### 质数判断

**练习点：** 函数、`for` + `else`、`range`、`break`

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出 1-50 之间所有质数
primes = [n for n in range(1, 51) if is_prime(n)]
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

**为什么只除到平方根？** 如果 n 有一个大于 `√n` 的因子，那它必然也有一个小于 `√n` 的因子。所以只需要检查到平方根就够了，大幅减少计算量。

列表推导式 `[n for n in range(1, 51) if is_prime(n)]` 一行代码完成筛选。

## 五、把重复代码改造成函数

这是实际开发中最有用的技能。看下面这段代码：

### 重构前：重复代码

```python
# 三个不同的人分别打招呼
name1 = "张三"
print(f"你好，{name1}")
print(f"你的名字有 {len(name1)} 个字")
print(f"名字的首字母是 {name1[0]}")
print("---")

name2 = "李四"
print(f"你好，{name2}")
print(f"你的名字有 {len(name2)} 个字")
print(f"名字的首字母是 {name2[0]}")
print("---")

name3 = "王五"
print(f"你好，{name3}")
print(f"你的名字有 {len(name3)} 个字")
print(f"名字的首字母是 {name3[0]}")
print("---")
```

同样的逻辑抄了三遍，如果要改格式（比如把"你好"改成"Hello"），要改三处。**这就是需要函数的信号**。

### 重构后：提取函数

```python
def show_name_info(name):
    print(f"你好，{name}")
    print(f"你的名字有 {len(name)} 个字")
    print(f"名字的首字母是 {name[0]}")
    print("---")

show_name_info("张三")
show_name_info("李四")
show_name_info("王五")
```

逻辑只写一遍，改格式只改一处，调用时只传不同的名字。

### 再进一步：批量处理

```python
def show_name_info(name):
    print(f"你好，{name}")
    print(f"你的名字有 {len(name)} 个字")
    print(f"名字的首字母是 {name[0]}")
    print("---")

names = ["张三", "李四", "王五"]
for name in names:
    show_name_info(name)
```

列表 + for 循环 + 函数，数据和行为分离，新增一个人只需要往列表加一个名字。

### 重构前后的对比

```python
# 重构前：计算三个人的 BMI
height1, weight1 = 1.75, 70
bmi1 = weight1 / (height1 ** 2)
if bmi1 < 18.5:
    status1 = "偏瘦"
elif bmi1 < 24:
    status1 = "正常"
else:
    status1 = "偏胖"
print(f"BMI: {bmi1:.1f}, 状态: {status1}")

height2, weight2 = 1.60, 55
bmi2 = weight2 / (height2 ** 2)
if bmi2 < 18.5:
    status2 = "偏瘦"
elif bmi2 < 24:
    status2 = "正常"
else:
    status2 = "偏胖"
print(f"BMI: {bmi2:.1f}, 状态: {status2}")
```

```python
# 重构后：提取函数
def calc_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "偏瘦"
    elif bmi < 24:
        status = "正常"
    else:
        status = "偏胖"
    print(f"BMI: {bmi:.1f}, 状态: {status}")

calc_bmi(1.75, 70)
calc_bmi(1.60, 55)
calc_bmi(1.80, 90)
```

### 什么时候该提取函数

**同一段代码出现两次以上**，就该提取成函数。具体信号包括：

- 复制粘贴了一段代码，只改了其中几个变量名
- 逻辑分了好几步，一个函数超过 30 行
- 给一段代码加注释才能看懂，说明这段逻辑值得独立成函数并取个好名字

提取函数的原则：**一个函数只做一件事，名字说明它做什么**。

## 五个项目的知识点对照

| 项目 | 核心练习点 |
|---|---|
| 猜数字游戏 | input、类型转换、if/elif/else、while、break、for...else |
| 简单计算器 | 函数定义、参数、默认参数、返回值、条件判断 |
| 学生成绩管理 | 字典增删查、for 遍历、sum、函数封装 |
| 九九乘法表 | 嵌套 for、f-string 对齐、range |
| 斐波那契 | while、多变量赋值、函数 |
| 质数判断 | 函数、range、数学优化、列表推导式 |
| 重构重复代码 | 识别重复、提取函数、参数化、循环调用 |

## 要点

这五个项目覆盖了 Python 基础语法的核心：**输入输出、条件判断、循环、函数、容器**。猜数字练的是流程控制，计算器练的是函数封装，成绩管理练的是字典操作，经典算法练的是循环和数学思维，重构练的是把重复代码变成可复用的函数。**动手敲一遍，比看十遍教程都有用。**
