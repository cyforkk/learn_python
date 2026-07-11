# Python 包管理工具：对比与选择

写 Python 代码时，你几乎一定会用到别人写好的库。包管理工具解决的核心问题就一个：**帮你安装、管理、锁定第三方依赖**，让代码在不同环境下都能稳定运行。

Python 生态里包管理工具不少，下面逐一对比，帮你找到适合自己场景的那一个。

## pip：默认选择

pip 是 Python 官方的包管理工具，从 **Python 2.7.9** 和 **Python 3.4** 开始默认随 Python 一起安装。从 python.org 下载安装 Python 时，pip 会自动包含在内。

少数情况下 pip 可能不存在：老旧版本、精简安装，或某些 Linux 发行版（如 Ubuntu 需手动 `sudo apt install python3-pip`）。这时可以用 `python -m ensurepip` 引导安装。

验证是否已安装：运行 `pip --version` 即可。

**优点：** 官方标配，几乎所有 Python 环境都有；学习成本低，命令简单；社区资源丰富，遇到问题容易找到答案。

**缺点：** 依赖解析不够严格，容易产生版本冲突；没有锁文件机制，难以保证团队成员环境一致；不管理虚拟环境，需要配合 `venv` 单独处理。

### 常用命令语法

```bash
# 通用语法
pip install <包名>                 # 安装包
pip install <包名>==<版本号>       # 安装指定版本
pip uninstall <包名>              # 卸载包
pip list                          # 查看已安装的包
pip freeze > requirements.txt     # 导出依赖清单
pip install -r requirements.txt  # 按清单安装依赖

# 具体示例
pip install requests
pip install requests==2.28.0
pip uninstall requests
```

## Poetry：现代化项目管理的标配

集**依赖管理、虚拟环境管理、打包发布**于一体，用 `pyproject.toml` 和 `poetry.lock` 锁定版本，依赖解析比 pip 严格得多。

**优点：** 依赖解析准确，锁文件保证团队环境一致；自动管理虚拟环境，不需要手动激活；打包发布流程完整，一条命令搞定构建和上传。

**缺点：** 学习曲线比 pip 陡；对部分老旧项目和非标准包的兼容性偶尔有问题；安装和运行速度不算快。

### 常用命令语法

```bash
# 通用语法
poetry init                      # 初始化项目，生成 pyproject.toml
poetry add <包名>                 # 添加依赖
poetry add <包名>==<版本号>       # 添加指定版本
poetry remove <包名>              # 移除依赖
poetry install                    # 按 poetry.lock 安装全部依赖

# 具体示例
poetry add requests
poetry add requests==2.28.0
```

## uv：速度优先的新生力量

Astral 公司推出的用 **Rust** 编写的超快包管理工具，兼容 pip 的命令接口，速度比 pip 快几十倍，同时也能管理 Python 版本和虚拟环境。

**优点：** 速度极快，安装依赖几乎是秒级；兼容 pip 命令，迁移成本低；一站式管理 Python 版本、虚拟环境和依赖；自带锁文件支持。

**缺点：** 生态尚新，部分边缘场景的稳定性有待验证；社区和文档积累不如 pip 和 Poetry 成熟；部分高级功能仍在快速迭代中。

### 常用命令语法

```bash
# 通用语法
uv pip install <包名>              # 安装包
uv pip install <包名>==<版本号>     # 安装指定版本
uv pip list                        # 查看已安装的包
uv venv <环境名>                   # 创建虚拟环境

# 具体示例
uv pip install requests
uv venv .venv
```

## Conda：数据科学的专属领域

面向**数据科学和科学计算**领域，不仅能装 Python 包，还能管理非 Python 的系统级依赖（如 C 库、CUDA 等）。Anaconda 和 Miniconda 都基于它。

**优点：** 能安装非 Python 的系统级依赖，这是 pip 做不到的；预装大量数据科学常用库，开箱即用；多环境管理方便。

**缺点：** 安装包体积大，Miniconda 也要几百 MB；依赖解析速度慢，有时要等很久；与 pip 混用时容易产生冲突；对纯 Python Web 项目来说过重。

### 常用命令语法

```bash
# 通用语法
conda create -n <环境名> python=<版本号>   # 创建环境
conda activate <环境名>                    # 激活环境
conda install <包名>                       # 安装包
conda install <包名>=<版本号>              # 安装指定版本
conda env list                            # 查看所有环境

# 具体示例
conda create -n myenv python=3.11
conda activate myenv
conda install numpy
```

## 其他工具一览

**Hatch** — 由 PyPA 成员开发，偏向项目管理一体化，涵盖环境管理、构建、发布、测试脚本运行。功能全面但社区热度不高。

**PDM** — 遵循 PEP 标准，特点是**不需要虚拟环境也能隔离依赖**（利用 `__pypackages__` 机制）。技术上有创新，但采用率有限。

**pipenv** — 曾经被官方推荐过一段时间，结合 pip 和 virtualenv 的功能。近年热度明显下降，很多人转投了 Poetry 或 uv。

**Virtualenv** — 严格来说是**虚拟环境工具**而非包管理器，比 Python 自带的 `venv` 模块速度更快、功能更多，常和 pip 配合使用。

## 怎么选

| 需求场景 | 推荐工具 |
|---|---|
| 初学 Python，写简单脚本 | **pip** |
| 正式项目开发，需要管理复杂依赖 | **Poetry** 或 **uv** |
| 追求极致速度，习惯 pip 命令 | **uv** |
| 数据科学、机器学习、需要 CUDA 等 | **Conda** |

**核心原则很简单：** 初学者用 pip 就够了，正式项目上 Poetry 或 uv，数据科学选 Conda。先从一个工具用起，遇到瓶颈再换，不必纠结。

---

## 本仓库学习导航
- **练习安排：无独立新题**（与虚拟环境篇的 ex01 一起完成即可）
- 综合工程 **加练** → [ex05 迷你工程](../exercises/ex05_mini_project/)
