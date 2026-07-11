# Python 条件与循环：控制程序流向的两种方式

程序默认从上到下一行行执行。但现实中的逻辑往往需要**根据条件做不同的事**，或者**重复执行某段代码**。条件语句和循环语句就是用来改变程序执行顺序的。

## if / elif / else — 条件判断

### 基本结构

**语法：**

```python
if 条件:
    代码块
elif 条件:
    代码块
else:
    代码块
```

```python
age = 18

if age >= 18:
    print("成年")
elif age >= 12:
    print("青少年")
else:
    print("儿童")
```

`if` 是入口条件，`elif` 是中间分支（可以有多个），`else` 是以上都不满足时的兜底分支。

**注意缩进：** Python 用缩进（4 个空格）表示代码块，不靠大括号。缩进错了程序就跑不对。

### 单个 if

不需要 else 时可以只写 if：

**语法：**

```python
if 条件:
    代码块
```

```python
if score >= 60:
    print("及格了")
```

### 多个 elif

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

条件从上往下依次判断，**一旦某个条件满足，后面的都不再执行**。所以顺序很重要，大的条件写前面。

### 条件嵌套

**语法：**

```python
if 外层条件:
    if 内层条件:
        代码块
    else:
        代码块
else:
    代码块
```

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以进场")
    else:
        print("需要买票")
else:
    print("未成年人不能进入")
```

嵌套层数不要太多，超过三层就该考虑重构逻辑了。

### 三元表达式 — 一行 if-else

其他语言叫三元运算符（如 `条件 ? A : B`），Python 的写法不同，语法是**值A if 条件 else 值B**：

```python
# 传统 if-else 赋值
if score >= 60:
    result = "及格"
else:
    result = "不及格"

# 三元表达式（一行搞定）
result = "及格" if score >= 60 else "不及格"
```

**执行逻辑：** 条件为 True 返回前面的值，False 返回后面的值。

#### 基本用法

```python
# 判断奇偶
num = 7
label = "奇数" if num % 2 != 0 else "偶数"
print(label)   # 奇数

# 设置默认值
name = input("姓名: ") or "匿名"
age = int(input("年龄: "))
status = "成年" if age >= 18 else "未成年"
print(f"{name} 是 {status}")

# 返回不同的值
def get_discount(is_vip):
    return 0.8 if is_vip else 1.0

print(get_discount(True))   # 0.8
print(get_discount(False))  # 1.0
```

#### 在列表推导式中使用

三元表达式在列表推导式里特别有用，对每个元素做条件判断：

```python
scores = [85, 45, 92, 60, 30, 78]

# 给每个分数标记及格/不及格
labels = ["及格" if s >= 60 else "不及格" for s in scores]
print(labels)
# ['及格', '不及格', '及格', '及格', '不及格', '及格']

# 正数保留，负数取绝对值
nums = [3, -1, 4, -5, 2]
processed = [n if n > 0 else -n for n in nums]
print(processed)
# [3, 1, 4, 5, 2]
```

#### 在函数返回值中使用

```python
# 一行返回不同值
def check_age(age):
    return "可以进入" if age >= 18 else "禁止进入"

# 配合 print
print("通过" if score >= 60 else "不通过")

# 配合变量赋值
level = "高" if score >= 90 else "中" if score >= 60 else "低"
# 等价于：
# if score >= 90:
#     level = "高"
# elif score >= 60:
#     level = "中"
# else:
#     level = "低"
```

#### 嵌套三元表达式

三元表达式可以嵌套，模拟 if-elif-else：

```python
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 60 else "F"
print(grade)   # B
```

**但不推荐嵌套多层**，超过两层可读性急剧下降，不如用普通 if-elif-else：

```python
# 不推荐：太长，难读
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# 推荐：清晰明了
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

#### 三元表达式 vs if-else 语句

| 特性 | 三元表达式 | if-else 语句 |
|---|---|---|
| 返回值 | 有返回值 | 无返回值 |
| 使用场景 | 赋值、return、print | 复杂逻辑、多行代码 |
| 可读性 | 简单判断时更简洁 | 复杂逻辑时更清晰 |
| 嵌套 | 可以但不推荐超过两层 | elif 处理多分支更好 |

**判断标准：** 一眼能看懂的三元表达式就用，看不懂就改回 if-else。三元表达式的价值在于**简洁**，不在于炫技。

