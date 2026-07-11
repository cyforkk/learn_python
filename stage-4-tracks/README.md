# 阶段 4 · 方向分支

**前提**：已有 Python 基础（约等于本仓库 stage-1～3）。  
**原则**：一次只选 **1 条主线**。  
**顺序**：**先读方向路线文章** `path-*.md` → 再跑 `starter`/`demo` → 再 GitHub 读码/练手 → 再 stage-5 项目。  
不要一上来只跑 starter 却不读路线说明。

## 从零路线与资源（主文档）

→ **[docs/stage4-paths/README.md](../docs/stage4-paths/README.md)**

| 方向 | 学习路线与资源 | 本仓库代码 |
|------|----------------|------------|
| 自动化 / 脚本 | [path-automation.md](../docs/stage4-paths/path-automation.md) | [automation/](automation/) |
| 数据分析 | [path-data.md](../docs/stage4-paths/path-data.md) | [data/](data/) |
| Web 后端 | [path-web.md](../docs/stage4-paths/path-web.md) | [web/](web/) |
| AI / ML / LLM | [path-ai.md](../docs/stage4-paths/path-ai.md) | [ai/](ai/) |

每个方向文档包含：前置检查、分周路线、资源表、能力自评、常见坑。

## 代码入口

| 方向 | starter | 中型 demo | 方向说明 |
|------|---------|-----------|----------|
| 自动化 | [starter/](automation/starter/) | [demo/](automation/demo/) | [README](automation/README.md) |
| 数据 | [starter/](data/starter/) | [demo/](data/demo/) | [README](data/README.md) |
| Web | [starter/](web/starter/) | [demo/](web/demo/) | [README](web/README.md) |
| AI | [starter/](ai/starter/) | [demo/](ai/demo/) | [README](ai/README.md) |

```bash
pip install -r requirements.txt   # 若有
python main.py
```

## GitHub 练手与读码

→ **[docs/stage4-github-projects.md](../docs/stage4-github-projects.md)**

| 方向 | 优先读 | 优先练 |
|------|--------|--------|
| 自动化 | automate-the-boring-stuff、requests | public-apis 选题写脚本 |
| 数据 | Data-Science-For-Beginners、Handbook | Kaggle CSV + 本仓库 demo |
| Web | FastAPI / Flask 官方 Tutorial | 扩展 web/demo CRUD |
| AI | ML-For-Beginners | scikit-learn examples |

## 建议

1. 阶段 1～3 未扎实不要同时开四条线  
2. 路线文档跟完「初级自评」再冲作品集项目  
3. 代码放 `projects/方向名-xxx/`，API Key 勿提交  

总路线：[docs/roadmap.md](../docs/roadmap.md) · 地图：[docs/learning-map.md](../docs/learning-map.md)

## 下一步

[stage-5-projects](../stage-5-projects/README.md)
