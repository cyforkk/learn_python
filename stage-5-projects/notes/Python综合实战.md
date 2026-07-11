# Python 综合实战：四个项目串联全部基础

## 为什么做综合项目

前面的笔记学了文件读写、异常处理、面向对象、标准库等知识点。但这些知识点单独看是零散的，**综合项目把它们串起来用**——文件操作、数据处理、类的设计、异常处理、命令行交互，一个项目同时用上多个技能。

下面四个项目从易到难，每个都只用标准库，不需要安装第三方包。

## 一、批量重命名文件

**练习点：** pathlib、字符串方法、for 循环

### 需求

某个文件夹里有一堆图片文件，名字杂乱无章，想把它们统一重命名为 `001.jpg`、`002.jpg`、`003.jpg` 的格式。

### 代码

```python
from pathlib import Path

def batch_rename(folder, pattern="img", ext=".jpg"):
    folder = Path(folder)
    if not folder.is_dir():
        print(f"{folder} 不是有效目录")
        return

    files = sorted(folder.glob(f"*{ext}"))
    if not files:
        print(f"没有找到 {ext} 文件")
        return

    print(f"共找到 {len(files)} 个文件")
    for i, file in enumerate(files, 1):
        new_name = f"{pattern}_{i:03d}{ext}"
        new_path = file.parent / new_name
        file.rename(new_path)
        print(f"{file.name} -> {new_name}")

batch_rename("E:/photos", pattern="travel", ext=".jpg")
```

### 代码解读

`Path(folder).glob("*jpg")` 找出目录下所有 jpg 文件。`enumerate(files, 1)` 从 1 开始编号。`{i:03d}` 格式化数字为三位数，不够的前面补零（001、002、003）。`file.rename()` 重命名文件。

### 升级版：添加前缀和保留原名

```python
from pathlib import Path

def batch_rename(folder, prefix="new_"):
    folder = Path(folder)
    files = sorted(folder.iterdir())

    for file in files:
        if file.is_file():
            new_path = file.parent / f"{prefix}{file.name}"
            file.rename(new_path)
            print(f"{file.name} -> {prefix}{file.name}")

batch_rename("E:/data", prefix="processed_")
```

## 二、读 CSV 做统计后写回

**练习点：** csv 模块、数据处理、文件读写、推导式

### 需求

读取一个学生成绩 CSV 文件，计算每个学生的总分和等级，把结果写回新的 CSV 文件。

### 原始数据 students.csv

```
姓名,语文,数学,英语
张三,85,92,78
李四,70,65,80
王五,90,95,88
```

### 代码

```python
import csv
from pathlib import Path

def process_scores(input_file, output_file):
    input_file = Path(input_file)
    output_file = Path(output_file)

    # 读取数据
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

    # 处理数据
    results = []
    for s in students:
        chinese = int(s["语文"])
        math = int(s["数学"])
        english = int(s["英语"])
        total = chinese + math + english
        average = round(total / 3, 1)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        results.append({
            "姓名": s["姓名"],
            "语文": chinese,
            "数学": math,
            "英语": english,
            "总分": total,
            "平均分": average,
            "等级": grade,
        })

    # 按总分排序
    results.sort(key=lambda x: x["总分"], reverse=True)

    # 写入文件
    fieldnames = ["姓名", "语文", "数学", "英语", "总分", "平均分", "等级"]
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"处理完成，共 {len(results)} 条记录")
    print(f"结果已保存到 {output_file}")

    # 打印前三名
    print("\n前三名:")
    for i, s in enumerate(results[:3], 1):
        print(f"  {i}. {s['姓名']} - 总分{s['总分']} 平均{s['平均分']} 等级{s['等级']}")

process_scores("students.csv", "students_result.csv")
```

### 代码解读

`csv.DictReader` 读取每行为字典，`csv.DictWriter` 写入字典到 CSV。`round(total / 3, 1)` 保留一位小数。`sort(key=lambda x: x["总分"], reverse=True)` 按总分降序排列。`results[:3]` 取前三名。

### 加入异常处理

```python
import csv
from pathlib import Path

def process_scores(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            students = list(reader)
    except FileNotFoundError:
        print(f"文件 {input_file} 不存在")
        return
    except Exception as e:
        print(f"读取失败: {e}")
        return

    results = []
    for s in students:
        try:
            chinese = int(s["语文"])
            math = int(s["数学"])
            english = int(s["英语"])
        except (ValueError, KeyError) as e:
            print(f"数据格式错误: {s}，跳过")
            continue

        total = chinese + math + english
        average = round(total / 3, 1)
        grade = ("A" if average >= 90 else "B" if average >= 80
                 else "C" if average >= 60 else "D")

        results.append({
            "姓名": s["姓名"],
            "语文": chinese,
            "数学": math,
            "英语": english,
            "总分": total,
            "平均分": average,
            "等级": grade,
        })

    results.sort(key=lambda x: x["总分"], reverse=True)

    fieldnames = ["姓名", "语文", "数学", "英语", "总分", "平均分", "等级"]
    try:
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"处理完成，共 {len(results)} 条记录")
    except Exception as e:
        print(f"写入失败: {e}")

process_scores("students.csv", "students_result.csv")
```