#### 与其他语言的对比

其他语言的三元运算符是 `条件 ? 值A : 值B`：

```javascript
// JavaScript
result = score >= 60 ? "及格" : "不及格"
```

```python
# Python
result = "及格" if score >= 60 else "不及格"
```

Python 的写法更接近自然语言，但顺序和传统三元运算符**反过来**了：先写值，再写条件。初学者注意别搞混。

### match-case（Python 3.10+）

Python 3.10 引入了类似其他语言 switch-case 的语法：

**语法：**

```python
match 值:
    case 模式1:
        代码块
    case 模式2:
        代码块
    case _:
        代码块    # 通配符，匹配其他所有情况
```

```python
command = "start"

match command:
    case "start":
        print("启动")
    case "stop":
        print("停止")
    case "restart":
        print("重启")
    case _:
        print("未知命令")
```

`_` 是通配符，匹配所有其他情况，相当于 else。低版本 Python 不支持，老项目里用 if-elif 就行。

## for — 遍历循环

### 基本结构

`for` 用来遍历**可迭代对象**（列表、字符串、字典、range 等）中的每个元素：

**语法：**

```python
for 变量 in 可迭代对象:
    代码块
```

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
```

### range — 生成数字序列

不需要列表，只是想重复执行 N 次，用 `range`：

```python
for i in range(5):        # 0 1 2 3 4
    print(i)

for i in range(1, 6):    # 1 2 3 4 5（左闭右开）
    print(i)

for i in range(0, 10, 2): # 0 2 4 6 8（步长为 2）
    print(i)
```

**range 不是列表**，它是按需生成数字的对象，几乎不占内存，可以直接用于循环。

#### 三种形式

`range` 接受一到三个参数，对应三种用法：

```python
# 形式一：range(stop) — 从 0 开始，到 stop-1 结束
range(5)        # 0, 1, 2, 3, 4

# 形式二：range(start, stop) — 从 start 开始，到 stop-1 结束
range(2, 8)     # 2, 3, 4, 5, 6, 7

# 形式三：range(start, stop, step) — 指定步长
range(1, 10, 3) # 1, 4, 7
```

**核心规律：左闭右开**——包含 start，不包含 stop。这和切片、列表索引的规则一致，记住一个规律就行。

#### 步长为负数 — 反向生成

步长可以是负数，此时 start 必须大于 stop 才能生成序列：

```python
# 从大到小
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
    print(i)

# 倒计时
for i in range(3, -1, -1):  # 3, 2, 1, 0
    print(i)
```

**注意：** `range(5, 0, -1)` 生成 5 到 1，不包含 0。仍然遵守左闭右开——这里 start=5 在左，stop=0 在右，步长为负所以往左走，到 0 之前停。

#### range 是惰性序列

range 对象**不会一次性生成所有数字**，而是按需计算：

```python
r = range(1000000)  # 不会占用内存来存一百万个数字
print(r)            # range(0, 1000000)

# 迭代时才逐个生成
for i in r:
    if i >= 5:
        break
    print(i)        # 0 1 2 3 4
```

对比一下，如果用列表存一百万个数字：

```python
nums = list(range(1000000))  # 真的在内存里放了一百万个 int
```

**range 几乎不占内存**，而等价的列表要占几十 MB。所以循环计数时永远用 `range`，不要先 `list(range(n))` 再遍历。

#### 转成列表查看内容

range 对象不能直接打印出所有数字，需要用 `list()` 转换才能看到：

```python
print(range(5))          # range(0, 5)，看不到具体数字
print(list(range(5)))    # [0, 1, 2, 3, 4]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
```

调试时用 `list()` 看内容，正式循环时直接用 range 对象。

#### range 支持 in 判断和索引

range 对象虽然不存数据，但支持成员判断和索引访问：

```python
r = range(10)

# 判断某个数是否在范围内
print(5 in r)     # True
print(15 in r)    # False

# 索引访问（不生成整个列表）
print(r[3])       # 3
print(r[-1])      # 9（支持负索引）

# 切片返回 range 对象，不是 list
print(r[0:3])     # range(0, 3)
```

#### 常见用例

```python
# 重复执行 N 次（不需要用到计数值）
for _ in range(5):
    print("Hello")    # 打印 5 次

