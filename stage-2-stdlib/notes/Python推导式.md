# Python 推导式：用一行代码写出简洁逻辑

## 为什么需要推导式

Python 中创建列表、字典最常见的方式是：建空容器 → 循环 → 条件判断 → 追加。这段模式代码写多了很烦。**推导式把这几步压缩成一行**，代码更短、更清晰、运行更快。

Python 有四种推导式：**列表推导式、字典推导式、集合推导式、生成器表达式**。日常用得最多的是前两种。

## 列表推导式

### 基本语法

语法结构：`[表达式 for 变量 in 可迭代对象]`

```python
# 传统写法
squares = []
for i in range(5):
    squares.append(i ** 2)
# [0, 1, 4, 9, 16]

# 列表推导式
squares = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]
```

### 带条件筛选

语法结构：`[表达式 for 变量 in 可迭代对象 if 条件]`

**条件放在后面**，先遍历再筛选。

```python
# 传统写法
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
# [0, 2, 4, 6, 8]

# 列表推导式
evens = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
```

### 带条件表达式

语法结构：`[值A if 条件 else 值B for 变量 in 可迭代对象]`

**条件表达式放在前面**，先判断再生成值。

```python
# 偶数标记 even，奇数标记 odd
labels = ["even" if i % 2 == 0 else "odd" for i in range(5)]
# ["even", "odd", "even", "odd", "even"]

# 正负数标记
nums = [-3, 1, -5, 2, 4, -1]
labels = ["正" if n > 0 else "负" for n in nums]
# ["负", "正", "负", "正", "正", "负"]
```

### 嵌套循环

语法结构：`[表达式 for 变量1 in 可迭代对象1 for 变量2 in 可迭代对象2]`

```python
# 九九乘法表的元素
pairs = [(i, j, i*j) for i in range(1, 4) for j in range(1, 4)]
# [(1,1,1), (1,2,2), (1,3,3), (2,1,2), (2,2,4), (2,3,6), (3,1,3), (3,2,6), (3,3,9)]
```

**不推荐常用嵌套**，可读性差。两层以上的循环建议用普通 for。

### 实用示例

```python
# 字符串列表转大写
names = ["zhangsan", "lisi", "wangwu"]
upper_names = [name.upper() for name in names]
# ["ZHANGSAN", "LISI", "WANGWU"]

# 提取字典列表中的某个字段
users = [{"name": "张三", "age": 25}, {"name": "李四", "age": 30}]
names = [user["name"] for user in users]
# ["张三", "李四"]

# 过滤及格的成绩
scores = [85, 45, 92, 60, 30, 78]
passed = [s for s in scores if s >= 60]
# [85, 92, 60, 78]

# 嵌套列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 使用边界

```python
# 推导式适合简洁逻辑
squares = [i**2 for i in range(10)]   # 好

# 逻辑复杂时用普通 for 循环
result = []
for i in range(10):
    if i % 2 == 0:
        x = i * 2
        if x > 5:
            result.append(x - 1)
        else:
            result.append(x + 1)
