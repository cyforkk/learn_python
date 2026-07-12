# Python 调试：断点与 pdb

代码写完不等于写对。程序运行结果和预期不符时，靠 `print` 到处插旗子效率太低。**调试工具让你在程序运行过程中暂停、查看变量、逐步执行**，精准定位问题出在哪一行。

Python 调试主要有两种方式：**用编辑器的图形化断点**（VS Code / PyCharm）和**用内置的 pdb 命令行调试器**。两者原理相同，都是让程序在指定位置停下来，区别只是交互方式。

## 核心概念：断点

**断点**是你在代码中标记的一个位置，程序执行到这里会暂停。暂停后你可以：

- 查看当前所有变量的值
- 逐行执行后续代码，观察每一步的变化
- 调用函数、执行表达式，验证假设

断点是调试的基础，所有调试工具都围绕它工作。

## VS Code 断点调试

VS Code 是最流行的 Python 编辑器，调试体验最好。用之前需要安装 Python 扩展（Python extension）。

### 设置断点

在代码行号左边点击，出现红点就是断点：

```python
def calculate_total(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate        # ← 在这行左边点一下，加红点
    total = subtotal + tax
    return total

result = calculate_total([10, 20, 30], 0.1)
print(result)
```

在 `tax = subtotal * tax_rate` 这行加断点，程序运行到这里会暂停。

### 启动调试

**语法结构：** 按 `F5` 启动调试（或点击侧栏 Run and Debug 面板的绿色播放按钮）

第一次按 F5 会让你选择调试配置，选 "Python File" 即可。之后直接 F5 就能启动当前文件的调试。

### 调试界面

程序暂停后，VS Code 界面会显示以下面板：

**变量面板（Variables）** — 查看当前所有局部变量和全局变量的值。可以展开复杂数据结构（列表、字典、对象）查看内部。

**监视面板（Watch）** — 手动添加要监视的表达式。比如添加 `tax_rate * 100`，实时显示计算结果。

**调用堆栈面板（Call Stack）** — 显示当前执行到哪一层函数，点击可以跳到上一层函数查看。

**断点面板（Breakpoints）** — 管理所有断点，可以启用/禁用单个断点。

### 逐步执行

程序暂停后，控制栏有四个核心按钮：

| 按钮 | 快捷键 | 作用 |
|---|---|---|
| 继续 | `F5` | 继续运行到下一个断点 |
| 单步跳过 | `F10` | 执行当前行，停在下一行 |
| 单步进入 | `F11` | 如果当前行调用了函数，进入函数内部 |
| 单步跳出 | `Shift+F11` | 从当前函数跳出，回到调用处 |

**单步跳过和单步进入的区别：**

```python
def validate(score):
    if score < 0:
        raise ValueError("分数不能为负数")
    return score

def process(scores):
    for s in scores:
        result = validate(s)    # ← 停在这里
        print(result)
```

停在 `validate(s)` 这行时：
- 按 `F10`（跳过）：执行完 `validate(s)`，停到 `print(result)` 这行。不进入 validate 内部。
- 按 `F11`（进入）：跳进 validate 函数内部，停到 `if score < 0` 这行。

**经验：** 大部分时候用 `F10` 逐行执行。只有怀疑被调用的函数有问题时，才用 `F11` 进去看。

### 条件断点

右键点击行号旁的红点，选择 "Edit Breakpoint"，可以设置条件：

```python
for i in range(10000):
    result = process(data[i])    # ← 加条件断点：i == 5000
    save(result)
```

设置条件 `i == 5000`，程序只在循环到第 5000 次时才暂停。**循环几千次才出问题时，条件断点非常实用。**

### 日志断点

右键断点，选择 "Edit Breakpoint"，将类型改为 "Log Message"。程序经过这行时会输出一条日志，**不暂停**，继续运行。

适合在不打断程序运行的情况下，记录某些关键变量的值。比 `print` 灵活，调试完直接删断点，不用清理代码。

## pdb — 命令行调试器

没有 VS Code、在服务器上跑代码、或者只想快速暂停一下时，用 Python 内置的 pdb。

### breakpoint() — 最简单的入口

**语法结构：** `breakpoint()`

在代码中直接写 `breakpoint()`，程序运行到这里会暂停，进入交互式调试环境：

```python
def calculate_total(prices, tax_rate):
    subtotal = sum(prices)
    breakpoint()                    # ← 程序停在这里
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

result = calculate_total([10, 20, 30], 0.1)
```

运行后终端会出现 `(pdb)` 提示符，可以输入调试命令。

**`breakpoint()` 是 Python 3.7+ 的内置函数**，等效于 `import pdb; pdb.set_trace()`，但更简洁。如果项目还用 Python 3.6 或更早，用后者。

### pdb 常用命令

进入 pdb 后，用以下命令控制执行和查看状态：

**执行控制：**

| 命令 | 简写 | 作用 |
|---|---|---|
| `next` | `n` | 执行下一行，不进入函数内部 |
| `step` | `s` | 执行下一行，遇到函数调用会进入 |
| `continue` | `c` | 继续运行到下一个断点 |
| `return` | `r` | 执行到当前函数结束 |
| `quit` | `q` | 退出调试，终止程序 |
| `where` | `w` | 查看当前调用堆栈 |

**查看变量：**

| 命令 | 作用 |
|---|---|
| `p 变量名` | 打印变量的值 |
| `pp 变量名` | 格式化打印（字典/列表更好看） |
| `l` | 查看当前行附近的源代码 |
| `ll` | 查看当前函数的完整源代码 |
| `a` | 查看当前函数的所有参数 |
| `dir(对象)` | 查看对象的所有属性和方法 |

