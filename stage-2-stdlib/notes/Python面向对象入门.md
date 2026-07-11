# Python 面向对象入门：class、__init__ 与实例方法

## 为什么需要面向对象

写函数组织代码已经不错了，但有些数据天然是**绑在一起**的。一个学生有姓名、年龄、分数，用三个变量存就散了，用字典存没有方法。**面向对象把数据和操作数据的方法打包到一个类里**，数据和行为不分离。

学生有姓名、年龄、分数，还能算等级——把这些封装成 `Student` 类，数据和行为在一起，创建多少个学生都不会乱。

## class — 定义类

### 基本结构

**语法格式：**

```python
class 类名:
    类体
```

```python
class Student:
    pass

s1 = Student()   # 创建实例
print(type(s1))  # <class '__main__.Student'>
```

`class 类名:` 定义一个类，类名**首字母大写**（Python 约定）。`Student()` 调用类创建一个实例，也叫对象。

### 类和实例的关系

**类是蓝图，实例是按蓝图造出来的具体对象。**

```python
class Student:
    pass

s1 = Student()   # 第一个学生
s2 = Student()   # 第二个学生
print(s1 is s2)  # False，两个不同的实例
```

`Student` 是类，`s1` 和 `s2` 是两个独立的实例，互不影响。

## `__init__` — 初始化方法

### 什么是 `__init__`

`__init__` 是类的**初始化方法**，在创建实例时自动调用，用来设置实例的初始数据：

**语法格式：**

```python
class 类名:
    def __init__(self, 参数1, 参数2):
        self.属性1 = 参数1
        self.属性2 = 参数2
```

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s1 = Student("张三", 25, 85)
print(s1.name)   # 张三
print(s1.age)    # 25
print(s1.score)  # 85
```

`Student("张三", 25, 85)` 做了三件事：

1. 创建一个新实例
2. 自动调用 `__init__`，把 `"张三"`、`25`、`85` 传进去
3. 把数据存到 `self` 上

### self 是什么

**`self` 就是实例本身。** `self.name = name` 的意思是"把这个实例的 name 属性设为传入的 name 值"。

```python
s1 = Student("张三", 25, 85)
s2 = Student("李四", 30, 92)

print(s1.name)   # 张三
print(s2.name)   # 李四
```

`s1` 和 `s2` 各自有独立的 `name`，因为 `__init__` 里用 `self.name = name` 给每个实例都存了一份。

**`self` 不是关键字，是约定俗成的参数名。** 调用时不需要手动传，Python 自动传入：

```python
# Python 内部做了这件事
s1 = Student.__new__(Student)
Student.__init__(s1, "张三", 25, 85)   # self 就是 s1
```

### 属性默认值

```python
class Student:
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score
        self.is_active = True   # 默认值，不需要从参数传入

s1 = Student("张三", 25)
print(s1.score)      # 0（默认值）
print(s1.is_active)  # True（默认值）
```

## 实例方法 — 操作实例数据的函数

### 基本用法

类里面定义的函数就是**方法**，第一个参数永远是 `self`：

**语法格式：**

```python
class 类名:
    def 方法名(self, 参数):
        方法体
        return 返回值
```

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"

    def introduce(self):
        return f"我叫{self.name}，{self.age}岁，成绩等级{self.get_grade()}"

s1 = Student("张三", 25, 85)
print(s1.get_grade())    # B
print(s1.introduce())   # 我叫张三，25岁，成绩等级B
```

**方法 vs 函数的区别：** 方法定义在类里面，第一个参数是 `self`，调用时 `实例.方法名()` 自动传入实例。函数是独立的，不依附于任何对象。

### 方法可以修改属性

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, bonus):
        self.score += bonus

    def reset(self):
        self.score = 0

s1 = Student("张三", 85)
print(s1.score)   # 85

s1.add_score(10)
print(s1.score)   # 95

s1.reset()
print(s1.score)   # 0
```

方法通过 `self.属性名` 读取和修改实例的数据。

### 方法之间互相调用

```python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores   # 分数列表

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_grade(self):
        avg = self.get_average()   # 用 self 调用自己的其他方法
        if avg >= 90:
            return "A"
        elif avg >= 60:
            return "B"
        else:
            return "C"

    def report(self):
        avg = self.get_average()
        grade = self.get_grade()
        return f"{self.name}：平均{avg:.1f}分，等级{grade}"

s1 = Student("张三", [85, 90, 78])
print(s1.report())   # 张三：平均84.3分，等级B
```

**方法内部用 `self.方法名()` 调用自己的其他方法。**

## 类属性 vs 实例属性

### 实例属性 — 每个实例独有

**语法格式：**

```python
class 类名:
    def __init__(self, 参数):
        self.属性名 = 值   # 实例属性
```

```python
class Student:
    def __init__(self, name):
        self.name = name   # 实例属性，每个实例不同

s1 = Student("张三")
s2 = Student("李四")
print(s1.name)   # 张三
print(s2.name)   # 李四
```

### 类属性 — 所有实例共享

**语法格式：**

```python
class 类名:
    类属性 = 值   # 类属性，所有实例共享

    def __init__(self, 参数):
        self.属性名 = 值   # 实例属性
```

```python
class Student:
    school = "北大"   # 类属性，所有实例共享

    def __init__(self, name):
        self.name = name   # 实例属性

s1 = Student("张三")
s2 = Student("李四")

print(s1.school)   # 北大
print(s2.school)   # 北大
print(Student.school)   # 北大（也可以通过类名访问）
```

**类属性放在 `__init__` 外面**，所有实例共享同一份数据。

### 实际用途：计数器

```python
class Student:
    count = 0   # 类属性，统计创建了几个学生

    def __init__(self, name):
        self.name = name
        Student.count += 1   # 每创建一个实例，计数加 1

