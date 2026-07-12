# Python 虚拟环境：为什么需要它，怎么用它

## 核心问题：依赖冲突

假设你有两个项目：A 项目依赖 Django 3.x，B 项目依赖 Django 4.x。如果都装在全局 Python 环境里，版本就会打架，只能留一个。**虚拟环境就是解决这个问题的**——给每个项目创建一个独立的 Python 运行空间，各项目装的库互不干扰。

## 虚拟环境是什么

虚拟环境本质上是一个**独立的 Python 运行目录**，里面有自己独立的解释器副本和独立的第三方包安装目录。激活某个虚拟环境后，你用 `pip install` 装的包只会装到这个目录里，不会污染全局环境，也不会被其他项目的包影响。

它不复制整个 Python 安装，只是创建一个轻量的隔离层，所以创建速度很快，占用空间也不大。

## 怎么用

Python 自带的 `venv` 模块就能创建虚拟环境，一行命令：

通用语法：

```bash
python -m venv <环境名>
```

具体示例：

```bash
python -m venv .venv
```

创建后需要**激活**才能生效：

Windows 上：

通用语法：

```bash
<环境名>\Scripts\activate
```

具体示例：

```bash
.venv\Scripts\activate
```

macOS / Linux 上：

通用语法：

```bash
source <环境名>/bin/activate
```

具体示例：

```bash
source .venv/bin/activate
```

激活后你会看到命令行前面多了 `(.venv)` 标志，说明你已经在虚拟环境里了。这时候用 `pip install` 装的包都会装到这个环境里。

退出虚拟环境，运行：

```bash
deactivate
```

## 为什么都用 .venv 这个名字

你可能注意到，大多数教程和项目都用 `.venv` 作为虚拟环境名，这不是巧合，而是有几个实际好处：

**隐藏目录，保持项目整洁。** 在 macOS 和 Linux 上，以 `.` 开头的目录默认不在文件管理器和 `ls` 输出中显示。项目目录里只看到代码和配置文件，不会被虚拟环境里的几百个包文件干扰。Windows 上虽然没有隐藏效果，但约定俗成也跟着用 `.venv`。

**主流工具默认识别。** VS Code、PyCharm 等 IDE 看到项目目录下有 `.venv`，会**自动识别为虚拟环境**并提示选中。GitHub 默认的 `.gitignore` 模板通常已经包含 `.venv`，不会被误提交到仓库。如果叫别的名字，可能要手动配置 IDE 和 `.gitignore`。

**名字本身就是一个信号。** `.venv` 一眼就能看出是虚拟环境，不会跟项目里的其他文件夹混淆。

所以 `.venv` 不是技术要求，而是一个**社区约定**，用它能省掉不少配置上的麻烦。

## 常用操作

| 操作 | 命令 |
|---|---|
| 创建虚拟环境 | `python -m venv .venv` |
| 激活（Windows） | `.venv\Scripts\activate` |
| 激活（macOS/Linux） | `source .venv/bin/activate` |
| 退出虚拟环境 | `deactivate` |
| 查看已装包 | `pip list` |
| 导出依赖清单 | `pip freeze > requirements.txt` |
| 按清单安装 | `pip install -r requirements.txt` |

导出依赖和按清单安装的通用语法：

```bash
# 通用语法
pip freeze > <输出文件>
pip install -r <依赖清单文件>

# 具体示例
pip freeze > requirements.txt
pip install -r requirements.txt
```

**导出依赖清单**这一步很关键——别人拿到你的项目后，只需要一条 `pip install -r requirements.txt` 就能还原出完全一致的依赖环境。

## 和包管理工具的关系

虚拟环境和包管理工具分工不同：**虚拟环境管隔离，包管理工具管安装**。两者配合使用才是完整方案。

pip + venv 是最常见的组合，但需要手动管理两件事。Poetry 和 uv 把虚拟环境管理和包安装整合到一个工具里，自动创建和激活，体验更顺畅。Conda 则自带环境管理能力，`conda create -n 环境名` 就能创建独立环境。

## 一句话总结

**每个项目用独立的虚拟环境，是 Python 开发的最基本的习惯。** 不管你用 venv、Poetry、uv 还是 Conda，核心目的都一样——把项目的依赖隔离开，避免互相打架。

---

## 本仓库练习（只列题目 · 步骤在链接里）

### 建议 · 虚拟环境实践

**题目：** 创建 venv、激活、安装一个小包、知道 `.venv` 不要提交 Git。  

**作业（按步骤做）：** [ex01_venv_practice.md](../exercises/ex01_venv_practice.md)