```

**原则：一行能看懂就用推导式，看不懂就用 for 循环。** 不要为了炫技写超长推导式。

## 字典推导式

### 基本语法

语法结构：`{键表达式: 值表达式 for 变量 in 可迭代对象}`

```python
# 传统写法
squares = {}
for i in range(5):
    squares[i] = i ** 2
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 字典推导式
squares = {i: i ** 2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 带条件筛选

```python
# 只保留偶数的平方
squares = {i: i**2 for i in range(10) if i % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### 实用示例

```python
# 列表转字典（姓名:分数）
names = ["张三", "李四", "王五"]
scores = [85, 92, 78]
student_dict = {name: score for name, score in zip(names, scores)}
# {"张三": 85, "李四": 92, "王五": 78}

# 字典键值互换
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# 字典过滤（只保留分数及格的）
students = {"张三": 85, "李四": 45, "王五": 92, "赵六": 30}
passed = {name: score for name, score in students.items() if score >= 60}
# {"张三": 85, "王五": 92}

# 统计字符串长度
words = ["apple", "banana", "cherry", "date"]
lengths = {word: len(word) for word in words}
# {"apple": 5, "banana": 6, "cherry": 6, "date": 4}
```

### 字典键值互换的注意点

```python
# 键值互换时，值必须不可变且不重复
d = {"a": 1, "b": 1, "c": 2}
swapped = {v: k for k, v in d.items()}
# {1: "b", 2: "c"}
# "a" 的 1 被 "b" 的 1 覆盖了（键重复）
```

值有重复时互换会丢数据，因为字典的键不能重复。

## 集合推导式

语法结构：`{表达式 for 变量 in 可迭代对象}`（和列表推导式完全一样，只是用 `{}` 代替 `[]`）

```python
# 提取不重复的首字母
words = ["apple", "ant", "banana", "cherry", "apricot", "cat"]
first_letters = {word[0] for word in words}
# {"a", "b", "c"}

# 去重
nums = [1, 2, 2, 3, 3, 3, 4, 4]
unique = {n for n in nums}
# {1, 2, 3, 4}
```

**集合自动去重，结果无序。**

## 生成器表达式

把列表推导式的 `[]` 换成 `()` 就是生成器表达式：

语法结构：`(表达式 for 变量 in 可迭代对象)`

```python
# 列表推导式（立即创建，占内存）
squares_list = [i**2 for i in range(1000000)]
print(type(squares_list))   # <class 'list'>

# 生成器表达式（按需生成，几乎不占内存）
squares_gen = (i**2 for i in range(1000000))
print(type(squares_gen))   # <class 'generator'>
```

**列表推导式一次性创建所有元素，生成器表达式按需逐个生成。** 处理大数据量时用生成器省内存。

```python
# 生成器可以遍历
for sq in (i**2 for i in range(5)):
    print(sq)
# 0 1 4 9 16

# 用 sum 直接消费生成器
total = sum(i**2 for i in range(101))
print(total)   # 338350

# 用 list 转成列表
squares = list(i**2 for i in range(5))
# [0, 1, 4, 9, 16]
```

**sum、max、min 等函数直接接收生成器，不需要多加一层括号：**

```python
# 推荐
total = sum(i for i in range(101))

# 不推荐
total = sum([i for i in range(101)])   # 多了括号和内存
```

## 推导式 vs for 循环

### 什么时候用推导式

```python
# 创建新列表 → 推导式
squares = [i**2 for i in range(10)]

# 过滤筛选 → 推导式
evens = [i for i in nums if i % 2 == 0]

# 转换数据 → 推导式
upper_names = [name.upper() for name in names]
```

### 什么时候用 for 循环

```python
# 修改原列表 → for 循环
for i in range(len(nums)):
    nums[i] *= 2

# 复杂逻辑 → for 循环
result = []
for i in range(10):
    x = process(i)
    if validate(x):
        result.append(transform(x))

# 有副作用（打印、写文件等）→ for 循环
for name in names:
    print(name)   # 不要写成 [print(name) for name in names]
```

**推导式用于创建新数据，for 循环用于副作用操作。** 用推导式去 print 是 Python 中的反模式。

## 常见误区

### 推导式不是万能的

```python
# 看不懂的推导式（不要这样写）
result = [x if x > 0 else -x for x in [int(s) for s in text.split() if s.isdigit()] if x != 0]

# 拆成普通循环更清晰
result = []
for s in text.split():
    if s.isdigit():
        x = int(s)
        if x != 0:
            result.append(x if x > 0 else -x)
```

**超过一层嵌套的推导式就该拆成循环。** 简洁不等于难懂。

### 不要用推导式做副作用

```python
# 不推荐
results = [process(item) for item in data]

# 如果 process 函数只是执行操作、不返回值
# 这会创建一个全为 None 的列表，浪费内存

# 推荐
for item in data:
    process(item)
```

**推导式的目的是生成数据，不是执行操作。**

## 速查表

| 类型 | 语法 | 用途 |
|---|---|---|
| 列表推导式 | `[expr for x in iter]` | 创建新列表 |
| 列表筛选 | `[expr for x in iter if cond]` | 筛选后创建列表 |
| 字典推导式 | `{k: v for x in iter}` | 创建新字典 |
| 集合推导式 | `{expr for x in iter}` | 创建去重集合 |
| 生成器表达式 | `(expr for x in iter)` | 按需生成，省内存 |

## 要点

推导式的核心就一句话：**把"循环创建新容器"压缩成一行**。列表推导式用 `[]`，字典推导式用 `{}`，生成器表达式用 `()`。带条件筛选时 `if` 放后面，带条件取值时 `if-else` 放前面。能用推导式的就用，简洁可读；逻辑复杂的拆成 for 循环，不要为了短而牺牲清晰度。处理大数据量用生成器表达式省内存，配合 `sum`、`max` 等函数使用最舒服。

---

## 本仓库学习导航
- **练习安排：无独立练习**（了解写法即可，代码里见到能读懂）