## 三、命令行待办清单

**练习点：** json 模块、面向对象、while 循环、异常处理、sys.argv

### 需求

一个命令行待办清单工具，支持添加、查看、完成、删除任务，数据保存到 JSON 文件，下次启动能恢复。

### 代码

```python
import json
from pathlib import Path

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = Path(filename)
        self.todos = self.load()

    def load(self):
        if self.filename.exists():
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"加载失败: {e}，使用空列表")
        return []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)

    def add(self, task):
        self.todos.append({"task": task, "done": False})
        self.save()
        print(f"已添加: {task}")

    def list_all(self):
        if not self.todos:
            print("待办清单为空")
            return
        print("\n--- 待办清单 ---")
        for i, item in enumerate(self.todos, 1):
            status = "x" if item["done"] else " "
            print(f"  [{status}] {i}. {item['task']}")
        print()

    def complete(self, index):
        if 1 <= index <= len(self.todos):
            self.todos[index - 1]["done"] = True
            self.save()
            print(f"已完成: {self.todos[index - 1]['task']}")
        else:
            print("序号无效")

    def remove(self, index):
        if 1 <= index <= len(self.todos):
            removed = self.todos.pop(index - 1)
            self.save()
            print(f"已删除: {removed['task']}")
        else:
            print("序号无效")

    def clear_done(self):
        before = len(self.todos)
        self.todos = [t for t in self.todos if not t["done"]]
        after = len(self.todos)
        self.save()
        print(f"清理了 {before - after} 条已完成任务")


def main():
    todo = TodoList("todos.json")

    while True:
        print("\n1.查看  2.添加  3.完成  4.删除  5.清理已完成  6.退出")
        choice = input("选择操作: ").strip()

        if choice == "1":
            todo.list_all()
        elif choice == "2":
            task = input("输入任务: ").strip()
            if task:
                todo.add(task)
        elif choice == "3":
            todo.list_all()
            num = input("完成第几条: ").strip()
            if num.isdigit():
                todo.complete(int(num))
        elif choice == "4":
            todo.list_all()
            num = input("删除第几条: ").strip()
            if num.isdigit():
                todo.remove(int(num))
        elif choice == "5":
            todo.clear_done()
        elif choice == "6":
            print("再见")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()
```

### 代码解读

`TodoList` 类封装所有待办操作，数据用 JSON 持久化。`load()` 启动时从文件恢复，`save()` 每次操作后保存。`[x]` 表示已完成，`[ ]` 表示未完成。`clear_done()` 用列表推导式过滤掉已完成的任务。

### 运行效果

```
1.查看  2.添加  3.完成  4.删除  5.清理已完成  6.退出
选择操作: 2
输入任务: 买牛奶
已添加: 买牛奶

1.查看  2.添加  3.完成  4.删除  5.清理已完成  6.退出
选择操作: 2
输入任务: 写报告
已添加: 写报告

1.查看  2.添加  3.完成  4.删除  5.清理已完成  6.退出
选择操作: 1

--- 待办清单 ---
  [ ] 1. 买牛奶
  [ ] 2. 写报告

1.查看  2.添加  3.完成  4.删除  5.清理已完成  6.退出
选择操作: 3
完成第几条: 1
已完成: 买牛奶
```

## 四、用类建模图书管理系统

**练习点：** 面向对象、类属性、实例方法、`__str__`、列表推导式

### 需求

用类建模一个图书管理系统：有书、有用户、有借阅记录。书有书名、作者、是否借出状态；用户有姓名、已借书目；借阅时书的状态和用户的借阅列表同步更新。

