# 练习 01：虚拟环境与依赖清单

## 目标

在本机完整体验一次：创建 venv → 安装包 → 导出依赖 → 新人复现思路。

## 步骤

1. 在仓库根目录（或临时目录）执行：
   ```bash
   python -m venv .venv
   ```
2. 激活（Windows PowerShell）：
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
3. 安装一个小库验证：
   ```bash
   pip install requests
   python -c "import requests; print(requests.__version__)"
   ```
4. 导出依赖（任选一种理解即可）：
   ```bash
   pip freeze > requirements-lock.txt
   ```
   或手写精简版 `requirements.txt`：
   ```
   requests>=2.31.0
   ```
5. 在 `bugs/` 或 `notes/` 写 5 行记录：你执行了哪些命令、有没有报错。

## 验收

- [x] 激活后命令行提示符通常带 `(.venv)`（本仓库学习时已用过 venv / 系统 pip）
- [x] `import requests` 成功（stage-4 automation starter 已验证）
- [x] 知道 `.venv` 不应提交到 Git（见根目录 `.gitignore`）

## 注意

本练习以操作与记录为主。参考说明见 `solutions/ex01_venv_practice.md`。

完成记录见：`../../notes/2026-07-11-开练.md` 与下方简记。

### 简记

- 命令：`python -m venv .venv` → 激活 → `pip install -r requirements.txt`
- 依赖文件只提交 `requirements.txt`，不提交 `.venv`
- PowerShell 若禁止脚本：可用 `cmd` 的 `activate.bat` 或调整 ExecutionPolicy
