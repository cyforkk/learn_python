# Python 速成：学习路线与资源

> 目标：用最短路径建立可写脚本、能读文档、会查资料的 Python 能力。  
> **默认已会运行 Python**；环境安装不是主线。  
> 适合：有一点基础或装好 Python 后想系统练；方向阶段见 stage-4。

## 本仓库导航（按阶段学）

| 阶段 | 目录 | 说明 |
|------|------|------|
| 总入口 | [../README.md](../README.md) | 怎么用本仓库 |
| 进度勾选 | [../progress.md](../progress.md) | 打勾清单 |
| 学习地图 | [learning-map.md](learning-map.md) | 笔记↔练习（含「无/过关/加练」） |
| 练习原则 | [exercise-policy.md](exercise-policy.md) | 不是每篇笔记都有题 |
| 搭建工作流 | [repo-build-workflow.md](repo-build-workflow.md) | 从零搭学习仓库的可复用流程 |
| FAQ 错题 | [faq-common-mistakes.md](faq-common-mistakes.md) | 常见报错 |
| ~~0 环境~~ | [../stage-0-setup/README.md](../stage-0-setup/README.md) | **可选附录**（装不上再看） |
| 1 语法核心 | [../stage-1-basics/README.md](../stage-1-basics/README.md) | **主线起点** · 笔记 + 练习 |
| 2 标准库 | [../stage-2-stdlib/README.md](../stage-2-stdlib/README.md) | 文件 / 异常 / 模块 / OOP |
| 3 工程习惯 | [../stage-3-engineering/README.md](../stage-3-engineering/README.md) | venv / 测试 / 调试 / Git |
| 4 方向分支 | [../stage-4-tracks/README.md](../stage-4-tracks/README.md) | [各方向路线](stage4-paths/README.md) + GitHub |
| 5 综合项目 | [../stage-5-projects/README.md](../stage-5-projects/README.md) | 项目规格与实战笔记 |

**学习节奏（勿颠倒）**：① 读 `notes/` → ② **仅做标注为必做/建议的练习**（不是篇篇有题）→ ③ 对照 `solutions/` → ④ 项目。  
练习原则：[exercise-policy.md](exercise-policy.md) · 地图：[learning-map.md](learning-map.md)

---

## 一、你需要先建立的正确预期

| 误区 | 更合理的目标 |
|------|----------------|
| 把语法全背完再写代码 | 会查官方文档 + 每天写一点小程序 |
| 先精通所有框架 | 先把「语法 + 标准库 + 调试」打牢 |
| 只看视频不写代码 | 每学一个知识点，立刻写 3～5 个小例子 |
| 追求一次学完 | 分阶段：会用 → 写对 → 写稳 → 写快 |

**速成的本质**：少而精的知识点 + 大量动手 + 一条清晰的进阶路线。

---

## 二、环境（可选 · 默认跳过）

本仓库**默认已有 Python 3.10+**。  
仅当 `python`/`py` 不可用时，再看：[stage-0-setup](../stage-0-setup/README.md)、[windows-setup.md](windows-setup.md)。

`pip` / `venv` 在 **阶段 3** 系统练习；做 stage-1 练习通常本机 Python 足够。

---

## 三、学习路线总览（建议 6～12 周）

```
阶段 1  语法核心（主线起点）      → stage-1-basics/
   ↓
阶段 2  标准库 + 文件/异常/模块   → stage-2-stdlib/
   ↓
阶段 3  工程习惯（venv/测试/Git） → stage-3-engineering/
   ↓
阶段 4  方向分支                  → stage-4-tracks/
   ↓
阶段 5  项目实战                  → stage-5-projects/ + projects/

（可选附录）stage-0-setup — 仅环境故障时查阅
```

时间可按每天 1～2 小时估算。

---

## 四、分阶段详细路线

### 阶段 1：语法核心（约 1～2 周）

→ **入口**：[stage-1-basics/README.md](../stage-1-basics/README.md)  
→ **笔记**：[stage-1-basics/notes/](../stage-1-basics/notes/)  
→ **练习**：[stage-1-basics/exercises/](../stage-1-basics/exercises/)（完成后 `python ex0x_xxx.py --check`）  
→ **答案**：[stage-1-basics/solutions/](../stage-1-basics/solutions/)

**学什么**

