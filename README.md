# Python 速成学习仓库

从零基础到能独立完成小项目的 **自学跟练型** 仓库（MIT License）。

> 笔记里有完整示例；练习在 `exercises/` 完成，做完再看 `solutions/`。  
> 学习地图（笔记↔练习）：[docs/learning-map.md](docs/learning-map.md)

## 你将获得

- 分阶段路径、主题笔记、难度与时长标注  
- 可自检练习（`--check` / pytest）+ 参考答案  
- 四方向 starter + 中型 demo  
- 三个综合项目（`projects/`）  
- FAQ、Windows 专文、一键自检脚本  

## 环境要求

- Python **3.10+** 可学（推荐 3.11 / 3.12）  
- 编辑器：VS Code + Python 扩展，或 PyCharm Community  
- Git  

```bash
py -3 --version
# 或 python --version
```

Windows 细节：[docs/windows-setup.md](docs/windows-setup.md)

## 怎么学

```
1. docs/roadmap.md 与 docs/learning-map.md
2. stage-0 → stage-3（语法 + 标准库 + 工程）
3. stage-4 选一条方向：starter → demo
4. stage-5 / projects/ 做完整项目
5. progress.md 打勾 · bugs/ 记坑 · notes/ 写日记
```

阶段内：`读 notes/` → `做 exercises/` → `python xxx.py --check` → `对照 solutions/`

**先别抄 solutions。** 错题见 [docs/faq-common-mistakes.md](docs/faq-common-mistakes.md)。

## 快速开始

```bash
cd learn_python
py -3 -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

py -3 stage-0-setup/hello.py
py -3 scripts/check_all.py
```

## 仓库结构

```
learn_python/
├── README.md / LICENSE / CONTRIBUTING.md
├── progress.md
├── requirements-dev.txt
├── scripts/check_all.py
├── docs/          # roadmap · learning-map · FAQ · windows-setup
├── stage-0-setup/ … stage-5-projects/
├── notes/ · bugs/ · projects/
└── .github/workflows/ci.yml
```

| 阶段 | 目录 | 内容 |
|------|------|------|
| 0 | [stage-0-setup](stage-0-setup/README.md) | 安装、编码、hello |
| 1 | [stage-1-basics](stage-1-basics/README.md) | 语法 · 6 题 |
| 2 | [stage-2-stdlib](stage-2-stdlib/README.md) | 文件/模块/OOP · 6 题 |
| 3 | [stage-3-engineering](stage-3-engineering/README.md) | venv/测试/Git · 进阶笔记 |
| 4 | [stage-4-tracks](stage-4-tracks/README.md) | 自动化/数据/Web/AI |
| 5 | [stage-5-projects](stage-5-projects/README.md) | 项目规格 · 实现在 projects/ |

完整路线：[docs/roadmap.md](docs/roadmap.md)

## 项目一览

| 项目 | 路径 |
|------|------|
| 待办 CLI | [projects/todo-cli](projects/todo-cli/) |
| 文件整理 | [projects/file-organizer](projects/file-organizer/) |
| API CLI | [projects/api-cli](projects/api-cli/) |

## 约定（A1）

1. 笔记可含完整示例  
2. 练习可自检，答案在 `solutions/`  
3. 个人项目与密钥不进 Git（见 `.gitignore`）  

## 贡献与许可

- [CONTRIBUTING.md](CONTRIBUTING.md)  
- [LICENSE](LICENSE)（MIT）  

推送到 GitHub（可选）：

```bash
gh repo create learn_python --public --source=. --remote=origin --push
# 或手动添加 remote 后 git push -u origin main
```
