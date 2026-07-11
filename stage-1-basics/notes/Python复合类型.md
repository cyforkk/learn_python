# Python 复合类型：容器详解

基本类型（int、float、str、bool）一个变量只存一个值。但现实中的数据往往是**一组值**——一个班的学生名单、一个用户的个人信息、一组不重复的标签。Python 用四种容器类型来处理这些场景：**list、tuple、dict、set**。

理解容器的关键在三个维度：**是否有序**（能不能按位置访问）、**是否可变**（能不能增删改）、**是否允许重复**。

## list — 列表

### 是什么

**有序、可变**的序列容器，用方括号 `[]` 表示。可以存放任意类型的元素，不同类型也可以混在一起。

语法结构：`列表名 = [元素1, 元素2, ...]`

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]  # 混合类型也可以
```

### 增删改

语法结构：

```python
列表.append(元素)         # 末尾添加
列表.insert(位置, 元素)    # 指定位置插入
列表.extend(可迭代对象)    # 追加多个元素
列表.remove(值)           # 按值删除
列表.pop()               # 弹出末尾元素
```

```python
fruits = ["apple", "banana", "cherry"]

# 增
fruits.append("orange")        # 末尾添加 → ["apple", "banana", "cherry", "orange"]
fruits.insert(1, "pear")      # 在位置1插入 → ["apple", "pear", "banana", "cherry", "orange"]
fruits.extend(["grape", "kiwi"])  # 合并另一个列表

# 删
fruits.remove("banana")       # 按值删除
del fruits[0]                  # 按位置删除
popped = fruits.pop()         # 弹出末尾元素并返回它

# 改
fruits[0] = "mango"           # 按索引直接赋值
```

### 查

语法结构：`列表[索引]` 索引访问，`列表[开始:结束:步长]` 切片（左闭右开）

```python
fruits = ["apple", "banana", "cherry"]

fruits[0]        # 索引访问 → "apple"
fruits[-1]       # 负索引从末尾算 → "cherry"
fruits[0:2]      # 切片，左闭右开 → ["apple", "banana"]
"banana" in fruits  # 成员判断 → True
len(fruits)      # 长度 → 3
fruits.index("banana")  # 查位置 → 1
fruits.count("apple")  # 统计出现次数 → 1
```

### 排序与反转

语法结构：`列表.sort()` 原地排序，`sorted(可迭代对象)` 返回新列表

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()           # 原地排序 → [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)  # 降序 → [9, 6, 5, 4, 3, 2, 1, 1]
nums.reverse()        # 原地反转
sorted(nums)          # 返回新列表，不修改原列表
```

**`sort()` 修改原列表，`sorted()` 返回新列表。** 这是个重要区别。

### 列表推导式

Python 中创建列表的**简洁写法**，实际开发中极常用：

```python
# 传统写法
squares = []
for i in range(5):
    squares.append(i ** 2)

# 列表推导式
squares = [i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]

# 带条件
evens = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]
```

### 什么时候用 list

需要**按顺序存储、需要增删改、允许重复元素**的场景。这是 Python 中使用频率最高的容器。

## tuple — 元组

### 是什么

**有序、不可变**的序列容器，用圆括号 `()` 表示。创建后不能增删改元素。

语法结构：`变量名 = (元素1, 元素2, ...)`（单元素元组需加逗号 `(元素,)`）

```python
point = (3, 5)
rgb = (255, 128, 0)
single = (42,)   # 单元素元组，注意逗号不能少
```

### 能做什么

因为不可变，所以**没有 append、remove、sort 等修改方法**。但支持索引访问、切片、成员判断、len：

```python
point[0]          # 3
point[1]          # 5
point[0:2]        # (3, 5)
3 in point        # True
len(point)        # 2
```

### 解包

元组最常用的特性之一，把元素一次性赋给多个变量，语法结构：`变量1, 变量2 = 元组`

```python
point = (3, 5)
x, y = point      # x=3, y=5

# 交换两个变量不需要临时变量
a, b = b, a
```

### 什么时候用 tuple

**数据不应该被修改**的场景：坐标、RGB 颜色值、日期、配置常量。比列表占用内存更少、访问速度更快。

当你写 `return a, b, c` 时，Python 实际返回的就是一个元组。

## dict — 字典

### 是什么

**键值对**结构，用花括号 `{}` 表示。每个元素是一个 `key: value` 对，通过键快速查找对应的值。

