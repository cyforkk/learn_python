# Python 速成学习仓库

从零基础到能独立完成小项目的 **自学跟练型** 仓库。

> 笔记里有完整示例，方便理解；练习在 `exercises/` 独立完成，做完再看 `solutions/`。

## 你将获得

- 按阶段划分的学习路径与主题笔记
- 可动手写的练习骨架 + 参考答案
- 进度勾选、踩坑记录、个人项目工作区

## 环境要求

- Python **3.11+**（推荐 3.12）
- 编辑器：VS Code（装 Python 扩展）或 PyCharm Community
- Git（本仓库已是 Git 项目）

验证：

```bash
python --version
# 或 Windows
py --version
```

## 怎么学（推荐顺序）

```
1. 读 docs/roadmap.md          → 建立全局感
2. 从 stage-0 做到 stage-3     → 语法 + 标准库 + 工程习惯
3. stage-4 选一条方向深挖
4. stage-5 / projects/         → 做完整小项目
5. 随时在 progress.md 打勾，bugs/ 记坑
```

每个阶段内部：

```
读 notes/  →  做 exercises/  →  对照 solutions/  →  progress.md 勾选
```

**不要**一上来就抄 `solutions/`；笔记示例可以看，练习请自己写。

## 仓库结构

```
learn_python/
├── README.md                 # 本文件
├── progress.md               # 进度清单
├── docs/roadmap.md           # 完整学习路线与资源
├── stage-0-setup/            # 环境准备
├── stage-1-basics/           # 语法核心
├── stage-2-stdlib/           # 文件 / 异常 / 模块 / 标准库 / OOP
├── stage-3-engineering/      # venv / 风格 / 测试 / 调试 / Git
├── stage-4-tracks/           # 方向：自动化 / 数据 / Web / AI
├── stage-5-projects/         # 综合实战说明与项目规格
├── notes/                    # 你的学习日记
├── bugs/                     # 踩坑记录
└── projects/                 # 你自己的项目代码
```

每个 `stage-N`（1～3、5）大致包含：

| 目录 | 作用 |
|------|------|
| `notes/` | 主题讲解 + 完整示例 |
| `exercises/` | 题目与待完成 `.py` 骨架 |
| `solutions/` | 参考答案（做完再看） |

## 快速开始

```bash
# 克隆或进入本仓库后
cd learn_python

# 建议创建虚拟环境（stage-3 会系统学习）
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# 从阶段 0 开始
# 打开 stage-0-setup/README.md
```

第一行代码：创建任意文件试跑：

```python
print("Hello, Python!")
```

```bash
python hello.py
```

## 阶段导航

| 阶段 | 目录 | 目标 |
|------|------|------|
| 0 | [stage-0-setup](stage-0-setup/README.md) | 安装、跑通脚本 |
| 1 | [stage-1-basics](stage-1-basics/README.md) | 语法核心，能写小脚本 |
| 2 | [stage-2-stdlib](stage-2-stdlib/README.md) | 文件、异常、模块、OOP 入门 |
| 3 | [stage-3-engineering](stage-3-engineering/README.md) | 工程习惯：venv、测试、调试、Git |
| 4 | [stage-4-tracks](stage-4-tracks/README.md) | 选方向深挖 |
| 5 | [stage-5-projects](stage-5-projects/README.md) | 综合项目 |

完整路线、资源列表、30 天计划见：[docs/roadmap.md](docs/roadmap.md)

## 进度与记录

- [progress.md](progress.md) — 勾选完成情况
- [notes/_template.md](notes/_template.md) — 学习日记模板
- [bugs/_template.md](bugs/_template.md) — 踩坑模板

## 约定（A1）

1. **笔记**：可含完整示例代码，用于理解概念  
2. **练习**：另一套题，骨架里只有要求，没有完整实现  
3. **答案**：与练习同名，位于 `solutions/`，用于对照而非抄袭  

## 贡献 / 自用建议

- 个人练习代码可直接改 `exercises/` 下的文件  
- 完整项目请放到 `projects/你的项目名/`  
- 提交 Git 时避免把 `.venv`、密钥、大数据文件推上去（已在 `.gitignore`）

---

从 [stage-0-setup](stage-0-setup/README.md) 开始，或先通读 [docs/roadmap.md](docs/roadmap.md)。
