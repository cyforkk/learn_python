# 方向：Web 后端

> **从零路线与资源（已有 Python 基础）** → [docs/stage4-paths/path-web.md](../../docs/stage4-paths/path-web.md)

## 常见技能

- FastAPI 或 Flask  
- JSON API、状态码、请求方法  
- SQLite + 基础 SQL（再学 ORM）

## 入门资源

- FastAPI 官方：https://fastapi.tiangolo.com/zh/  
- Flask 教程：https://flask.palletsprojects.com/

## 先跑 starter → 再跑 demo

- [starter/](starter/)  
- [demo/](demo/)：内存待办 GET/POST  

## GitHub：读码与练手

完整表见 → **[docs/stage4-github-projects.md](../../docs/stage4-github-projects.md)**（路线 C）

| 类型 | 仓库 | 你怎么做 |
|------|------|----------|
| 官方教程 | [tiangolo/fastapi](https://github.com/tiangolo/fastapi) + [中文 Tutorial](https://fastapi.tiangolo.com/zh/tutorial/) | 跟完路径操作与响应模型，对照本仓库 demo |
| 读码 | [pallets/flask](https://github.com/pallets/flask) | 跑 examples / 官方 Tutorial，加一个自己的路由 |
| 看结构 | [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | 浏览真实 monorepo 目录（不必一次部署成功） |
| HTTP 靶场 | [postmanlabs/httpbin](https://github.com/postmanlabs/httpbin) | 理解状态码、方法、JSON 响应 |

## 最小 demo 选题

1. 待办事项 REST API（增删改查）  
2. 返回 JSON 的简易「健康检查 + 回显」服务  

代码建议路径：`projects/web-demo/`
