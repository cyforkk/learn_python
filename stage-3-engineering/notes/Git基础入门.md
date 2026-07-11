# Git 基础：从 add 到 push 的工作流

写代码最怕的不是 bug，而是"改坏了回不去"。手动复制文件夹做备份？文件一多就乱。**Git 是代码版本管理工具，记录每次修改的历史，随时可以回退到任意版本**。团队协作时，Git 还负责合并多人的代码，避免互相覆盖。

Git 的核心工作流就三步：**add 把改动加入暂存区，commit 把暂存区拍一个快照，push 把快照推到远程仓库**。理解这三步，日常使用就够了。

## 核心概念

### 三个区域

Git 有三个关键区域，理解它们的关系就理解了 Git 的工作流：

**工作区（Working Directory）** — 你在编辑器里看到的实际文件。你改了代码，文件变了，这些改动就在工作区。

**暂存区（Staging Area）** — 改动文件的"候车区"。你用 `git add` 把工作区的改动放进来，准备打包提交。

**仓库（Repository）** — 用 `git commit` 把暂存区的改动拍一个快照，永久记录到版本历史中。

数据流向：

```
工作区 ──git add──→ 暂存区 ──git commit──→ 本地仓库 ──git push──→ 远程仓库
                     ↑
                     │
              git commit 把这里的改动打包
```

**为什么要分暂存区？** 因为你可能同时改了 5 个文件，但只想提交其中 3 个。暂存区让你精确控制每次提交包含哪些改动，而不是一股脑全提交。

### 远程仓库

远程仓库是存放在服务器上的代码仓库（GitHub、GitLab、Gitee 等）。本地仓库只在你电脑上，`git push` 把本地提交推到远程，`git pull` 把远程的更新拉到本地。

## 初始化与配置

### 安装后的一次性配置

**语法结构：** `git config --global user.属性 "值"`

```bash
# 语法
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 示例
git config --global user.name "张三"
git config --global user.email "zhangsan@example.com"
```

安装 Git 后第一次使用时配置一次就行。名字和邮箱会记录在每次提交中，团队协作时别人能看到是谁提交的。

验证配置：

```bash
git config --list
```

### 初始化仓库

**语法结构：** `git init [仓库名]`

```bash
# 在当前目录初始化
git init

# 在指定目录创建新仓库
git init my_project
```

执行后当前目录会多一个 `.git` 隐藏文件夹，Git 的所有版本数据都存在这里面。**不要手动改 `.git` 里的文件**，损坏了版本历史就没了。

### 克隆远程仓库

**语法结构：** `git clone 仓库地址 [本地目录名]`

```bash
# 语法
git clone <远程仓库地址>

# 示例
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git my_folder    # 克隆到指定目录
```

`git clone` 一次性完成：下载远程仓库全部历史记录 + 创建本地仓库 + 关联远程地址。如果项目已经存在于远程，克隆就够了，不需要 `git init`。

## add — 把改动加入暂存区

### 基本语法

**语法结构：** `git add 文件路径`

```bash
# 添加单个文件
git add README.md

# 添加多个文件
git add file1.py file2.py

# 添加当前目录下所有改动
git add .

# 添加某个目录下所有改动
git add src/
```

`git add` 把工作区的改动复制到暂存区。**不会提交，只是标记"这些改动我准备提交"**。

### 查看状态

**语法结构：** `git status`

```bash
git status
```

`git status` 是最常用的查看命令，告诉你：

```
On branch main
Changes to be committed:        ← 暂存区（即将被 commit）
  modified:   src/main.py

Changes not staged for commit:  ← 工作区改了但没 add
  modified:   src/utils.py

Untracked files:                ← 新文件，Git 还不认识
  src/new_module.py
```

三种状态对应三个操作：

| 状态 | 含义 | 下一步 |
|---|---|---|
| Changes to be committed | 已暂存，准备提交 | `git commit` |
| Changes not staged for commit | 改了但没暂存 | `git add` 加入暂存 |
| Untracked files | 新文件，未被 Git 跟踪 | `git add` 开始跟踪 |

**养成习惯：commit 前先 `git status` 看一眼，确认暂存区里是你要提交的内容。**

### 添加改动的策略

