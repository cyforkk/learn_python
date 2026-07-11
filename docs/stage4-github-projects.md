# 阶段 4：GitHub 练手与读码清单

> 配合本仓库 [stage-4-tracks](../stage-4-tracks/README.md) 使用：先跑通本仓库 `starter/` → `demo/`，再来读开源、做小改。  
> 仓库星数与结构会变，以各项目 **README / 官方文档** 为准；下列侧重 **适合初中级读码与练手**，不是「只追 star」。

---

## 怎么用这些 GitHub 项目

### 推荐节奏

```
1. 本仓库 stage-4 对应方向 starter + demo 跑通
2. 选 1 个「读码」仓库：只读 README + 一个最小示例目录
3. 选 1 个「练手」仓库或课题：clone 后改一处、能跑、写进自己的 projects/
4. 用 Git 提交：说明改了什么（中文 commit 亦可）
```

### 读码时看什么

| 关注点 | 问题 |
|--------|------|
| 入口 | 从哪个文件启动？`main` / `__main__` / CLI？ |
| 依赖 | `requirements.txt` / `pyproject.toml` 里有哪些库？ |
| 目录 | 业务代码、测试、文档怎么分？ |
| 错误处理 | 网络失败、参数错误怎么提示？ |
| 风格 | 命名、类型注解、函数是否够短？ |

### 练手任务模板（可复制）

1. Fork 或 clone 到本地（大项目不必 fork 全量，可只抄思路自建小仓库）  
2. 建 venv，按 README 安装依赖  
3. 跑通官方「最小例子」  
4. **只改一处**：多一个参数 / 多写一个输出字段 / 换数据源  
5. 在 `learn_python/projects/方向-xxx/` 写自己的笔记：学到了什么  

### 注意

- 遵守各仓库 **License** 与 **贡献指南**；商用/爬虫注意法律与网站条款  
- 大仓库（pandas、pytorch 等）**不要从头读源码**，只读 `docs/`、`examples/`、官方教程链接  
- API Key 放 `.env`，**不要**提交到 GitHub  

---

## 路线 A：自动化 / 脚本

**本仓库入口**：[automation/](../stage-4-tracks/automation/README.md) · [starter](../stage-4-tracks/automation/starter/) · [demo](../stage-4-tracks/automation/demo/)

### 建议读码（看别人怎么组织脚本）

| 仓库 | 链接 | 适合看什么 | 难度 |
|------|------|------------|------|
| Automate the Boring Stuff（书配套代码） | https://github.com/asweigart/automate-the-boring-stuff | 文件、Excel、邮件、剪贴板等脚本写法 | ⭐ |
| requests | https://github.com/psf/requests | `README`、文档示例；HTTP 客户端习惯 | ⭐ |
| httpx | https://github.com/encode/httpx | 现代 HTTP 客户端 API 设计 | ⭐⭐ |
| schedule | https://github.com/dbader/schedule | 定时任务几行怎么写 | ⭐ |
| yt-dlp | https://github.com/yt-dlp/yt-dlp | 大型 CLI 项目结构（只看目录与入口，不求全懂） | ⭐⭐⭐ |

### 建议练手（想法源 + 小改）

| 资源 | 链接 | 练手建议 | 难度 |
|------|------|----------|------|
| public-apis | https://github.com/public-apis/public-apis | 选 1 个免 Key API，写「查询 + 存 JSON」脚本（可基于本仓库 automation demo 扩展） | ⭐⭐ |
| TheAlgorithms/Python | https://github.com/TheAlgorithms/Python | 挑 1 个简单算法文件，读懂后默写；或修文档/补测试（入门贡献） | ⭐⭐ |
| python-telegram-bot | https://github.com/python-telegram-bot/python-telegram-bot | 跟官方 examples 做 echo bot（需 Bot Token，勿提交） | ⭐⭐⭐ |
| Beautiful Soup 文档示例 | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | 配合合规公开页做解析小练习 | ⭐⭐ |