# 生成下标序列遍历列表
names = ["张三", "李四", "王五"]
for i in range(len(names)):
    print(f"{i}: {names[i]}")
# 不过这种写法不如 enumerate 简洁，优先用 enumerate

# 按固定步长遍历
for i in range(0, 100, 10):
    print(i)    # 0 10 20 30 ... 90

# 倒序遍历列表
names = ["张三", "李四", "王五"]
for i in range(len(names) - 1, -1, -1):
    print(names[i])
# 王五 李四 张三
# 但更 Pythonic 的写法是 reversed(names) 或 names[::-1]
```

#### 常见陷阱

```python
# 陷阱一：以为 range 会包含终点
for i in range(1, 5):
    print(i)    # 1 2 3 4，不包含 5

# 陷阱二：步长为 0 会报错
# range(0, 10, 0)  → ValueError: range() arg 3 must not be zero

# 陷阱三：方向搞反了，结果为空
list(range(5, 1))       # []，start < stop 但没指定负步长
list(range(1, 5, -1))   # []，start < stop 但步长为负
```

**规则：** 步长为正，start 必须小于 stop；步长为负，start 必须大于 stop。方向不匹配就生成空序列，不会报错但也不会循环。

#### range vs 列表

| 特性 | range | list |
|---|---|---|
| 内存占用 | 几乎为零 | 与元素数量成正比 |
| 生成方式 | 按需计算，惰性求值 | 一次性创建所有元素 |
| 可变性 | 不可变 | 可变 |
| 支持索引 | 是 | 是 |
| 支持切片 | 返回 range | 返回 list |
| 适用场景 | 循环计数、数字序列 | 需要增删改、随机访问 |

**记住一个原则：** 只需要数字序列做循环计数时，永远用 `range`，不要转成 `list`。

### 遍历字符串

```python
for char in "hello":
    print(char)
# h e l l o
```

### 遍历字典

**语法：**

```python
# 遍历键
for 键 in 字典:
    代码块

# 遍历键值对
for 键, 值 in 字典.items():
    代码块
```

```python
person = {"name": "张三", "age": 25, "city": "北京"}

# 遍历键
for key in person:
    print(key)               # name, age, city

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")
# name: 张三
# age: 25
# city: 北京
```

### enumerate — 同时拿索引和值

**语法：**

```python
for 索引, 值 in enumerate(可迭代对象):
    代码块
```

`enumerate` 接受任何**可迭代对象**（列表、元组、字符串、字典、文件等），不局限于序列。

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

**非常实用。** 需要索引时不要写 `for i in range(len(fruits))`，用 `enumerate` 更 Pythonic。

### zip — 同时遍历多个可迭代对象

**语法：**

```python
for 值1, 值2 in zip(可迭代对象1, 可迭代对象2):
    代码块
```

```python
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name}: {age}岁")
# 张三: 25岁
# 李四: 30岁
# 王五: 28岁
```

## while — 条件循环

### 基本结构

`while` 在条件为 True 时**反复执行**，直到条件变为 False：

**语法：**

```python
while 条件:
    代码块
```

```python
count = 0
while count < 5:
    print(count)
    count += 1
# 0 1 2 3 4
```

**关键：** 循环体内必须有改变条件的操作，否则会变成**死循环**。上面的例子如果忘写 `count += 1`，程序会一直打印 0。

### 死循环的正确写法

需要持续运行直到某个条件触发退出时，用 `while True` 配合 `break`：

**语法：**

```python
while True:
    if 退出条件:
        break
    代码块
```

```python
while True:
    command = input("输入命令（quit 退出）: ")
    if command == "quit":
        break
    print(f"执行: {command}")
```

### for 和 while 怎么选

**知道循环次数** → 用 `for`。遍历列表、重复 N 次，都是 for 的主场。

**不知道循环次数** → 用 `while`。比如等待用户输入、等待网络响应、轮询状态。

能用 for 解决的优先用 for，更简洁不容易出错。

## break 和 continue — 循环控制

### break — 直接跳出循环

**语法：**

```python
for 变量 in 可迭代对象:
    if 退出条件:
        break
    代码块
```

```python
# 找到第一个偶数就停止
for num in [1, 3, 5, 4, 7, 8]:
    if num % 2 == 0:
        print(f"找到偶数: {num}")
        break