### 代码

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def __str__(self):
        status = "已借出" if self.borrowed else "可借"
        return f"《{self.title}》{self.author} [{status}]"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []   # 借的书列表

    def __str__(self):
        return f"{self.name} (已借{len(self.borrowed_books)}本)"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []     # 馆藏所有书
        self.users = []     # 所有注册用户

    def add_book(self, book):
        self.books.append(book)
        print(f"入库: {book}")

    def register_user(self, user):
        self.users.append(user)
        print(f"注册用户: {user.name}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def borrow(self, user_name, book_title):
        user = self.find_user(user_name)
        book = self.find_book(book_title)

        if not user:
            print(f"用户 {user_name} 不存在")
            return
        if not book:
            print(f"图书《{book_title}》不存在")
            return
        if book.borrowed:
            print(f"《{book_title}》已被借出")
            return

        book.borrowed = True
        user.borrowed_books.append(book)
        print(f"{user.name} 借阅了 {book}")

    def return_book(self, user_name, book_title):
        user = self.find_user(user_name)
        book = self.find_book(book_title)

        if not user or not book:
            print("用户或图书不存在")
            return
        if book not in user.borrowed_books:
            print(f"{user.name} 没有借《{book_title}》")
            return

        book.borrowed = False
        user.borrowed_books.remove(book)
        print(f"{user.name} 归还了 {book}")

    def show_books(self):
        print(f"\n--- {self.name} 馆藏 ---")
        for book in self.books:
            print(f"  {book}")
        available = [b for b in self.books if not b.borrowed]
        print(f"共 {len(self.books)} 本，可借 {len(available)} 本")

    def show_user_books(self, user_name):
        user = self.find_user(user_name)
        if not user:
            print(f"用户 {user_name} 不存在")
            return
        print(f"\n{user.name} 借阅记录:")
        if not user.borrowed_books:
            print("  无借阅记录")
        for book in user.borrowed_books:
            print(f"  {book}")


# 使用
library = Library("市图书馆")

# 入库
library.add_book(Book("Python编程", "Eric Matthes", "ISBN001"))
library.add_book(Book("深入理解计算机系统", "Patterson", "ISBN002"))
library.add_book(Book("算法导论", "Cormen", "ISBN003"))

# 注册用户
library.register_user(User("张三"))
library.register_user(User("李四"))

# 借书
library.borrow("张三", "Python编程")
library.borrow("李四", "算法导论")
library.borrow("张三", "算法导论")   # 已被借出

# 查看馆藏
library.show_books()

# 查看用户借阅
library.show_user_books("张三")
library.show_user_books("李四")

# 还书
library.return_book("张三", "Python编程")
library.show_books()
```

### 运行效果

```
入库: 《Python编程》Eric Matthes [可借]
入库: 《深入理解计算机系统》Patterson [可借]
入库: 《算法导论》Cormen [可借]
注册用户: 张三
注册用户: 李四
张三 借阅了 《Python编程》Eric Matthes [已借出]
李四 借阅了 《算法导论》Cormen [已借出]
《算法导论》已被借出

--- 市图书馆 馆藏 ---
  《Python编程》Eric Matthes [已借出]
  《深入理解计算机系统》Patterson [可借]
  《算法导论》Cormen [已借出]
共 3 本，可借 1 本

张三 借阅记录:
  《Python编程》Eric Matthes [已借出]

李四 借阅记录:
  《算法导论》Cormen [已借出]

张三 归还了 《Python编程》Eric Matthes [可借]

--- 市图书馆 馆藏 ---
  《Python编程》Eric Matthes [可借]
  《深入理解计算机系统》Patterson [可借]
  《算法导论》Cormen [已借出]
共 3 本，可借 2 本
```

### 设计解读

三个类各司其职：

**Book** — 封装单本书的数据（书名、作者、ISBN、借出状态）。`__str__` 让打印时直接显示书名和状态。

**User** — 封装用户数据（姓名、已借书目列表）。

**Library** — 封装管理逻辑（入库、注册、借阅、归还、查询）。借阅时同时修改书的 `borrowed` 状态和用户的 `borrowed_books` 列表，保持数据一致。

**关键设计：** `borrow` 方法里做了三层校验——用户存在、书存在、书没被借出。任何一层不满足都不执行借阅操作，直接给用户提示。这就是面向对象的好处：数据和行为在一起，逻辑不会散落到各处。

## 四个项目的知识点对照

| 项目 | 主要知识点 |
|---|---|
| 批量重命名 | pathlib、字符串格式化、for 循环、enumerate |
| CSV 统计写回 | csv 模块、DictReader/DictWriter、排序、异常处理 |
| 命令行待办 | json 读写、面向对象、while 循环、文件持久化 |
| 图书管理 | 类设计、`__str__`、多类协作、列表推导式 |

## 要点

这四个项目的共同特点：**用类组织代码、用文件持久化数据、用异常处理防御错误、用标准库省力气**。批量重命名练的是 pathlib 和字符串处理，CSV 统计练的是数据处理和文件读写，待办清单练的是面向对象和 JSON 持久化，图书管理练的是多类协作。做完这四个项目，Python 基础的核心知识点就全用了一遍。**动手敲一遍，比看十遍文档都管用。**

---

## 本仓库学习导航
项目规格： [../exercises/](../exercises/) · 实现 [../../projects/](../../projects/)
