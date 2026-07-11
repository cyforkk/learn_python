# 参考：venv 实践说明

常见问题：

1. **PowerShell 禁止脚本运行**  
   可临时：`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`  
   或使用 `cmd` 激活：`.venv\Scripts\activate.bat`

2. **python 不是 3.x**  
   Windows 尝试 `py -3.12 -m venv .venv`

3. **装包装到系统环境**  
   确认提示符有 `(.venv)` 再 `pip install`

4. **不要提交 `.venv`**  
   体积大且与机器相关；只提交 `requirements.txt`
