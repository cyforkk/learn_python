# Web 后端：从零路线与资源（已有 Python 基础）

> 目标：能独立实现可运行的 JSON API（路由、状态码、校验、持久化入门），并会本地调试与简单测试。  
> 本仓库：[stage-4-tracks/web/](../../stage-4-tracks/web/)  
> **框架建议**：入门用 **Flask** 或 **FastAPI** 二选一（推荐 API 向优先 FastAPI）。

---

## 一、你需要已经会的（检查清单）

- [ ] 函数、模块拆分、字典/JSON  
- [ ] venv / pip / requirements  
- [ ] HTTP 名词不陌生更好：URL、GET/POST（不会可边学边补）  
- [ ] 会读报错；会用编辑器调试  

---

## 二、先补的 Web 概念（2～3 天，不必很深）

| 概念 | 你要能回答 |
|------|------------|
| 客户端 / 服务端 | 浏览器或前端请求，后端返回数据 |
| 请求方法 | GET 读、POST 建、PUT/PATCH 改、DELETE 删 |
| 状态码 | 200 成功、201 创建、400 参数错、404 没有、500 服务器错 |
| JSON API | 请求/响应体多为 JSON |
| 路由 | URL 路径对应处理函数 |

**小实验**：跑本仓库 web starter/demo，用浏览器或 `curl`/httpie 看 JSON。

---

## 三、学习路线（建议 5～8 周）

### 第 0 步：本仓库热身（1～2 天）

```bash
cd stage-4-tracks/web/starter
pip install -r requirements.txt
python main.py

cd ../demo
pip install -r requirements.txt
python main.py
```

**验收**：说清 `/health`、`/echo`、demo 里 POST/GET 待办的含义。

---

### 阶段 1：框架官方 Tutorial（约 1.5～2 周）——只跟一门

#### 选项 A：FastAPI（推荐做 API）

**学什么**（按官方教程顺序）

1. 第一个路径操作  
2. 路径参数 / 查询参数  
3. 请求体与 Pydantic 模型  
4. 响应模型与状态码  
5. 自动文档 `/docs`  

**资源**：https://fastapi.tiangolo.com/zh/tutorial/

#### 选项 B：Flask

**学什么**

1. 最小应用与路由  
2. `jsonify`、request 取 JSON  
3. 蓝图（Blueprint）入门（可稍后）  
4. 官方 Tutorial  

**资源**：https://flask.palletsprojects.com/

**验收**：不看教程能默写「健康检查 + 回显 name」两个接口。

---

### 阶段 2：CRUD 与内存/文件持久化（约 1～2 周）

**学什么**

| 主题 | 要点 |
|------|------|
| REST 风格 | 资源用名词；用方法区分动作 |
| 校验 | 空字段、类型错误返回 400 |
| 持久化 v1 | JSON 文件（先会） |
| 持久化 v2 | SQLite + 基础 SQL（下一阶段） |
| 测试 | Flask test_client / FastAPI TestClient |

**练什么**

1. 待办 API：增、删、改、查（在 demo 上扩展）  
2. 至少 3 个自动化测试  
3. README：如何启动、如何用 `/docs` 或示例请求  

**验收**：重启进程后数据仍在（若做了文件/DB 持久化）。

---

### 阶段 3：数据库与结构（约 1～2 周）

**学什么**

| 主题 | 要点 |
|------|------|
| SQL 基础 | CREATE/SELECT/INSERT/UPDATE/DELETE |
| SQLite | 文件型数据库，适合本地作品 |
| ORM 入门 | SQLAlchemy 或框架自带（先会一种） |
| 项目结构 | `routers/`、`models/`、`schemas/` 分离（FastAPI 常见） |

**练什么**

记账 / 博客文章 API（二选一），表结构清晰。

**验收**：能画出「表字段」与「接口列表」两张小表。

---

### 阶段 4：进阶选修（按需）

| 主题 | 说明 |
|------|------|
| 认证 | API Key / JWT 入门（别一上来上 OAuth 全家桶） |
| 跨域 CORS | 给前端联调时再开 |
| Docker 部署 | 作品可展示时再学 |
| 全栈模板 | [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) 只看目录 |

---

## 四、资源清单

### 官方（第一优先）

| 资源 | 链接 |
|------|------|
| FastAPI 中文文档 | https://fastapi.tiangolo.com/zh/ |
| Flask 文档 | https://flask.palletsprojects.com/ |
| MDN HTTP 概述 | https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Overview |
| SQLite 文档 | https://www.sqlite.org/docs.html |

### 教程 / 书（选一）

| 资源 | 说明 |
|------|------|
| FastAPI 官方 Tutorial | 最好的入门路径 |
| Flask Mega-Tutorial | 经典长文，偏 Web 应用 |
| TestDriven.io / Real Python FastAPI 文 | 英文质量高，按需搜 |

### GitHub

完整表：[stage4-github-projects.md](../stage4-github-projects.md) 路线 C  

| 用途 | 仓库 |
|------|------|
| 框架 | tiangolo/fastapi、pallets/flask |
| 结构 | fastapi/full-stack-fastapi-template |
| HTTP 靶场 | postmanlabs/httpbin |

### 工具栈建议

```
# 二选一主栈
fastapi + uvicorn
# 或
flask

httpx 或 requests   # 测接口、调别人
pytest
sqlite3（标准库）或 SQLAlchemy
python-dotenv
```

---

## 五、能力自评

### 初级

- [ ] 能写带 JSON 的 GET/POST API  
- [ ] 会返回合适状态码  
- [ ] 会本地启动并看文档页或 test_client  

### 中级

- [ ] 完整 CRUD + 持久化  
- [ ] 有基础自动化测试  
- [ ] 模块拆分清楚  

### 可展示

- [ ] `projects/web-xxx` 他人按 README 能跑通并调通主要接口  

---

## 六、常见坑

1. 同时学 Django + Flask + FastAPI → **只选一个**  
2. 先上微服务/K8s → 先把单机 API 做稳  
3. 不写校验 → 前端乱传直接 500  
4. 密钥写进代码 → 用环境变量  

下一步：[README.md](README.md) · [../../stage-4-tracks/web/README.md](../../stage-4-tracks/web/README.md)