1. 变量、类型：`int` / `float` / `str` / `bool` / `None`
2. 输入输出：`print`、`input`
3. 运算符与表达式
4. 条件：`if` / `elif` / `else`
5. 循环：`for`、`while`、`break`、`continue`
6. 容器：
   - 列表 `list`（增删改查、切片）
   - 元组 `tuple`
   - 字典 `dict`（最常用）
   - 集合 `set`
7. 字符串常用方法、f-string
8. 函数：`def`、参数、返回值、默认参数
9. 作用域基础（局部 / 全局）

**练什么（仓库内对应题）**

| 练习 | 文件 |
|------|------|
| 猜数字（限次） | [ex01_guess_number.py](../stage-1-basics/exercises/ex01_guess_number.py) |
| 简易计算器 | [ex02_calculator.py](../stage-1-basics/exercises/ex02_calculator.py) |
| 学生成绩统计 | [ex03_score_stats.py](../stage-1-basics/exercises/ex03_score_stats.py) |
| 九九乘法表 | [ex04_multiplication_table.py](../stage-1-basics/exercises/ex04_multiplication_table.py) |
| 函数小重构 | [ex05_refactor_functions.py](../stage-1-basics/exercises/ex05_refactor_functions.py) |

**验收标准**

- 不看笔记能写出：`for` 遍历列表、字典读写、自定义函数
- 能解释：可变 vs 不可变（list vs tuple/str）
- 相关练习 `--check` 全部通过

---

### 阶段 2：能干活的 Python（约 1～2 周）

→ **入口**：[stage-2-stdlib/README.md](../stage-2-stdlib/README.md)  
→ **笔记**：[stage-2-stdlib/notes/](../stage-2-stdlib/notes/)  
→ **练习**：[stage-2-stdlib/exercises/](../stage-2-stdlib/exercises/)  
→ **答案**：[stage-2-stdlib/solutions/](../stage-2-stdlib/solutions/)

**学什么**

1. 文件读写：`open`、`with`、文本 / CSV 基础
2. 异常：`try` / `except` / `else` / `finally`
3. 模块与包：`import`、自己拆文件
4. 常用标准库（先会用即可）：
   - `pathlib`：路径
   - `json`：JSON 读写
   - `datetime`：时间日期
   - `os` / `sys`：环境与参数（了解）
   - `re`：正则（先会简单匹配）
   - `collections`：`Counter`、`defaultdict`（可选）
5. 推导式：列表/字典推导式（写简洁代码）
6. 面向对象入门：
   - `class`、`__init__`、实例方法
   - 不必先深挖继承/元类

**练什么（仓库内对应题）**

| 练习 | 文件 |
|------|------|
| JSON 待办 | [ex01_todo_json.py](../stage-2-stdlib/exercises/ex01_todo_json.py) |
| 安全读文件 | [ex02_safe_read.py](../stage-2-stdlib/exercises/ex02_safe_read.py) |
| 小模块拆分 | [ex03_mini_package/](../stage-2-stdlib/exercises/ex03_mini_package/) |
| pathlib 列目录 | [ex04_list_files.py](../stage-2-stdlib/exercises/ex04_list_files.py) |
| Book 类 | [ex05_book_class.py](../stage-2-stdlib/exercises/ex05_book_class.py) |

**验收标准**

- 会用 `with open(...)` 安全读写文件
- 会处理「文件不存在」等常见异常
- 能把一个脚本拆成 2～3 个 `.py` 模块
- 相关练习 `--check` 全部通过

---

### 阶段 3：工程习惯（约 1 周，可与阶段 2 并行）

→ **入口**：[stage-3-engineering/README.md](../stage-3-engineering/README.md)  
→ **笔记**：[stage-3-engineering/notes/](../stage-3-engineering/notes/)  
→ **练习**：[stage-3-engineering/exercises/](../stage-3-engineering/exercises/)  
→ **答案**：[stage-3-engineering/solutions/](../stage-3-engineering/solutions/)

**学什么**

1. 虚拟环境 + `requirements.txt`（或 `pip freeze`）
2. 代码风格：PEP 8 基本约定（命名、缩进、空行）
3. 类型注解入门（`def f(x: int) -> str:`）——先认识，不强迫精通
4. 调试：
   - VS Code 断点
   - `pdb` 或 `breakpoint()`
5. 测试入门：`assert` 或 `pytest` 写 3～5 个用例
6. Git 基础：`add` / `commit` / `push`（强烈建议）

**练什么**

