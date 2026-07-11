# Python 异常处理：try/except/else/finally 完整指南

## 程序为什么会出错

写代码时错误是常态——用户输入了非法数据、文件不存在、网络断了、除以零。如果不管它，程序直接崩溃退出。**异常处理就是让程序在出错时不要崩，而是优雅地处理问题、继续运行或安全退出。**

## 异常是什么

异常是程序运行时发生的错误，Python 会抛出一个异常对象。如果不捕获，程序就会崩溃：

```python
print(10 / 0)   # ZeroDivisionError: division by zero
print("这行不会执行")
```

用 `try/except` 捕获后，程序不会崩溃：

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("不能除以零")
print("程序继续运行")   # 会执行
```

## try / except — 捕获异常

### 基本结构

```python
# 语法
try:
    可能出错的代码
except 异常类型:
    处理逻辑
```

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 出错后的处理
    print("不能除以零")
```

`try` 块里放可能出错的代码，`except` 块里放出错后的处理逻辑。

### 捕获不同类型的异常

不同的错误对应不同的异常类型：

```python
# 语法
try:
    可能出错的代码
except 异常类型1:
    处理逻辑1
except 异常类型2:
    处理逻辑2
```

```python
try:
    num = int(input("请输入数字: "))
    result = 10 / num
    print(result)
except ValueError:
    print("输入的不是数字")
except ZeroDivisionError:
    print("不能除以零")
```

用户输入字母时触发 `ValueError`，输入 0 时触发 `ZeroDivisionError`，分别处理。

### 一个 except 捕获多种异常

```python
# 语法
try:
    可能出错的代码
except (异常类型1, 异常类型2):
    处理逻辑
```

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("转换失败")
```

用元组把多种异常类型放在一起，任意一种触发都走这个分支。

### 捕获异常信息

用 `as` 把异常对象赋给变量，可以拿到错误详情：

```python
# 语法
try:
    可能出错的代码
except 异常类型 as 变量名:
    # 通过变量名获取错误详情
    处理逻辑
```

```python
try:
    num = int("abc")
except ValueError as e:
    print(f"出错了: {e}")
# 出错了: invalid literal for int() with base 10: 'abc'
```

### 捕获所有异常

```python
try:
    # 一些可能出错的代码
    result = 10 / 0
except Exception as e:
    print(f"发生错误: {e}")
```

**`Exception` 是所有常见异常的父类**，能捕获绝大部分错误。但不推荐无差别捕获——**该精确捕获的就精确捕获**，否则可能把不该忽略的错误也吞掉了。

**不要用 bare except：**

```python
# 不推荐：捕获所有异常，包括 KeyboardInterrupt，连 Ctrl+C 都杀不掉
try:
    something()
except:
    pass

# 推荐：明确捕获 Exception
try:
    something()
except Exception as e:
    print(f"出错: {e}")
```

## else — 没出错时执行

`else` 块在 `try` 中的代码**没有发生任何异常时**才执行：

```python
# 语法
try:
    可能出错的代码
except 异常类型:
    处理逻辑
else:
    没出错时执行的代码
```

```python
try:
    num = int(input("请输入数字: "))
except ValueError:
    print("不是数字")
else:
    print(f"你输入了: {num}")
```

输入合法数字时走 `else`，输入非法时走 `except`。

### 为什么要用 else

**把可能出错的代码和不出错的代码分开。** 如果都放在 try 里，可能多捕获了不该捕获的异常：

```python
# 不推荐：process 函数出错也会被 except 捕获
try:
    num = int(input("请输入数字: "))
    result = process(num)
except ValueError:
    print("出错了")

# 推荐：只捕获可能出错的那行
try:
    num = int(input("请输入数字: "))
except ValueError:
    print("输入不是数字")
else:
    result = process(num)   # 这行出错不会被上面的 except 捕获
```

## finally — 无论如何都执行

`finally` 块**无论是否发生异常都会执行**，通常用来做清理工作：

```python
# 语法
try:
    可能出错的代码
except 异常类型:
    处理逻辑
finally:
    无论如何都执行的代码
```

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在")
else:
    print(content)
finally:
    f.close()   # 无论成功还是失败，都要关闭文件
    print("清理完成")
```

### finally 的执行时机

```python
try:
    print("1. try 开始")
    result = 10 / 0
    print("2. 这行不会执行")
except ZeroDivisionError:
    print("3. 捕获到异常")
else:
    print("4. else 不会执行（因为出错了）")
finally:
    print("5. finally 总是执行")
print("6. 程序继续")
```

输出：

```
1. try 开始
3. 捕获到异常
5. finally 总是执行
6. 程序继续
```

**即使 try 或 except 里有 return，finally 也会在 return 之前执行。**

### finally 的实际用途

```python
# 数据库连接
try:
    conn = connect_database()
    data = conn.query("SELECT * FROM users")
except ConnectionError:
    print("连接失败")
else:
    process(data)
finally:
    conn.close()   # 无论成功失败，断开连接

# 文件操作（实际上用 with 更好）
try:
    f = open("data.txt", "w")
    f.write("hello")
finally:
    f.close()
```

