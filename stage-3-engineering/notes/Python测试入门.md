# Python 测试入门：从 assert 到 pytest

代码能跑不代表代码是对的。手动运行验证一次，改了别的代码后又坏了——这种"改一个 bug 引入两个 bug"的循环，根本原因是没有自动化测试。**测试就是把"代码是否符合预期"这件事自动化**：写一段验证代码，每次改完跑一遍，几秒内告诉你哪里出了问题。

Python 测试从简单到专业分两层：**`assert` 语句做最基础的断言**，**pytest 框架组织和管理测试用例**。先从 assert 开始，再过渡到 pytest。

## assert — 最基础的断言

### 语法结构

```python
# 语法
assert 布尔表达式, "失败时的提示信息"

# 示例
assert 1 + 1 == 2, "加法算错了"
assert len("hello") == 5
```

`assert` 是 Python 关键字。表达式为 True 时什么都不发生；为 False 时抛出 `AssertionError`，程序停止。第二个参数（提示信息）可选，不写也行。

### 基本用法

```python
def add(a, b):
    return a + b

# 手动验证
result = add(2, 3)
assert result == 5, f"期望 5，实际 {result}"
print("测试通过")
```

`add(2, 3)` 返回 5，`assert result == 5` 通过，继续执行。如果 `add` 写错了返回 6，assert 直接报错，告诉你哪里出了问题。

### 验证函数

给一个函数写多条断言，覆盖不同输入：

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "C"

# 正常用例
assert get_grade(95) == "A"
assert get_grade(85) == "B"
assert get_grade(50) == "C"

# 边界用例
assert get_grade(90) == "A"    # 边界值
assert get_grade(60) == "B"    # 边界值
assert get_grade(0) == "C"     # 最小值
```

**边界值是最容易出错的地方。** 90 分和 89 分应该返回不同等级，少写一个等号就会导致边界用例失败。

### assert 的局限

assert 能验证单个函数，但有几个问题：

- 用例多了之后，全写在脚本里不好管理
- 某条 assert 失败后，后面的用例不会执行
- 没有清晰的"哪些通过、哪些失败"的报告
- 不能方便地组织批量测试

**pytest 解决了这些问题。**

## pytest — 测试框架

### 安装

```bash
pip install pytest
```

### 基本规则

pytest 约定大于配置，记住三条规则就能用：

**规则一：测试文件名必须以 `test_` 开头**，如 `test_math.py`、`test_utils.py`。

**规则二：测试函数名必须以 `test_` 开头**，如 `test_add`、`test_get_grade`。

**规则三：用 `assert` 做断言**，不需要学新的断言语法，直接用 Python 内置的 `assert`。

### 第一个测试

创建文件 `test_calculator.py`：

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 20) == -10
```

在终端运行：

```bash
# 语法
pytest

# 示例
pytest test_calculator.py
```

pytest 自动发现所有 `test_` 开头的函数，逐个执行，输出结果：

```
============================== test session starts ==============================
collected 2 items

test_calculator.py::test_add PASSED                                     [ 50%]
test_calculator.py::test_subtract PASSED                                [100%]

=============================== 2 passed in 0.01s ===============================
```

`PASSED` 表示通过，`FAILED` 表示失败。不用写任何配置，一个命令就跑完所有测试。

### 测试失败时的报告

故意写一个会失败的断言：

```python
def test_add():
    assert add(2, 3) == 6    # 故意写错，期望 6 实际 5
```

运行后 pytest 输出：

```
============================== FAILED ==============================
def test_add():
       assert add(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = add(2, 3)
============================== 1 failed in 0.01s ==============================
```

**pytest 会显示哪个 assert 失败了、期望值和实际值各是多少、函数调用过程**。信息比裸 `assert` 丰富得多，定位问题很快。

### 测试和代码分离

实际项目中，测试代码和业务代码分开放：

```
my_project/
├── calculator.py       # 业务代码
└── test_calculator.py  # 测试代码
```

`calculator.py`：

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
```

`test_calculator.py`：

```python
from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
```

运行测试时指定文件名：

```bash
pytest test_calculator.py
```

或者运行整个目录：

```bash
pytest
```

pytest 自动发现所有 `test_` 开头的文件并执行。

## 五个实战用例

下面用 pytest 写 5 个测试用例，覆盖不同场景。

### 用例一：成绩等级判定

```python
# 业务代码
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