### 练手课题（可放 `projects/automation-*`）

1. 定时备份某个文件夹到带日期的 zip  
2. 调用公开 API，结果写入 CSV/Excel  
3. 批量压缩图片或重命名（先 dry-run）  

---

## 路线 B：数据分析

**本仓库入口**：[data/](../stage-4-tracks/data/README.md) · [starter](../stage-4-tracks/data/starter/) · [demo](../stage-4-tracks/data/demo/)

### 建议读码 / 跟做

| 仓库 | 链接 | 适合看什么 | 难度 |
|------|------|------------|------|
| Python Data Science Handbook（笔记代码） | https://github.com/jakevdp/PythonDataScienceHandbook | Notebook：NumPy / Pandas / 可视化 | ⭐⭐ |
| Data Science for Beginners（微软） | https://github.com/microsoft/Data-Science-For-Beginners | 课程式项目，步骤清晰 | ⭐ |
| pandas 用户指南（文档，非硬啃源码） | https://pandas.pydata.org/docs/user_guide/ | 官方「正确用法」优先于读 C 扩展 | ⭐⭐ |
| seaborn | https://github.com/mwaskom/seaborn | `examples` / 文档画图套路 | ⭐⭐ |
| streamlit-example / 官方 gallery 思路 | https://github.com/streamlit/streamlit | 把分析做成简单 Web 报表 | ⭐⭐ |
| data-science-ipython-notebooks | https://github.com/donnemartin/data-science-ipython-notebooks | 大量 notebook 案例，按主题挑一篇复现 | ⭐⭐ |

### 练手数据源

| 资源 | 链接 | 练手建议 |
|------|------|----------|
| Kaggle Datasets | https://www.kaggle.com/datasets | 下 1 个 CSV，清洗 → 分组 → 2 张图 → 写 5 行结论 |
| 本仓库 sample | [data/starter/sample.csv](../stage-4-tracks/data/starter/sample.csv)、[demo/sales.csv](../stage-4-tracks/data/demo/sales.csv) | 先在本仓库改字段再换真数据 |

### 练手课题（可放 `projects/data-*`）

1. 一份销售/天气 CSV 的完整分析报告（Markdown + 图）  
2. 用 Streamlit 做「上传 CSV → 出统计」小工具  
3. 复现 Handbook 里某一章 notebook，并改用自己的数据  

---

## 路线 C：Web 后端

**本仓库入口**：[web/](../stage-4-tracks/web/README.md) · [starter](../stage-4-tracks/web/starter/) · [demo](../stage-4-tracks/web/demo/)

### 建议读码

| 仓库 | 链接 | 适合看什么 | 难度 |
|------|------|------------|------|
| Flask | https://github.com/pallets/flask | 官方文档 Tutorial；`examples` 目录 | ⭐⭐ |
| FastAPI | https://github.com/tiangolo/fastapi | 官方 Tutorial（文档站）；类型注解 + 自动 OpenAPI | ⭐⭐ |
| full-stack-fastapi-template | https://github.com/fastapi/full-stack-fastapi-template | 真实项目目录（后端/前端/Docker）— 先浏览结构 | ⭐⭐⭐ |
| Flask Mega-Tutorial 相关资料 | 搜索 “Flask Mega-Tutorial” | 经典博客式后端进阶（跟文章比只 clone 更有效） | ⭐⭐ |
| httpbin | https://github.com/postmanlabs/httpbin | 学习 HTTP 时当「靶场」服务看路由设计 | ⭐⭐ |

### 练手 / 模板向

| 仓库 | 链接 | 练手建议 | 难度 |
|------|------|----------|------|
| FastAPI 官方文档示例 | https://fastapi.tiangolo.com/zh/tutorial/ | 独立实现 CRUD 待办 API（对照本仓库 web/demo） | ⭐⭐ |
| flask/examples | https://github.com/pallets/flask/tree/main/examples | 跑通 tutorial 示例后加一个自己的路由 | ⭐⭐ |
| awesome-flask（索引） | https://github.com/mjhea0/awesome-flask | 按需找扩展（登录、迁移），勿一次装全 | ⭐ |