# 找到偶数: 4
```

break 跳出**当前这一层**循环，不执行循环剩余部分。

### continue — 跳过本次，继续下一次

**语法：**

```python
for 变量 in 可迭代对象:
    if 跳过条件:
        continue
    代码块
```

```python
# 只打印奇数
for num in range(10):
    if num % 2 == 0:
        continue    # 跳过偶数，直接进入下一次循环
    print(num)
# 1 3 5 7 9
```

continue 不跳出循环，只是**跳过这一轮剩下的代码**，直接进入下一轮。

### break 和 continue 的区别

```python
# break：找到 3 就不循环了
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)
# 1 2

# continue：跳过 3，继续后面的
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue
    print(i)
# 1 2 4 5
```

### 嵌套循环中的 break

break 只跳出**最内层**循环：

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}")
# i=0, j=0
# i=1, j=0
# i=2, j=0
```

外层循环不受内层 break 影响。如果需要一次跳出多层循环，用标志位或 `return`（在函数中）。

## for-else 和 while-else

Python 独有的语法：循环正常结束（没有被 break 跳出）时执行 else 块：

**语法：**

```python
for 变量 in 可迭代对象:
    if 退出条件:
        break
else:
    代码块    # 循环正常结束（未被 break）时执行
```

```python
# 查找列表中是否有负数
nums = [1, 2, 3, 4]

for num in nums:
    if num < 0:
        print("发现负数")
        break
else:
    print("没有负数")   # 循环正常结束，执行这里
# 没有负数
```

**如果被 break 了，else 不执行。** 这个语法不常用，但在查找场景下很优雅。

## 实战示例

### 成绩分级

```python
score = int(input("请输入分数: "))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 循环 + 分支（示意，不是作业答案）

```python
# 比较大小时常用这种分支
if guess < answer:
    print("太小了")
elif guess > answer:
    print("太大了")
else:
    print("猜对了")
```

### 嵌套 for（示意，不是作业答案）

```python
# 外层控制「行」，内层控制「这一行打印几次」
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

完整猜数字、九九表请自己做仓库练习，不要在这里抄答案。

### 计算 1-100 中所有偶数的和

```python
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue    # 跳过奇数
    total += i
print(total)    # 2550
```

## 速查表

| 语法 | 用途 |
|---|---|
| `if` / `elif` / `else` | 条件判断，多分支选择 |
| `for item in iterable` | 遍历可迭代对象 |
| `for i in range(n)` | 重复执行 n 次 |
| `enumerate(items)` | 同时拿索引和值 |
| `zip(a, b)` | 同时遍历多个可迭代对象 |
| `while condition` | 条件为 True 时循环 |
| `while True + break` | 死循环配合退出条件 |
| `break` | 跳出当前循环 |
| `continue` | 跳过本次，进入下一次 |
| `for ... else` | 循环正常结束（未被 break）时执行 |

## 要点

条件判断的核心是**根据不同情况走不同分支**，循环的核心是**重复执行某段逻辑**。掌握 `if-elif-else` 的多分支、`for` 遍历各种容器、`while` 做条件循环、`break` 和 `continue` 控制循环流程，日常编程 80% 以上的逻辑都能覆盖。嵌套循环和 for-else 用得少，知道有这些写法，需要时查文档即可。

---

## 本仓库练习（只列题目 · 答案在链接里）

> 下面**不贴答案代码**。点开链接自己写；做完再看 `solutions/`。

### 过关 1 · 九九乘法表（建议先做）

**题目：**

1. 用两层 `for` 打印下三角九九表（1×1、到 9×9）  
2. 不要手写 81 行 `print`  

**打开作业（自己写）：** [ex04_multiplication_table.py](../exercises/ex04_multiplication_table.py)  
**参考答案（做完再看）：** [solutions/ex04_multiplication_table.py](../solutions/ex04_multiplication_table.py)

### 过关 2 · 猜数字

**题目：**

1. 随机生成 1～100 的整数  
2. 最多猜 7 次；每次提示太大 / 太小 / 猜对  
3. 猜对提前结束；7 次都错则公布答案  

**打开作业（自己写）：** [ex01_guess_number.py](../exercises/ex01_guess_number.py)  
**参考答案（做完再看）：** [solutions/ex01_guess_number.py](../solutions/ex01_guess_number.py)

新手说明：[../exercises/新手怎么做.md](../exercises/新手怎么做.md)