# 测试代码
def test_get_grade_normal():
    assert get_grade(95) == "A"
    assert get_grade(85) == "B"
    assert get_grade(70) == "C"
    assert get_grade(30) == "F"

def test_get_grade_boundary():
    assert get_grade(90) == "A"    # 边界：恰好 90
    assert get_grade(80) == "B"    # 边界：恰好 80
    assert get_grade(60) == "C"    # 边界：恰好 60
    assert get_grade(59) == "F"    # 边界：恰好不及格
    assert get_grade(0) == "F"     # 边界：零分
```

**每个边界值都测。** 边界是 `>=` 和 `<` 最容易写错的地方，写成 `>` 就会漏掉恰好等于的分数。

### 用例二：字符串处理

```python
# 业务代码
def normalize_name(name):
    return name.strip().lower().replace(" ", "_")

# 测试代码
def test_normalize_name():
    assert normalize_name("张三") == "张三"
    assert normalize_name("  张三  ") == "张三"
    assert normalize_name("HELLO") == "hello"
    assert normalize_name("hello world") == "hello_world"
    assert normalize_name("  Hello  World  ") == "hello_world"
```

测试 strip、lower、replace 三步链式操作的组合效果。带空格和大小写的输入最容易出现遗漏。

### 用例三：异常场景

```python
# 业务代码
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 测试代码
import pytest

def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(10, 0)
```

**语法结构：** `with pytest.raises(异常类型, match="错误信息匹配"):`

`pytest.raises` 用来测试某个操作是否抛出了预期的异常。`match` 参数可以用正则匹配错误信息，不需要精确匹配。

不写 `pytest.raises`，直接 `divide(10, 0)` 会抛异常导致测试报错。用 `pytest.raises` 包裹后，抛了 `ValueError` 算通过，不抛反而算失败。

### 用例四：字典操作

```python
# 业务代码
def filter_passed(students):
    return {name: score for name, score in students.items() if score >= 60}

# 测试代码
def test_filter_passed():
    students = {"张三": 85, "李四": 45, "王五": 92, "赵六": 30}
    result = filter_passed(students)

    assert "张三" in result
    assert "李四" not in result
    assert result["张三"] == 85
    assert result["王五"] == 92
    assert len(result) == 2

def test_filter_passed_empty():
    assert filter_passed({}) == {}

def test_filter_passed_all_failed():
    students = {"张三": 30, "李四": 45}
    assert filter_passed(students) == {}
```

**不光测正常数据，还要测空字典和全部不及格的极端情况。** 这些场景最容易出 `KeyError` 或空指针类的问题。

### 用例五：列表排序

```python
# 业务代码
def sort_by_score(students):
    return sorted(students, key=lambda s: s["score"], reverse=True)

# 测试代码
def test_sort_by_score():
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 70},
    ]
    result = sort_by_score(students)

    assert result[0]["name"] == "李四"     # 最高分排第一
    assert result[1]["name"] == "张三"
    assert result[2]["name"] == "王五"
    assert result[0]["score"] >= result[1]["score"]    # 验证降序

def test_sort_by_score_single():
    students = [{"name": "张三", "score": 85}]
    result = sort_by_score(students)
    assert len(result) == 1
    assert result[0]["name"] == "张三"
```

**验证排序结果时，既检查具体顺序，也检查排序的数学性质**（前一个 >= 后一个），比逐一比对更健壮。

## 测试组织

### 一个文件测一个模块

```
my_project/
├── calculator.py
├── utils.py
└── tests/
    ├── test_calculator.py
    ├── test_utils.py
    └── test_grade.py
```

测试放在 `tests/` 目录下，一个业务模块对应一个测试文件。

### setup 和 teardown — 前置和后置操作

有些测试需要准备数据（创建临时文件、初始化对象），测完要清理。pytest 用**fixture** 处理：

**语法结构：**

```python
# 语法
import pytest

@pytest.fixture
def fixture名称():
    # 前置：准备数据
    data = 准备数据()
    yield data          # yield 之前是 setup，之后是 teardown
    # 后置：清理数据
    清理操作()