## 完整结构

`try/except/else/finally` 的完整组合：

```python
try:
    # 可能出错的代码
    num = int(input("请输入数字: "))
    result = 10 / num
except ValueError:
    # 处理类型错误
    print("请输入数字")
except ZeroDivisionError:
    # 处理除零错误
    print("不能除以零")
except Exception as e:
    # 处理其他未知错误
    print(f"未知错误: {e}")
else:
    # 没出错时执行
    print(f"结果: {result}")
finally:
    # 无论是否出错都执行
    print("处理完毕")
```

**四块的执行逻辑：**

1. 先执行 `try` 中的代码
2. 出错了 → 跳到匹配的 `except`
3. 没出错 → 执行 `else`
4. 最后**无论什么情况**都执行 `finally`

## 主动抛出异常

用 `raise` 主动抛出异常，通常用在**函数参数校验**中：

```python
# 语法
raise 异常类型(消息)
```

```python
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return f"年龄设置为 {age}"

try:
    set_age(-5)
except ValueError as e:
    print(e)   # 年龄不能为负数
```

**函数发现参数不合法时，不要返回错误码或字符串，直接 raise 异常**。调用者用 try/except 处理。

## 自定义异常

Python 允许创建自己的异常类，继承 `Exception`：

```python
# 语法
class 自定义异常名(Exception):
    """异常说明"""
    pass
```

```python
class InvalidScoreError(Exception):
    """分数不合法异常"""
    pass

def set_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"分数 {score} 不合法，必须在 0-100 之间")
    print(f"分数设置为 {score}")

try:
    set_score(150)
except InvalidScoreError as e:
    print(e)   # 分数 150 不合法，必须在 0-100 之间
```

自定义异常让错误类型更明确，调用者可以精确捕获。

## 常见异常类型

| 异常 | 触发场景 |
|---|---|
| `ValueError` | 值不合法，如 `int("abc")` |
| `TypeError` | 类型错误，如 `"a" + 1` |
| `ZeroDivisionError` | 除以零 |
| `IndexError` | 索引越界，如 `[1,2][10]` |
| `KeyError` | 字典键不存在 |
| `FileNotFoundError` | 文件不存在 |
| `AttributeError` | 属性不存在，如 `None.split()` |
| `NameError` | 变量未定义 |
| `ImportError` | 导入模块失败 |

## 实战示例

### 安全的用户输入

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("请输入有效数字")

age = get_number("请输入年龄: ")
print(f"你的年龄是 {age}")
```

输入不合法时不崩溃，循环提示重新输入。

### 安全的文件读取

```python
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return None
    except UnicodeDecodeError:
        print("编码错误，可能不是 UTF-8 文件")
        return None
    except Exception as e:
        print(f"读取失败: {e}")
        return None

content = read_file("data.txt")
if content:
    print(content)
```

### 安全的除法计算

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "除数不能为零"
    except TypeError:
        return "两个参数都必须是数字"
    else:
        return result
    finally:
        print("计算完成")

print(safe_divide(10, 5))    # 计算完成 → 2.0
print(safe_divide(10, 0))    # 计算完成 → 除数不能为零
print(safe_divide(10, "a"))  # 计算完成 → 两个参数都必须是数字
```

### 带重试的操作

```python
import time

def retry(func, max_attempts=3, delay=1):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            print(f"第 {attempt} 次失败: {e}")
            if attempt < max_attempts:
                time.sleep(delay)
    print("重试次数用完")
    return None

# 模拟不稳定操作
def fetch_data():
    import random
    if random.random() < 0.5:
        raise ConnectionError("网络超时")
    return "数据获取成功"

result = retry(fetch_data)
print(result)
```

## 速查表

| 语法 | 用途 |
|---|---|
| `try:` | 尝试执行的代码 |
| `except 异常类型:` | 捕获特定异常 |
| `except 异常类型 as e:` | 捕获并拿到异常信息 |
| `except (A, B):` | 捕获多种异常 |
| `except Exception:` | 捕获所有常见异常 |
| `else:` | 没出错时执行 |
| `finally:` | 无论如何都执行 |
| `raise 异常` | 主动抛出异常 |
| `raise 异常(msg)` | 带消息抛出异常 |

## 要点

异常处理日常最常用的就是 **try + except**。`else` / `finally` / 自定义异常以后用到再学。

---

## 本篇对应练习（最简示例 · 与仓库题一致）

请先读完「文件读写」。必做 [ex02](../exercises/ex02_safe_read.py) 就是这种级别：

```python
path = input("请输入文件路径: ")

try:
    f = open(path, encoding="utf-8")
    text = f.read()
    f.close()
    print(text)
except FileNotFoundError:
    print("文件不存在:", path)
```

（以后你会学 `with open`，作业先会 `open` + `try` 即可。）

---

## 本仓库学习导航
- **练习安排：必做** [ex02 安全读文件](../exercises/ex02_safe_read.py)  
  （请已读完「文件读写」）
- 作业是最简单脚本，**不含测试代码**