- [ex01 venv 实践](../stage-3-engineering/exercises/ex01_venv_practice.md)
- [ex02 类型注解](../stage-3-engineering/exercises/ex02_typed_functions.py)
- [ex03 pytest](../stage-3-engineering/exercises/ex03_pytest_stats/)
- [ex04 调试日记](../stage-3-engineering/exercises/ex04_debug_journal.md)

**验收标准**

- 能在新电脑上：`venv` → `pip install -r requirements.txt` → 跑起来
- 出 bug 时第一反应是「复现 + 定位」，而不是盲目改代码

---

### 阶段 4：方向分支（选 1 条主线，约 2～4 周）

→ **入口**：[stage-4-tracks/README.md](../stage-4-tracks/README.md)  
→ **各方向从零路线与资源（已有 Python 基础）**：[stage4-paths/README.md](stage4-paths/README.md)  
→ **GitHub 读码/练手清单**：[stage4-github-projects.md](stage4-github-projects.md)

先选 **一个** 方向深挖，其他方向以后再扩。阅读对应 `path-*.md` → 跑通 **starter + demo** → 外部资源与 GitHub 练手。

#### 路线 A：自动化 / 脚本（上手最快）

→ [automation/](../stage-4-tracks/automation/README.md) · starter：[automation/starter/](../stage-4-tracks/automation/starter/) · demo：[automation/demo/](../stage-4-tracks/automation/demo/)

| 主题 | 库 / 技能 |
|------|-----------|
| HTTP 请求 | `requests` |
| 解析网页 | `BeautifulSoup`（注意合规与 robots） |
| Excel | `openpyxl` / `pandas`（轻量） |
| 定时 / 批处理 | 系统计划任务 + 自己的脚本 |
| GUI（可选） | `tkinter` |

**小项目**：自动下载公开数据并整理成 Excel；批量处理图片文件名；监控某目录变化。

**GitHub（摘要）**

