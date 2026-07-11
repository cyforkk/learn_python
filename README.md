# Python 速成学习仓库

用练习和项目巩固 Python 的 **自学跟练型** 仓库（MIT License）。

> **默认你已经装好 Python 3.10+**，会在终端运行 `python` / `py`。  
> 不把「装环境」当主线——卡住时再查可选附录即可。

> 笔记里有完整示例；练习在 `exercises/` 完成，做完再看 `solutions/`。  
> 学习地图：[docs/learning-map.md](docs/learning-map.md)

## 你将获得

- 分阶段路径、主题笔记、练习与参考答案  
- 四方向学习路线 + starter/demo + GitHub 清单  
- 综合项目与 FAQ  

## 前提（默认已满足）

```bash
python --version   # 或 py -3 --version  → 3.10+
```

装不上、PATH 乱、编码问题 → 再看可选文档 [stage-0-setup](stage-0-setup/README.md) / [docs/windows-setup.md](docs/windows-setup.md)（**可整段跳过**）。

## 怎么学

```
1. docs/roadmap.md 或 docs/learning-map.md
2. stage-1 → stage-3（语法 → 标准库 → 工程习惯）
3. stage-4 选一条方向（已有基础可直接进）
4. stage-5 / projects/ 做完整项目
5. progress.md 打勾
```

阶段内：`读 notes/` → `做 exercises/` → `python xxx.py --check` → 对照 `solutions/`

**先别抄 solutions。** 错题：[docs/faq-common-mistakes.md](docs/faq-common-mistakes.md)。

## 快速开始

```bash
cd learn_python

# 直接开练（已有 Python 即可）
cd stage-1-basics/exercises
python ex01_guess_number.py --check

# 可选：装开发依赖并一键自检
# pip install -r requirements-dev.txt
# python scripts/check_all.py
```

`venv` 等在 **stage-3** 系统学；平时本地有 Python 就能做练习。

## 仓库结构

```
learn_python/
├── README.md · progress.md · docs/
├── stage-1-basics/ … stage-5-projects/   # 主线
├── stage-0-setup/                        # 可选：环境附录
├── notes/ · bugs/ · projects/
└── scripts/check_all.py
```

| 阶段 | 目录 | 内容 |
|------|------|------|
| ~~0~~ | [stage-0-setup](stage-0-setup/README.md) | **可选**环境附录（默认可跳过） |
| 1 | [stage-1-basics](stage-1-basics/README.md) | 语法 · 练习 |
| 2 | [stage-2-stdlib](stage-2-stdlib/README.md) | 文件/模块/OOP |
| 3 | [stage-3-engineering](stage-3-engineering/README.md) | venv/测试/Git（需要时再学） |
| 4 | [stage-4-tracks](stage-4-tracks/README.md) | [方向路线](docs/stage4-paths/README.md) · [GitHub](docs/stage4-github-projects.md) |
| 5 | [stage-5-projects](stage-5-projects/README.md) | 项目规格 · `projects/` |

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