```bash
# 只添加修改和删除的文件，不包括新文件
git add -u

# 添加所有改动（修改、删除、新增）
git add .

# 交互式选择添加哪些改动（按文件块）
git add -p
```

`git add -p` 会逐块展示你的改动，按 `y` 加入暂存、`n` 跳过。一个文件里改了多处，只想提交其中一部分时用这个。

## commit — 把暂存区打包成快照

### 基本语法

**语法结构：** `git commit -m "提交说明"`

```bash
# 语法
git commit -m "提交说明"

# 示例
git commit -m "修复用户登录失败的bug"
git commit -m "添加用户注册功能"
```

`git commit` 把暂存区的所有改动拍一个快照，永久记录到版本历史。`-m` 后面跟提交说明，简明描述这次改了什么。

### 写好的提交说明

提交说明要**说清楚做了什么**，不要写"修改"或"更新"这种废话：

```bash
# 不好：不知道改了什么
git commit -m "修改"

# 不好：太模糊
git commit -m "更新代码"

# 好：动宾结构，一目了然
git commit -m "修复用户登录失败的bug"
git commit -m "添加用户注册接口"
git commit -m "重构数据库连接逻辑"
```

### 跳过暂存区

**语法结构：** `git commit -am "提交说明"`

```bash
# 只对已跟踪的文件有效，新文件不会自动包含
git commit -am "修复bug"
```

`-a` 参数跳过 `git add`，直接提交所有已跟踪文件的修改。**新文件（Untracked）不会被包含**，必须先 `git add`。这是一个快捷写法，但失去了精确控制暂存区的优势。

### 查看提交历史

**语法结构：** `git log [--oneline] [-n 数量]`

```bash
# 查看完整历史
git log

# 简洁模式，每条一行
git log --oneline

# 只看最近 5 条
git log --oneline -n 5
```

`--oneline` 模式输出：

```
a1b2c3d 修复用户登录失败的bug
e4f5g6h 添加用户注册功能
i7j8k9l 初始化项目
```

前面那串是 commit ID（哈希值），Git 用它定位每一次提交。

### 修改最近一次提交

**语法结构：** `git commit --amend -m "新说明"`

```bash
# 改提交说明
git commit --amend -m "修复用户登录失败的bug（含测试）"

# 追加文件到上一次提交
git add forgot_file.py
git commit --amend --no-edit    # 保持原说明不变
```

`--amend` 修改最近一次提交。发现刚提交的说明写错了、或者漏了一个文件，用这个修补，不用新开一个提交。

**注意：** `--amend` 会改写历史。如果这次提交已经 push 到远程，不要随便 amend，否则别人 pull 会出冲突。

## push — 推送到远程仓库

### 基本语法

**语法结构：** `git push [远程名] [分支名]`

```bash
# 语法
git push <远程名> <分支名>

# 示例
git push origin main
```

`origin` 是远程仓库的默认名称（克隆时自动设置），`main` 是分支名。这条命令把本地的 `main` 分支推到 `origin` 对应的远程仓库。

### 首次推送

如果是本地新建的仓库，第一次推送到远程时需要建立关联：

**语法结构：** `git push -u <远程名> <分支名>`

```bash
# 先添加远程地址
git remote add origin https://github.com/user/repo.git

# 第一次推送，-u 建立关联
git push -u origin main
```

`-u`（全称 `--set-upstream`）把本地 `main` 和远程 `origin/main` 关联起来。之后直接 `git push` 就行，不用再写 `origin main`。

### 后续推送

```bash
# 已关联远程分支后，直接 push
git push
```

### 添加远程地址

**语法结构：** `git remote add <名称> <地址>`

```bash
# 语法
git remote add <远程名> <远程仓库地址>

# 示例
git remote add origin https://github.com/zhangsan/my_project.git
```

查看已配置的远程地址：

```bash
git remote -v
```

## pull — 拉取远程更新

团队协作时别人推了新代码，你需要拉到本地：

**语法结构：** `git pull [远程名] [分支名]`

```bash
# 语法
git pull <远程名> <分支名>

# 示例
git pull origin main

# 已关联分支后直接 pull
git pull
```

`git pull` 等价于 `git fetch` + `git merge`：先下载远程的更新，再合并到当前分支。**每天开始工作前先 `git pull`，拉取别人的最新代码**，避免后面冲突。

## 完整工作流

从零开始的一个完整流程：