| 用途 | 仓库 |
|------|------|
| 读码 | [asweigart/automate-the-boring-stuff](https://github.com/asweigart/automate-the-boring-stuff)、[psf/requests](https://github.com/psf/requests) |
| 练手 | [public-apis/public-apis](https://github.com/public-apis/public-apis)、[TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) |

#### 路线 B：数据分析

→ [data/](../stage-4-tracks/data/README.md) · starter：[data/starter/](../stage-4-tracks/data/starter/) · demo：[data/demo/](../stage-4-tracks/data/demo/)

| 主题 | 库 / 技能 |
|------|-----------|
| 表格数据 | `pandas` |
| 数值计算 | `numpy` |
| 可视化 | `matplotlib` / `seaborn` |
| 笔记本 | Jupyter |

**小项目**：一份 CSV 的清洗 → 统计 → 出 3 张图 → 写结论。

**GitHub（摘要）**

| 用途 | 仓库 |
|------|------|
| 课程/读码 | [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners)、[jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) |
| 练手 | Kaggle Datasets + 本仓库 CSV；[mwaskom/seaborn](https://github.com/mwaskom/seaborn) examples |

#### 路线 C：Web 后端

→ [web/](../stage-4-tracks/web/README.md) · starter：[web/starter/](../stage-4-tracks/web/starter/) · demo：[web/demo/](../stage-4-tracks/web/demo/)

| 主题 | 库 / 技能 |
|------|-----------|
| 轻量 Web | Flask 或 FastAPI（推荐 FastAPI 做 API） |
| 数据库 | SQLite + SQL 基础，再学 ORM |
| HTTP 概念 | 请求方法、状态码、JSON API |
| 前端对接（可选） | 会返回 JSON 即可 |

**小项目**：待办 API / 简易博客 API / 记账 API。

**GitHub（摘要）**

| 用途 | 仓库 |
|------|------|
| 读码/教程 | [tiangolo/fastapi](https://github.com/tiangolo/fastapi)、[pallets/flask](https://github.com/pallets/flask) |
| 看结构 | [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) |

#### 路线 D：AI / 机器学习入门

→ [ai/](../stage-4-tracks/ai/README.md) · starter：[ai/starter/](../stage-4-tracks/ai/starter/) · demo：[ai/demo/](../stage-4-tracks/ai/demo/)

| 主题 | 库 / 技能 |
|------|-----------|
| 基础数学直觉 | 向量、梯度（够用即可） |
| 经典 ML | `scikit-learn` |
| 深度学习（后） | PyTorch 或 TensorFlow |
| LLM 应用（实用） | OpenAI 兼容 API、提示词、RAG 概念 |

**建议顺序**：先会 Python 数据处理（pandas）→ 再进模型；不要零语法直接啃大模型源码。

**GitHub（摘要）**

| 用途 | 仓库 |
|------|------|
| 课程 | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)、[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) |
| examples | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) 的 `examples/`；[openai/openai-python](https://github.com/openai/openai-python) |

#### 路线 E：爬虫 / 数据抓取（注意法律与网站条款）

可先走 **路线 A starter**（`requests`），再按需加解析库。GitHub 读码可参考路线 A 的 requests / public-apis，以及合规前提下的解析练习。

| 主题 | 技能 |
|------|------|
| 请求与解析 | `requests` + `BeautifulSoup` / `lxml` |
| 异步（进阶） | `httpx` + `asyncio` |
| 反爬（进阶） | 限速、代理、合规优先 |

---

### 阶段 5：项目实战与持续精进（长期）

→ **入口**：[stage-5-projects/README.md](../stage-5-projects/README.md)  
→ **笔记**：[stage-5-projects/notes/](../stage-5-projects/notes/)  
→ **项目规格**：[stage-5-projects/exercises/](../stage-5-projects/exercises/)  
→ **你的代码**：[projects/](../projects/README.md)

**如何选题（优先级从高到低）**

1. 能解决你自己真实麻烦的（最好）
2. 能写进作品集的（有输入→处理→输出）
3. 刻意练弱项的（例如「我不会文件批处理」）

**建议项目规模**

- 初级：1～3 个文件，1～2 天完成
- 中级：有模块划分、配置、README、简单测试
- 高级：部署、日志、错误处理、数据结构清晰

**进阶主题（按需）**

- 迭代器 / 生成器 / 装饰器
- 上下文管理器 `with` 自定义
- 并发：`threading` / `asyncio` / `multiprocessing`（先搞懂何时需要）
- 设计模式（够用即可，别背清单）
- 性能：`timeit`、profiling、算法复杂度直觉

---

## 五、每周可执行计划（示例 8 周）

| 周次 | 重点 | 交付物 |
|------|------|--------|
| 第 1 周 | 环境 + 变量/控制流/列表字典 | 3 个命令行小游戏或工具 |
| 第 2 周 | 函数 + 文件 + 异常 | 读写 JSON/CSV 的脚本 |
| 第 3 周 | 模块化 + venv + 调试 | 拆成多文件的待办/笔记工具 |
| 第 4 周 | 标准库深一点 + 小爬取/API 调用 | 用 `requests` 拉公开 API |
| 第 5～6 周 | 选定方向 A/B/C/D | 方向相关教程 + 1 个中型项目启动 |
| 第 7～8 周 | 项目收尾 | README、依赖、演示截图、能复现运行 |

---

## 六、学习方法（比资源清单更重要）

### 6.1 费曼学习法（简化版）

1. 学一个概念（如「字典」）
2. 合上书，用自己的话写 5 行解释
3. 写一个最小例子
4. 讲给别人听 / 写博客；卡壳的地方就是没懂的地方

### 6.2 刻意练习节奏

```
看 20% → 写 60% → 改 20%
```

- 不要连续看 3 小时视频零代码
- 遇到报错：先读完整 Traceback 最后几行
- 同一报错至少自己尝试 15 分钟再搜

### 6.3 如何问问题（高效）

写清楚这四件事：

1. 你想做什么
2. 你做了什么（代码片段）
3. 期望结果 vs 实际结果（完整报错）
4. 你已经试过什么

### 6.4 防坑清单

- 缩进必须一致（空格不要和 Tab 混用，统一 4 空格）
- 可变默认参数不要写 `def f(a=[])`
- 字符串与数字不要直接 `+`，先转换类型
- Windows 路径优先用 `pathlib` 或原始字符串 `r"C:\path"`
- 中文编码：读写文本时明确 `encoding="utf-8"`
- 不要用 `from module import *`

---

## 七、学习资源（精选，宁缺毋滥）

### 7.1 官方与权威（首选）

| 资源 | 说明 | 链接 |
|------|------|------|
| Python 官方教程 | 最权威入门，适合当词典 | https://docs.python.org/zh-cn/3/tutorial/ |
| Python 标准库文档 | 查模块用法 | https://docs.python.org/zh-cn/3/library/ |
| PEP 8 | 代码风格 | https://peps.python.org/pep-0008/ |
| Real Python | 英文高质量教程（中高级也强） | https://realpython.com/ |

### 7.2 系统课程 / 书籍

| 类型 | 推荐 | 适合阶段 |
|------|------|----------|
| 书籍 | 《Python 编程：从入门到实践》（Crash Course） | 阶段 1～2 |
| 书籍 | 《流畅的 Python》（Fluent Python） | 有基础后进阶 |
| 书籍 | 《Python  Cookbook》 | 查特定技巧 |
| 互动 | freeCodeCamp / Codecademy Python 轨 | 零基础练手 |
| 中文 | 菜鸟教程 Python3 | 速查语法（注意别只抄不练） |
| 中文 | 廖雪峰 Python 教程 | 入门串讲 |
| 视频 | freeCodeCamp YouTube 全长 Python 课 | 喜欢视频的人 |
| 视频 | B 站搜索「Python 黑马 / 尚硅谷」等完整版 | 体系课（选一门跟完即可） |

**原则**：系统课 **只跟一门** 到阶段 2 结束，然后转向「文档 + 项目」。

### 7.3 练习平台

| 平台 | 用途 |
|------|------|
| https://leetcode.cn | 算法题（后期，别一上来就刷 hard） |
| https://www.hackerrank.com/domains/python | Python 专项练习 |
| https://exercism.org/tracks/python | 有导师批改风格的练习 |
| https://www.codewars.com | 小 kata，练手感 |
| https://adventofcode.com | 每年 12 月趣味题，很适合项目化练习 |

入门期建议：Exercism / HackerRank 比 LeetCode 更友好。

### 7.4 方向型资源

| 方向 | 资源 |
|------|------|
| 数据分析 | pandas 官方用户指南；《利用 Python 进行数据分析》 |
| Web | FastAPI 官方文档；Flask 官方教程 |
| 自动化 | Automate the Boring Stuff with Python（免费在线：https://automatetheboringstuff.com/） |
| 科学计算 | NumPy 官方 quickstart |
| AI 应用 | 各家 LLM 官方 docs；Hugging Face 课程（有基础后） |
| 包管理 | pip 用户指南；了解 `uv` / `poetry`（中后期） |

### 7.5 社区与答疑

| 渠道 | 说明 |
|------|------|
| Stack Overflow | 英文报错检索首选 |
| 中文：SegmentFault / 掘金 / 知乎专栏 | 注意筛选年份与版本 |
| Reddit r/learnpython | 学习路径讨论 |
| GitHub | 读优秀小项目源码 |

搜报错时：`错误关键词 + Python`，并注意 Python 版本是否匹配。

---

## 八、速查：必须死磕的语法清单

下面这些建议达到「不看也能写」：

```python
# 1. f-string
name = "Ada"
print(f"Hello, {name}!")

# 2. 列表与切片
nums = [1, 2, 3, 4]
print(nums[0], nums[-1], nums[1:3])

# 3. 字典
user = {"id": 1, "name": "Ada"}
print(user.get("email", "N/A"))

# 4. 遍历
for i, x in enumerate(nums):
    print(i, x)

for k, v in user.items():
    print(k, v)

# 5. 推导式
squares = [x * x for x in range(10) if x % 2 == 0]

# 6. 函数与类型注解（注解可选但推荐）
def average(scores: list[float]) -> float:
    return sum(scores) / len(scores) if scores else 0.0

# 7. 安全读写
from pathlib import Path
import json

path = Path("data.json")
data = json.loads(path.read_text(encoding="utf-8"))
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# 8. 异常
try:
    value = int("x")
except ValueError as e:
    print("转换失败", e)

# 9. 虚拟环境里用第三方库
# pip install requests
import requests
r = requests.get("https://httpbin.org/get", timeout=10)
print(r.status_code)
```

---

## 九、能力自评表（定期打勾）

### 初级（速成通过线）

- [ ] 会安装 Python、跑脚本、用 venv
- [ ] 熟练使用 list / dict / 函数 / if / for
- [ ] 会读写文件与 JSON
- [ ] 会读 Traceback 并修复常见错误
- [ ] 会用 `pip` 安装库并写最小 demo

### 中级

- [ ] 能拆分模块、写简单类
- [ ] 会写基础单元测试
- [ ] 能独立完成一个中型项目（有 README）
- [ ] 会查官方文档解决新库问题
- [ ] 理解可变性、引用、浅拷贝/深拷贝的基本区别

### 高级（按方向）

- [ ] 异步 / 并发中至少深入一种
- [ ] 能做性能分析与简单优化
- [ ] 能读中等规模开源项目
- [ ] 有可展示的完整作品（部署或完整本地交付）

---

## 十、推荐最小工具栈（避免版本焦虑）

| 用途 | 推荐 |
|------|------|
| 语言 | Python 3.12 |
| 编辑器 | VS Code |
| 环境 | `venv`（入门）→ 以后可换 `uv` |
| 包安装 | `pip` |
| 测试 | `pytest` |
| 格式化（可选） | `ruff` 或 `black` |
| 笔记本（数据） | Jupyter |

先别同时折腾一堆脚手架；**会写 `.py` + venv + pip** 就够开始项目。

---

## 十一、30 天极速版（时间紧时用）

| 天数 | 内容 |
|------|------|
| 1～2 | 环境 + print/变量/if/for + 5 道小练习 |
| 3～5 | 列表、字典、函数；做猜数字 + 通讯录字典版 |
| 6～8 | 文件、JSON、异常；做「本地笔记/待办」 |
| 9～10 | venv、pip、requests；调用一个公开 API |
| 11～15 | 选方向：自动化 **或** pandas **或** FastAPI，只跟官方教程 |
| 16～25 | 做一个完整小项目（有输入输出与 README） |
| 26～30 | 重构、补测试、写学习笔记、复盘错题本 |

---

## 十二、文档使用建议（本仓库）

本仓库实际结构（请按这个走，不要再用旧的根目录平铺笔记）：

```
learn_python/
├── README.md                 # 总入口
├── progress.md               # 进度勾选
├── docs/roadmap.md           # 本文件
├── stage-0-setup/            # 环境
├── stage-1-basics/           # notes + exercises + solutions
├── stage-2-stdlib/
├── stage-3-engineering/
├── stage-4-tracks/           # 各方向 README + starter/
├── stage-5-projects/         # 实战笔记 + 项目规格
├── notes/                    # 你的学习日记（模板 _template.md）
├── bugs/                     # 踩坑记录
└── projects/                 # 你自己的项目代码
```

| 你想… | 去这里 |
|--------|--------|
| 从头学 | [../stage-0-setup/README.md](../stage-0-setup/README.md) |
| 做语法练习 | [../stage-1-basics/exercises/](../stage-1-basics/exercises/) |
| 自检对不对 | `python 某练习.py --check` |
| 选方向试跑 | [../stage-4-tracks/](../stage-4-tracks/README.md) 下各 `starter/` |
| 做完整项目 | [../stage-5-projects/exercises/](../stage-5-projects/exercises/) → 代码放 [../projects/](../projects/) |
| 记笔记/踩坑 | [../notes/_template.md](../notes/_template.md)、[../bugs/_template.md](../bugs/_template.md) |

每完成一个阶段，在 `notes/` 写一篇：

1. 学了什么  
2. 写了什么代码  
3. 卡在哪里、怎么解决  

**记住**：资源再多，也不如「一个能跑的小项目」。从今天起，先跑通 [stage-0](../stage-0-setup/README.md)，再做 [stage-1 ex01](../stage-1-basics/exercises/ex01_guess_number.py)。

---

## 附录 A：常见报错怎么读

```text
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    print(data["name"])
KeyError: 'name'
```

阅读顺序：

1. **最后一行**：异常类型 + 信息（`KeyError: 'name'`）
2. **从上往下**看调用栈，找到你自己写的文件行号
3. 定位：字典里没有 `'name'` 这个键

---

## 附录 B：下一步可以写什么项目（选题池）

1. 命令行待办清单（增删改查 + JSON 持久化）  
2. 个人记账本（分类统计）  
3. 文件夹整理器（按扩展名归档）  
4. 天气查询 CLI（公开 API）  
5. Markdown 笔记搜索工具  
6. CSV 清洗与报表导出  
7. 简易 REST API（FastAPI）  
8. 单词背诵默写小程序  

---

## 附录 C：版本与日期

| 项 | 内容 |
|----|------|
| 文档主题 | Python 速成学习路线与资源 |
| 面向 | 零基础到可独立做小项目 |
| 建议 Python 版本 | 3.10+ 可学；推荐 3.11/3.12 |
| 仓库形态 | 分阶段 `stage-*` 自学跟练（A1：笔记可有示例，练习独立完成） |
| 维护建议 | 方向资源随官方文档更新；路线骨架可长期沿用 |

---

**最后一句话**：Python 速成不是「看完一门课」，而是「尽快获得反馈循环」——写代码 → 报错 → 查文档 → 再写。从阶段 1 的第一个练习开始，比收藏一百个链接更重要。
