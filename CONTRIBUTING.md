# 贡献指南

感谢对本仓库感兴趣。本仓库以 **中文 Python 速成自学** 为主。

## 如何使用（学习者）

1. 从 [README.md](README.md) 与 [docs/roadmap.md](docs/roadmap.md) 开始  
2. 按 `stage-0` → `stage-5` 学习  
3. 练习优先自己写；卡很久再看 `solutions/`  
4. 进度记在 [progress.md](progress.md)，踩坑记在 `bugs/`

## 如何贡献（改仓库）

1. Fork / 建分支  
2. 保持「笔记可有示例，练习独立可测」的 A1 约定  
3. 新增练习请带 `--check` 或 pytest，并补 `solutions/`  
4. 跑通一键检查：
   ```bash
   pip install -r requirements-dev.txt
   python scripts/check_all.py
   ```
5. 提交说明用完整句子，描述「改了什么、为什么」

## 提交规范建议

- `feat:` 新练习 / 新笔记 / 新项目  
- `fix:` 修错误答案或坏掉的链接  
- `docs:` 仅文档  
- `chore:` 工具与 CI  

## 不要提交

- `.venv/`、API Key、个人 `todos.json`、大体积数据  
- 未脱敏的真实路径隐私  

## 行为约定

- 尊重新手问题  
- 示例代码以清晰为主，不过度炫技  
