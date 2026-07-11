# 阶段 0 · 环境准备

**目标**：能安装 Python、用编辑器写文件、在终端跑起来。  
**建议时间**：1～2 小时。

## 清单

1. 安装 [Python 3.11+](https://www.python.org/downloads/)（Windows 勾选 **Add python.exe to PATH**）
2. 验证：
   ```bash
   python --version
   # 或
   py --version
   ```
3. 安装编辑器：
   - [VS Code](https://code.visualstudio.com/) + 扩展 **Python**
   - 或 PyCharm Community
4. 在本仓库外或临时目录创建 `hello.py`：
   ```python
   print("Hello, Python!")
   ```
5. 运行：
   ```bash
   python hello.py
   ```

## 可选：虚拟环境预览

系统学习在 stage-3；现在知道有这回事即可：

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

## 验收

- [ ] 终端能显示 Python 版本
- [ ] 能运行并看到 `Hello, Python!`
- [ ] 知道本仓库路径，能用编辑器打开

## 下一步

进入 [../stage-1-basics/README.md](../stage-1-basics/README.md)，开始语法核心。

完整路线见 [../docs/roadmap.md](../docs/roadmap.md)。