```

**示例：**

```python
import pytest

@pytest.fixture
def sample_students():
    # 前置：准备测试数据
    students = [
        {"name": "张三", "score": 85},
        {"name": "李四", "score": 92},
        {"name": "王五", "score": 30},
    ]
    yield students    # 把数据交给测试函数
    # 后置：这里可以做清理（本例不需要）

def test_filter_passed(sample_students):
    from grade import filter_passed
    result = filter_passed({s["name"]: s["score"] for s in sample_students})
    assert "张三" in result
    assert "王五" not in result

def test_sort_by_score(sample_students):
    from grade import sort_by_score
    result = sort_by_score(sample_students)
    assert result[0]["name"] == "李四"
```

测试函数的参数名 `sample_students` 和 fixture 名一致，pytest 自动注入。多个测试共用同一份准备逻辑时，fixture 避免重复代码。

### 运行指定测试

```bash
# 运行单个文件
pytest test_calculator.py

# 运行单个函数
pytest test_calculator.py::test_add

# 运行名字包含关键词的测试
pytest -k "grade"

# 显示详细输出
pytest -v

# 遇到第一个失败就停止
pytest -x

# 显示 print 输出
pytest -s
```

## 常用 pytest 参数

| 参数 | 作用 |
|---|---|
| `-v` | 详细模式，显示每个测试函数的名字和结果 |
| `-s` | 显示测试中的 `print` 输出（默认捕获） |
| `-x` | 遇到第一个失败就停止 |
| `-k "关键词"` | 只运行名字包含关键词的测试 |
| `--tb=short` | 简化失败时的错误追踪信息 |
| `--lf` | 只运行上次失败的测试 |
| `--ff` | 先运行上次失败的，再运行其余的 |
| `--count=N` | 重复运行 N 次（排查不稳定测试） |

**日常最常用的是 `-v`（看详细结果）和 `-k`（筛选运行）。**

## assert vs pytest

| 特性 | assert | pytest |
|---|---|---|
| 本质 | Python 语句 | 测试框架 |
| 用例组织 | 手动写在脚本里 | 自动发现 `test_` 开头的文件和函数 |
| 失败报告 | 只显示 assert 行和值 | 显示上下文、期望值、实际值、调用过程 |
| 失败后继续 | 第一个失败就停 | 继续执行其他用例 |
| 异常测试 | 需要 try/except | `pytest.raises` 一步到位 |
| 适用场景 | 快速验证、临时检查 | 正式项目、持续集成 |

**关系是递进的：** pytest 底层用的就是 assert，只是在外面包了一层自动发现、执行、报告的功能。先学会写 assert，再学 pytest 只是多了几条规则。

## 速查表

| 操作 | 代码 |
|---|---|
| 基本断言 | `assert 条件` |
| 带提示断言 | `assert 条件, "提示"` |
| 浮点数比较 | `assert abs(a - b) < 0.001` |
| 异常断言 | `with pytest.raises(异常类型):` |
| 带匹配的异常断言 | `with pytest.raises(异常类型, match="信息"):` |
| 运行所有测试 | `pytest` |
| 运行指定文件 | `pytest test_xxx.py` |
| 运行指定函数 | `pytest test_xxx.py::test_func` |
| 关键词筛选 | `pytest -k "关键词"` |
| 详细输出 | `pytest -v` |
| 遇失败即停 | `pytest -x` |

## 要点

测试的核心就两件事：**用 assert 表达"期望什么结果"，用 pytest 自动运行和管理这些断言**。assert 是 Python 自带的语句，零学习成本；pytest 在 assert 外面包了自动发现、批量执行、清晰报告三层功能，记住三条规则就能用：**文件名 `test_` 开头、函数名 `test_` 开头、用 assert 做断言**。写测试时的重点是覆盖边界值和异常场景——正常流程谁都会写，bug 往往藏在边界和意外输入里。先给每个函数写 3 到 5 条断言覆盖正常值、边界值和异常情况，再逐步扩展，不需要一步到位。

---

## 本仓库学习导航
- **练习安排：加练** [ex03 pytest](../exercises/ex03_pytest_stats/)  
  **可以整段不做**；测试不是语法入门必选项
