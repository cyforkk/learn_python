# 项目规格 03：公开 API 查询 CLI

## 功能需求

1. 使用 `requests` 调用一个**无需密钥**或你自备密钥的公开 API  
   示例（可换）：`https://httpbin.org/get`、开放天气/汇率等（以对方条款为准）  
2. 命令行传入参数（城市名、关键词等）  
3. 将关键字段美化打印；可选保存为 JSON  

## 工程要求

- `requirements.txt` 包含 `requests`  
- 网络失败、超时、非 200 状态码要处理  
- **禁止**把 API Key 写进代码；用环境变量或 `.env`（勿提交）

## 验收

- [ ] `python main.py ...` 有清晰帮助或参数说明  
- [ ] 断网或错误 URL 时有友好报错  

代码目录建议：`projects/api-cli/`
