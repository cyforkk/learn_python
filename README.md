# Python 速成学习仓库

**先学笔记 → 再做练习 → 再做项目** 的自学仓库（MIT License）。

> **默认已装好 Python 3.10+**。环境不是主线；卡住再查 [stage-0-setup](stage-0-setup/README.md)。  
> **不要一上来就刷题。** 正确顺序是：读文章 → 动手题 → 综合项目。

学习地图：[docs/learning-map.md](docs/learning-map.md) · 练习原则：[docs/exercise-policy.md](docs/exercise-policy.md)（**不是每篇都有题**）

## 学习顺序（必读）

```
① 学：打开 stage-N/notes/ 按阅读顺序读文章（可运行文中示例）
② 练：再打开 exercises/ 做题，python xxx.py --check 自检
③ 对：做完再看 solutions/（禁止先抄答案）
④ 项：阶段后期或 stage-5 做 projects/
⑤ 勾：progress.md 打勾，bugs/ 记坑
```

| 阶段在干什么 | 先打开哪里 |
|--------------|------------|
| 学概念 | `stage-*/notes/*.md`（**第一站**） |
| 巩固 | `stage-*/exercises/` |
| 对照 | `stage-*/solutions/` |
| 作品 | `projects/`、stage-5 规格 |

## 前提

```bash
python --version   # 或 py -3 --version  → 3.10+
```

## 怎么学（全局）

```
1. 读 docs/roadmap.md 或 docs/learning-map.md（建立全局感）
2. stage-1 → stage-3：每个阶段都是「笔记读完 → 再练习」
3. stage-4：读该方向 path-*.md 路线 → starter/demo → 自选项目
4. stage-5：读实战笔记/规格 → 在 projects/ 交付
```

错题：[docs/faq-common-mistakes.md](docs/faq-common-mistakes.md)

## 快速开始（从「学」开始）

```bash
cd learn_python

# 1）先读第一篇笔记（浏览器或编辑器打开）
#    stage-1-basics/notes/Python基本数据类型.md  （只了解，无容器题）

# 2）按 stage-1-basics/README.md 阅读顺序读笔记
# 3）读完「条件与循环」后再做题（建议第一题九九表，不是成绩字典）
#    见 stage-1-basics/exercises/新手怎么做.md
```

第一天建议：基本类型**扫一眼** → 输入输出 → 条件与循环 → **九九表**。  
成绩字典要等 **复合类型** 笔记后再做。

## 你将获得

- 分阶段 **讲解笔记** + 练习与参考答案  
- 四方向学习路线 + starter/demo + GitHub 清单  
- 综合项目与 FAQ

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