直接输入变量名也行，pdb 会显示它的值。但变量名和命令名冲突时（比如变量叫 `n`），要用 `p n` 来查看。

### pdb 实战流程

```python
def find_user(users, target_id):
    for user in users:
        if user["id"] == target_id:
            return user
    return None

users = [
    {"id": 1, "name": "张三"},
    {"id": 2, "name": "李四"},
    {"id": 3, "name": "王五"},
]

result = find_user(users, 2)
print(result)
```

在 `return user` 这行前加 `breakpoint()`：

```python
        if user["id"] == target_id:
            breakpoint()      # ← 暂停
            return user
```

运行后的交互过程：

```
> /path/to/script.py(5)find_user()
-> return user
(Pdb) p user
{'id': 2, 'name': '李四'}
(Pdb) p target_id
2
(Pdb) n
> /path/to/script.py(10)<module>()
-> result = find_user(users, 2)
(Pdb) c
{'id': 2, 'name': '李四'}
```

先看 `user` 和 `target_id` 的值，确认匹配，然后 `n` 执行 `return user`，程序回到调用处，`c` 继续运行结束。

### pdb 设断点

除了 `breakpoint()`，还可以用 `b` 命令在指定文件和行号设断点：

**语法结构：** `b 行号` 或 `b 文件路径:行号`

```
(Pdb) b 15              # 在当前文件第 15 行设断点
(Pdb) b utils.py:30     # 在 utils.py 第 30 行设断点
(Pdb) b                  # 列出所有断点
(Pdb) cl 1               # 删除 1 号断点
(Pdb) cl                 # 删除所有断点
```

这种方式不需要在代码里加 `breakpoint()`，适合调试时临时加断点。

### 条件断点

**语法结构：** `b 行号, 条件`

```
(Pdb) b 15, user["id"] > 100    # 第 15 行，当 user["id"] > 100 时才暂停
```

和 VS Code 的条件断点一样，在循环中过滤特定情况。

## VS Code vs pdb

| 特性 | VS Code 断点 | pdb |
|---|---|---|
| 交互方式 | 图形界面，鼠标操作 | 命令行，键盘输入 |
| 变量查看 | 自动展示所有变量 | 需要手动输入 `p 变量名` |
| 适合场景 | 本地开发、日常调试 | 服务器调试、快速排查 |
| 上手难度 | 低，所见即所得 | 需要记命令 |
| 配置成本 | 需安装扩展和配置 | 零依赖，Python 自带 |

**实际使用建议：** 本地开发优先用 VS Code 断点调试，体验最好。服务器上或者 SSH 环境中用 `breakpoint()`。两者核心概念完全一样，学会一个就能迁移到另一个。

## 调试思路

调试工具只是手段，更重要的是**调试方法**：

**先定位，再动手。** 不要一上来就逐行执行。先看报错信息，确认是哪个函数、哪一行出的错。在该位置设断点，暂停后查看变量，比从头逐行走快得多。

**假设驱动调试。** 暂停后不是漫无目的地看所有变量，而是带着假设来验证——"我猜这个值是 None"——然后查看确认。猜对了就找到了 bug，猜错了就调整假设。

**二分法缩小范围。** 不知道哪里出问题时，在代码中间设断点。前半段没问题说明 bug 在后半段，继续对半切。比从头逐行走快几倍。

## 常见调试场景

### 变量值不符合预期

```python
def process_scores(scores):
    avg = sum(scores) / len(scores)
    breakpoint()        # 暂停，检查 scores 和 avg
    grades = [get_grade(s) for s in scores]
    return grades
```

暂停后用 `p scores` 和 `p avg` 确认值，找出是输入数据有问题还是计算逻辑有问题。

### 函数返回值不对

```python
result = calculate(data)    # ← 在这行加断点
print(result)               # 结果不对
```

停在 `result = calculate(data)` 这行，用 `F11` 进入 `calculate` 内部，逐步执行看哪一步算错了。

### 循环中某一次出错

```python
for i, item in enumerate(items):
    result = process(item)    # ← 条件断点：i == 50
    save(result)
```

只有第 50 次才出错，设条件断点 `i == 50`，跳过前面 49 次无用循环。

### 程序卡死或死循环

```python
while True:
    data = fetch()
    if data:
        process(data)
        break
    # ← 忘了加 sleep 或退出逻辑
```

在循环体内加 `breakpoint()`，每次循环暂停一次，手动检查 `data` 的值和循环条件。

## 速查表

| 操作 | VS Code | pdb |
|---|---|---|
| 设断点 | 点击行号旁红点 | `breakpoint()` 或 `b 行号` |
| 继续运行 | F5 | `c` |
| 单步跳过 | F10 | `n` |
| 单步进入 | F11 | `s` |
| 跳出函数 | Shift+F11 | `r` |
| 查看变量 | 变量面板 | `p 变量名` |
| 条件断点 | 右键断点设条件 | `b 行号, 条件` |
| 查看源码 | 直接看 | `l` |
| 退出调试 | 停止按钮 | `q` |

## 要点

调试的核心就两步：**在出问题的地方暂停，查看变量找到根因**。VS Code 断点调试是日常主力，所见即所得，上手成本最低。`breakpoint()` 是命令行场景的备选，几条命令就能掌握。真正决定调试效率的不是工具操作，而是**先定位再动手、假设驱动验证、二分法缩小范围**这三条思路。调试工具配合好的调试方法，定位 bug 的速度比满屏 `print` 快一个量级。

---

## 本仓库练习（只列题目 · 步骤在链接里）

### 建议 · 调试日记

**题目：** 故意制造或遇到一次报错，读 Traceback，修好，并写一篇踩坑记录。  

**作业（空白，自己写）：** [ex04_debug_journal.md](../exercises/ex04_debug_journal.md)
