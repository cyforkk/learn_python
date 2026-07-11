# Windows 环境专文

> 对应阶段：[stage-0-setup](../stage-0-setup/README.md)  
> Python **3.10+** 可学，文档推荐 3.11/3.12。

## 1. 安装 Python

1. 打开 https://www.python.org/downloads/  
2. 安装时 **勾选** `Add python.exe to PATH`  
3. 验证（PowerShell 或 cmd）：

```powershell
py -3 --version
# 或
python --version
```

若提示找不到命令：重装并勾选 PATH，或注销/重启后再试。

## 2. `py` 与 `python`

| 命令 | 说明 |
|------|------|
| `py -3` | Windows 启动器，推荐 |
| `python` | 依赖 PATH；有时指向商店占位符 |

本仓库示例两种都可能出现，任选能跑的一种。

## 3. 执行策略（venv 激活失败时）

PowerShell 报错「无法加载，因为在此系统上禁止运行脚本」：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

或用 cmd：

```bat
.venv\Scripts\activate.bat
```

## 4. 虚拟环境

```powershell
cd E:\talkAI\learn_python
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements-dev.txt
```

## 5. 编码与中文

- 源文件与读写文本统一 **UTF-8**  
- `open(..., encoding="utf-8")` / `Path.read_text(encoding="utf-8")`  
- 控制台乱码时可尝试：`chcp 65001`

## 6. 编辑器

- **VS Code**：安装扩展 `Python`（Microsoft）  
- 打开仓库根目录为工作区  
- 选择解释器：`Ctrl+Shift+P` → Python: Select Interpreter → 选 `.venv`

## 7. 路径注意

- 优先 `pathlib.Path`  
- 反斜杠字符串用原始字符串：`r"C:\Users\..."`  
- 在仓库内学习时用相对路径更稳

## 8. 一键自检

```powershell
pip install -r requirements-dev.txt
python scripts/check_all.py
```