语法结构：`字典名 = {键1: 值1, 键2: 值2, ...}`

```python
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}
```

### 增删改查

语法结构：

```python
字典[键]              # 查（键不存在会报错）
字典.get(键, 默认值)   # 查（键不存在返回默认值）
字典[键] = 值         # 增 / 改
del 字典[键]          # 删
字典.pop(键)          # 删并返回值
```

```python
# 查
person["name"]          # "张三"
person.get("email", "未填写")  # 键不存在时返回默认值，不会报错

# 增 / 改
person["email"] = "test@test.com"   # 键不存在则新增
person["age"] = 26                  # 键已存在则修改

# 删
del person["city"]                  # 按键删除
person.pop("email")                # 删除并返回值

# 判断键是否存在
"name" in person    # True
```

### 遍历

语法结构：`for 键, 值 in 字典.items():` 遍历键值对，`for 值 in 字典.values():` 遍历值，`for 键 in 字典:` 遍历键

```python
# 遍历键
for key in person:
    print(key)

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")

# 只遍历值
for value in person.values():
    print(value)
```

### 字典推导式

和列表推导式类似，用来快速创建字典：

```python
# 根据列表创建字典
names = ["张三", "李四", "王五"]
name_dict = {name: len(name) for name in names}
# {"张三": 2, "李四": 2, "王五": 2}
```

### 键的要求

键必须是**可哈希类型**：int、float、str、tuple 都行。list、dict、set 不能做键，因为它们不可哈希。

### 什么时候用 dict

需要**通过键快速查找值**的场景。比如用户信息、配置项、计数统计、缓存。字典的查找速度接近 O(1)，是 Python 中最高频使用的数据结构之一。

## set — 集合

### 是什么

**无序、不重复**的元素集合，用花括号 `{}` 表示。注意：空集合只能用 `set()` 创建，`{}` 表示的是空字典。

语法结构：`集合名 = {元素1, 元素2, ...}`，空集合用 `set()`

```python
tags = {"python", "django", "flask"}
empty = set()   # 不能写 {}，那是空字典
```

### 增删

语法结构：`集合.add(元素)` 添加，`集合.remove(值)` 删除（不存在报错），`集合.discard(值)` 删除（不存在不报错）

```python
tags.add("fastapi")      # 添加
tags.remove("flask")      # 删除，不存在会报错
tags.discard("flask")     # 删除，不存在不报错
tags.pop()                # 随机弹出一个元素
tags.clear()              # 清空
```

### 集合运算

这是 set 最独特的功能，直接支持数学集合运算，语法结构：`集合1 & 集合2` 交集，`集合1 | 集合2` 并集，`集合1 - 集合2` 差集，`集合1 ^ 集合2` 对称差

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b    # 交集 → {3, 4}
a | b    # 并集 → {1, 2, 3, 4, 5, 6}
a - b    # 差集 → {1, 2}
a ^ b    # 对称差 → {1, 2, 5, 6}
```

### 最常见用途：去重

```python
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))   # [1, 2, 3, 4]
```

一行代码去掉列表中的重复元素。

### 什么时候用 set

需要**去重**、需要**集合运算**（交集、并集、差集）、只关心**元素是否存在**而不关心顺序的场景。

## 四种容器对比

| | list | tuple | dict | set |
|---|---|---|---|---|
| **有序** | 是 | 是 | 是（3.7+ 保持插入顺序） | 否 |
| **可变** | 是 | 否 | 是 | 是 |
| **允许重复** | 是 | 是 | 键不允许 | 否 |
| **符号** | `[]` | `()` | `{key: value}` | `{}` |
| **按什么访问** | 索引 | 索引 | 键 | 不支持索引 |
| **典型用途** | 通用序列 | 固定数据 | 键值映射 | 去重、集合运算 |

## 怎么选

**存一组有序数据，需要增删改 → list**
**存一组固定不变的数据 → tuple**
**通过名字查值 → dict**
**去重或做集合运算 → set**

实际开发中，list 和 dict 用得最多，占日常 80% 以上的场景。tuple 和 set 在特定场景下才用，但用对了能让代码简洁很多。

---

## 本仓库学习导航
- **练习安排**
  - **必做** [ex03 成绩统计](../exercises/ex03_score_stats.py)
  - **选做** [ex06 通讯录](../exercises/ex06_contacts.py)
- 须先读完本篇再做；不要在「基本数据类型」篇后硬做