```bash
# 1. 克隆仓库（或 git init + git remote add）
git clone https://github.com/zhangsan/my_project.git
cd my_project

# 2. 写代码（编辑器里改文件）
#    ... 修改 src/main.py ...

# 3. 查看改了什么
git status
git diff                    # 查看具体改动内容

# 4. 暂存改动
git add src/main.py

# 5. 提交
git commit -m "添加用户登录功能"

# 6. 拉取远程更新（别人可能推了新代码）
git pull

# 7. 推送到远程
git push
```

**日常开发就是反复循环 3-7 步：改代码 → add → commit → pull → push。**

## 其他常用命令

### git diff — 查看改动内容

**语法结构：** `git diff [文件路径]`

```bash
# 查看工作区未暂存的改动
git diff

# 查看已暂存但未提交的改动
git diff --staged

# 查看某个文件的改动
git diff src/main.py
```

### git checkout — 撤销改动

**语法结构：** `git checkout -- <文件路径>`

```bash
# 撤销工作区的修改（回到上次 commit 的状态）
git checkout -- src/main.py

# 撤销所有工作区修改
git checkout -- .
```

**注意：** 撤销后改动不可恢复。确认不需要了再撤销。

### git reset — 撤销暂存

**语法结构：** `git reset <文件路径>`

```bash
# 把文件从暂存区移回工作区
git reset src/main.py

# 撤销所有暂存
git reset
```

`git reset` 只是把改动从暂存区移出，**不会丢失文件内容**，改动还在工作区。

### git rm — 删除文件

**语法结构：** `git rm <文件路径>`

```bash
git rm old_file.py
git commit -m "删除无用文件"
```

`git rm` 同时从文件系统和 Git 跟踪中删除文件。需要 commit 才生效。

### git mv — 重命名文件

**语法结构：** `git mv <旧路径> <新路径>`

```bash
git mv old_name.py new_name.py
git commit -m "重命名 old_name 为 new_name"
```

### .gitignore — 忽略文件

有些文件不想纳入版本管理（临时文件、密码配置、虚拟环境等），用 `.gitignore` 文件指定忽略规则：

```
# .gitignore 文件内容

# 忽略所有 .pyc 文件
*.pyc

# 忽略虚拟环境目录
.venv/
venv/

# 忽略 IDE 配置
.vscode/
.idea/

# 忽略环境变量文件
.env

# 忽略日志
*.log

# 忽略构建产物
dist/
build/
```

**`.gitignore` 本身要纳入版本管理**，和项目代码一起提交。

## 速查表

| 操作 | 命令 |
|---|---|
| 初始化仓库 | `git init` |
| 克隆仓库 | `git clone <地址>` |
| 配置用户名 | `git config --global user.name "名字"` |
| 查看状态 | `git status` |
| 查看改动 | `git diff` |
| 暂存改动 | `git add <文件>` |
| 暂存所有改动 | `git add .` |
| 提交 | `git commit -m "说明"` |
| 跳过暂存提交 | `git commit -am "说明"` |
| 修改最近提交 | `git commit --amend -m "新说明"` |
| 查看历史 | `git log --oneline` |
| 推送 | `git push` |
| 首次推送 | `git push -u origin main` |
| 拉取 | `git pull` |
| 撤销工作区修改 | `git checkout -- <文件>` |
| 撤销暂存 | `git reset <文件>` |
| 添加远程 | `git remote add origin <地址>` |
| 查看远程 | `git remote -v` |
| 删除文件 | `git rm <文件>` |
| 重命名文件 | `git mv <旧名> <新名>` |

## 要点

Git 的核心工作流就三步：**add 暂存改动、commit 拍快照、push 推到远程**。工作区是你在改的文件，暂存区是准备提交的改动，本地仓库是已提交的快照历史。每次改完代码先 `git status` 看状态，`git add` 暂存要提交的部分，`git commit -m` 写清楚改了什么，`git pull` 同步别人的更新，`git push` 推到远程。提交说明要写具体做了什么，不要写"修改"这种废话。`.gitignore` 文件指定忽略哪些文件。记住这个循环：**改代码 → add → commit → pull → push**，日常开发 80% 的 Git 操作都在这里面。

---

## 本仓库学习导航
在本仓库练习 add/commit；见根目录 CONTRIBUTING.md