s1 = Student("张三")
s2 = Student("李四")
s3 = Student("王五")

print(Student.count)   # 3
```

## `__str__` — 自定义打印格式

直接 print 实例会看到不好看的默认输出：

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("张三", 85)
print(s1)   # <__main__.Student object at 0x7f8b2c3d4e10>
```

定义 `__str__` 方法控制 print 输出：

**语法格式：**

```python
class 类名:
    def __str__(self):
        return 字符串
```

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student({self.name}, {self.score}分)"

s1 = Student("张三", 85)
print(s1)   # Student(张三, 85分)
```

**`__str__` 返回一个字符串**，print 实例时自动调用。让调试和输出更友好。

## 常用魔术方法一览

除了 `__init__` 和 `__str__`，还有一些常用的魔术方法，名字以双下划线开头和结尾：

| 方法 | 触发时机 | 用途 |
|---|---|---|
| `__init__` | 创建实例时 | 初始化属性 |
| `__str__` | `print(实例)` 或 `str(实例)` | 控制字符串显示 |
| `__repr__` | 调试输出 | 开发者看的详细表示 |
| `__len__` | `len(实例)` | 支持求长度 |
| `__eq__` | `实例1 == 实例2` | 支持相等比较 |
| `__lt__` | `实例1 < 实例2` | 支持大小比较 |
| `__contains__` | `x in 实例` | 支持 in 判断 |

**初学者先掌握 `__init__` 和 `__str__`**，其他的用到再查。

## 实战示例

### 学生管理

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "优秀"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def __str__(self):
        return f"{self.name}({self.age}岁, {self.score}分, {self.get_grade()})"


class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.name != name]

    def average_score(self):
        if not self.students:
            return 0
        return sum(s.score for s in self.students) / len(self.students)

    def show_all(self):
        print(f"--- {self.name} ---")
        for s in self.students:
            print(s)
        print(f"平均分: {self.average_score():.1f}")


# 使用
classroom = Classroom("三年二班")
classroom.add_student(Student("张三", 18, 85))
classroom.add_student(Student("李四", 19, 92))
classroom.add_student(Student("王五", 18, 55))

classroom.show_all()
# --- 三年二班 ---
# 张三(18岁, 85分, 及格)
# 李四(19岁, 92分, 优秀)
# 王五(18岁, 55分, 不及格)
# 平均分: 77.3

classroom.remove_student("王五")
classroom.show_all()
# --- 三年二班 ---
# 张三(18岁, 85分, 及格)
# 李四(19岁, 92分, 优秀)
# 平均分: 88.5
```

**`Student` 封装单个学生的数据和行为，`Classroom` 封装班级的管理逻辑。** 每个类各司其职，代码结构清晰。

### 银行账户

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("存款金额必须大于零")
            return
        self.balance += amount
        print(f"{self.owner} 存入 {amount}，余额 {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("取款金额必须大于零")
            return
        if amount > self.balance:
            print("余额不足")
            return
        self.balance -= amount
        print(f"{self.owner} 取出 {amount}，余额 {self.balance}")

    def __str__(self):
        return f"账户({self.owner}, 余额{self.balance})"


account = BankAccount("张三", 1000)
account.deposit(500)    # 张三 存入 500，余额 1500
account.withdraw(200)   # 张三 取出 200，余额 1300
account.withdraw(2000)  # 余额不足
print(account)          # 账户(张三, 余额1300)
```

**数据（余额）和操作（存取款）封装在一起**，外部不能直接改 balance，只能通过方法操作，逻辑可控。

## 面向对象 vs 面向过程

同一个功能，对比两种写法：

```python
# 面向过程：数据和行为分离
def create_student(name, age, score):
    return {"name": name, "age": age, "score": score}

def get_grade(student):
    if student["score"] >= 90:
        return "A"
    return "B"

s = create_student("张三", 25, 85)
print(get_grade(s))

# 面向对象：数据和行为在一起
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        return "B"

s = Student("张三", 25, 85)
print(s.get_grade())
```

面向过程用字典存数据，函数操作字典。面向对象把数据和操作绑在类里。**数据量小、逻辑简单时两种都行；数据复杂、需要复用时面向对象更清晰。**

## 速查表

| 概念 | 语法 | 说明 |
|---|---|---|
| 定义类 | `class 类名:` | 首字母大写 |
| 创建实例 | `类名(参数)` | 自动调用 `__init__` |
| 初始化方法 | `def __init__(self, ...):` | 创建实例时自动调用 |
| 实例属性 | `self.属性名 = 值` | 每个实例独有 |
| 类属性 | 在类体中直接定义 | 所有实例共享 |
| 实例方法 | `def 方法名(self, ...):` | 第一个参数是 self |
| 调用方法 | `实例.方法名()` | 自动传入实例 |
| 打印控制 | `def __str__(self):` | 控制 print 输出 |

## 要点

面向对象初学掌握：**class + `__init__` + 普通方法**。继承、多态、`__str__` 以后再深入。

---

## 本篇对应练习（最简示例 · 与仓库题一致）

必做 [ex05](../exercises/ex05_book_class.py)：

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"《{self.title}》- {self.author}, {self.pages}页"

    def is_long(self):
        return self.pages >= 300

b1 = Book("Python 入门", "张三", 200)
print(b1.info(), "长书?", b1.is_long())
```

---

## 本仓库学习导航
- **练习安排：过关** [ex05 Book 类](../exercises/ex05_book_class.py)
- 作业是最简单脚本，**不含测试代码**
