# 阶段 4 · 方向分支

**原则：先选 1 条主线**，`starter` → `demo` → **GitHub 读码/练手** → 再做 stage-5 项目。

## 方向一览

| 方向 | 说明 | starter | 中型 demo |
|------|------|---------|-----------|
| 自动化 | [automation/](automation/README.md) | [starter/](automation/starter/) | [demo/](automation/demo/) |
| 数据 | [data/](data/README.md) | [starter/](data/starter/) | [demo/](data/demo/) |
| Web | [web/](web/README.md) | [starter/](web/starter/) | [demo/](web/demo/) |
| AI | [ai/](ai/README.md) | [starter/](ai/starter/) | [demo/](ai/demo/) |

每个目录：

```bash
pip install -r requirements.txt   # 若有
python main.py
```

## GitHub 练手与读码（重点）

各方向精选仓库、读什么、练什么，见统一文档：

→ **[docs/stage4-github-projects.md](../docs/stage4-github-projects.md)**

简表：

| 方向 | 优先读 | 优先练 |
|------|--------|--------|
| 自动化 | [asweigart/automate-the-boring-stuff](https://github.com/asweigart/automate-the-boring-stuff) | [public-apis](https://github.com/public-apis/public-apis) 选题写脚本 |
| 数据 | [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | Kaggle CSV + 本仓库 data/demo |
| Web | [tiangolo/fastapi](https://github.com/tiangolo/fastapi) 官方 Tutorial | 扩展本仓库 web/demo CRUD |
| AI | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | scikit-learn examples 换自己的数据 |

## 建议

1. 阶段 1～3 扎实后再开方向  
2. 本仓库 starter/demo 跑通后，再 clone **一个** GitHub 项目深挖  
3. 扩展代码放 `projects/方向名-xxx/`，不要把 API Key 推进仓库  

资源总表：[docs/roadmap.md](../docs/roadmap.md)  
地图：[docs/learning-map.md](../docs/learning-map.md)

## 下一步

[stage-5-projects](../stage-5-projects/README.md)
