# 方向：AI / LLM 应用

> **从零路线与资源（已有 Python 基础）** → [docs/stage4-paths/path-ai.md](../../docs/stage4-paths/path-ai.md)

## 建议顺序

1. 先会 Python 与基础数据处理  
2. 再调 LLM API 做小工具（聊天、摘要、分类）  
3. 经典机器学习（`scikit-learn`）按兴趣补充  
4. 深度学习框架（PyTorch 等）放到更后面  

## 入门资源

- 各家 LLM 官方 API 文档  
- scikit-learn 教程：https://scikit-learn.org/stable/user_guide.html  

## 先跑 starter → 再跑 demo

- [starter/](starter/)：关键词助手  
- [demo/](demo/)：情感倾向统计流水线  

## GitHub：读码与练手

完整表见 → **[docs/stage4-github-projects.md](../../docs/stage4-github-projects.md)**（路线 D）

| 类型 | 仓库 | 你怎么做 |
|------|------|----------|
| 课程 | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 按课完成经典 ML 入门（优先于直接啃大库源码） |
| 课程 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 神经网络与现代 AI 路径 |
| examples | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 只跑 `examples/`，换成自己的小 CSV |
| SDK | [openai/openai-python](https://github.com/openai/openai-python) | 看 examples；Key 放 `.env` |
| 进阶 | [huggingface/transformers](https://github.com/huggingface/transformers) | 按文档跑最小 pipeline，勿一次读完仓库 |
| 流水线 | [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | 了解训练到部署的目录思路 |

## 最小 demo 选题

1. 命令行「文本摘要 / 翻译」小工具（需自备 API Key，勿提交密钥）  
2. 用 scikit-learn 跑一个官方入门分类示例并改数据路径  

代码建议路径：`projects/ai-demo/`  
**切记**：`.env` 已在仓库 `.gitignore` 中，不要把 Key 写进代码提交。