### 练手课题（可放 `projects/web-*`）

1. 待办 REST：增删改查 + JSON 持久化或 SQLite  
2. 为 API 写 3 个 pytest（测状态码与 JSON 字段）  
3. 加一个 `/health` 与统一错误返回格式  

---

## 路线 D：AI / 机器学习 / LLM 应用

**本仓库入口**：[ai/](../stage-4-tracks/ai/README.md) · [starter](../stage-4-tracks/ai/starter/) · [demo](../stage-4-tracks/ai/demo/)

### 建议读码 / 课程仓（优先课程，再库源码）

| 仓库 | 链接 | 适合看什么 | 难度 |
|------|------|------------|------|
| ML for Beginners（微软） | https://github.com/microsoft/ML-For-Beginners | 12 周经典 ML 课程，有测验与项目 | ⭐⭐ |
| AI for Beginners（微软） | https://github.com/microsoft/AI-For-Beginners | 神经网络与现代 AI 入门路径 | ⭐⭐⭐ |
| scikit-learn | https://github.com/scikit-learn/scikit-learn | **只看** `examples/` 与用户指南，不硬啃全部源码 | ⭐⭐ |
| Made With ML | https://github.com/GokuMohandas/Made-With-ML | MLOps 向完整流水线思路 | ⭐⭐⭐ |
| openai-python | https://github.com/openai/openai-python | 官方 SDK 用法与 examples（需 Key） | ⭐⭐ |
| transformers（Hugging Face） | https://github.com/huggingface/transformers | 文档 + notebooks；模型很大，按任务抄最小 pipeline | ⭐⭐⭐ |

### 练手课题（可放 `projects/ai-*`）

1. 用 scikit-learn 跑官方 iris / 文本分类 tutorial，换成自己的小 CSV  
2. 把本仓库 `ai/demo` 的规则情感，改成调用一个公开/自建 API（注意 Key）  
3. 做一个 CLI：输入一段文本 → 摘要或关键词（规则版或 LLM 版二选一）  

### 安全提醒

- 不要把 API Key 写进代码或推到 GitHub  
- 学习用途优先用小模型 / 免费额度 / 本地规则 demo  

---

## 按「一周」怎么排（示例）

| 天 | 自动化示例 | 数据示例 | Web 示例 | AI 示例 |
|----|------------|----------|----------|---------|
| 1–2 | 本仓库 starter+demo | 同左 | 同左 | 同左 |
| 3 | 读 public-apis + 写 API 脚本 | 跟 Data-Science-For-Beginners 一课 | FastAPI 官方 Tutorial 前 3 节 | ML-For-Beginners 第 1 课 |
| 4–5 | 读 automate-the-boring-stuff 一章代码 | Handbook 一章 notebook | 扩展本仓库 web/demo CRUD | scikit-learn 一个 example |
| 6–7 | 自己的 projects/automation-xxx | projects/data-xxx 出报告 | projects/web-xxx + 测试 | projects/ai-xxx CLI |

---

## 与本仓库的对应关系

| 阶段 4 方向 | 本仓库代码 | GitHub 深化文档（本页小节） |
|-------------|------------|------------------------------|
| 自动化 | `stage-4-tracks/automation/` | 上文「路线 A」 |
| 数据 | `stage-4-tracks/data/` | 上文「路线 B」 |
| Web | `stage-4-tracks/web/` | 上文「路线 C」 |
| AI | `stage-4-tracks/ai/` | 上文「路线 D」 |

总路线：[roadmap.md](roadmap.md) · 学习地图：[learning-map.md](learning-map.md)

---

## 维护说明

- 链接失效时以 GitHub 搜索项目全名核对  
- 新增推荐时保持：**有明确读码/练手动作**，避免只堆 star 榜  
