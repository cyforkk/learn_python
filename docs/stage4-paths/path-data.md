# 数据分析：从零路线与资源（已有 Python 基础）

> 目标：能独立完成「读表 → 清洗 → 统计 → 出图 → 写结论」，并会用 Jupyter 或脚本复现分析。  
> 本仓库：[stage-4-tracks/data/](../../stage-4-tracks/data/)

---

## 一、你需要已经会的（检查清单）

- [ ] 列表/字典/循环/函数熟练  
- [ ] 文件与路径基础  
- [ ] venv / pip  
- [ ] 会查官方文档（比背 API 重要）  

数学：高中统计直觉即可（平均、比例）；不要求先学高数。

---

## 二、学习路线（建议 5～8 周）

### 第 0 步：本仓库热身（1～2 天）

```bash
cd stage-4-tracks/data/starter
pip install -r requirements.txt
python main.py

cd ../demo
pip install -r requirements.txt
python main.py
```

**验收**：理解 DataFrame、分组 `groupby`、导出 CSV。

---

### 阶段 1：NumPy 直觉 + Pandas 读写（约 1～2 周）

**学什么**

| 主题 | 要点 |
|------|------|
| NumPy | 数组、向量化运算（够用即可，别深挖底层） |
| 读数据 | `read_csv` / `read_excel`、编码、缺失值预览 |
| 选择 | `loc` / `iloc`、条件筛选、增删列 |
| 清洗 | `dropna`、`fillna`、类型转换、去重 |
| 汇总 | `describe`、`groupby` + `agg`、`value_counts` |

**练什么**

1. 对本仓库 `sample.csv` / `sales.csv` 做 5 个统计问题并打印答案  
2. 换一份 Kaggle 小 CSV，重复清洗 + 分组  

**验收**：能口述「脏数据常见问题」及对应处理函数。

---

### 阶段 2：可视化（约 1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| matplotlib | 折线、柱状、散点、标题/图例/保存 png |
| seaborn（可选） | 更省事的统计图 |
| 原则 | 一图一结论；别堆 20 张无意义图 |

**练什么**

1. 对销售/城市数据出 2～3 张图  
2. 每张图写一句话结论（Markdown 报告）  

**验收**：报告里图文对应，他人不看代码也能懂结论。

---

### 阶段 3：分析流程与 Jupyter（约 1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| 分析流程 | 问题 → 数据 → 清洗 → 探索 → 结论 → 局限 |
| Jupyter | 单元格运行、导出；或继续用 `.py` 脚本（二选一熟练） |
| 可复现 | 固定随机种子、记录数据版本、requirements |

**练什么**

完整小报告一份（`projects/data-report/`）：

1. 研究问题（1～2 句）  
2. 数据来源  
3. 清洗步骤  
4. 关键统计 + 图  
5. 结论与不足  

---

### 阶段 4：进阶选修（按需 1～2 周）

| 方向 | 内容 | 何时学 |
|------|------|--------|
| 时间序列 | 日期解析、重采样 | 有日期字段需求时 |
| 合并表 | `merge` / `concat` | 多表分析时 |
| Streamlit | 把分析做成小网页 | 想演示给别人点时 |
| SQL | 基础 SELECT/GROUP BY | 数据在数据库里时 |
| 机器学习入门 | 见 AI 路线 | 要做预测时再跨过去 |

---

## 三、资源清单

### 官方与书籍

| 资源 | 说明 | 链接 |
|------|------|------|
| pandas 用户指南 | 第一手权威 | https://pandas.pydata.org/docs/user_guide/ |
| pandas 10 minutes | 快速过一遍 API | https://pandas.pydata.org/docs/user_guide/10min.html |
| NumPy 快速入门 | 数组基础 | https://numpy.org/doc/stable/user/quickstart.html |
| 《利用 Python 进行数据分析》 | 系统书 | 实体/电子书 |
| Python Data Science Handbook | 免费 notebook 风格 | https://jakevdp.github.io/PythonDataScienceHandbook/ |

### 课程（只跟一门主课）

| 资源 | 链接 | 说明 |
|------|------|------|
| Data Science for Beginners（微软） | https://github.com/microsoft/Data-Science-For-Beginners | 路径清晰，适合有 Python 基础 |
| Kaggle Learn - Pandas | https://www.kaggle.com/learn/pandas | 短课+练习 |
| freeCodeCamp 数据分析向 | YouTube 搜索 | 视频党选一门跟完 |

### GitHub / 数据源

详见 [stage4-github-projects.md](../stage4-github-projects.md) 路线 B  

| 类型 | 推荐 |
|------|------|
| 读 | jakevdp/PythonDataScienceHandbook、microsoft/Data-Science-For-Beginners |
| 画图 | mwaskom/seaborn examples |
| 数据 | Kaggle Datasets、政府开放数据、本仓库 CSV |

### 工具栈建议

```
pandas
numpy
matplotlib
seaborn          # 可选
jupyter          # 可选
openpyxl         # 读写 Excel 时
pytest           # 测清洗函数时
```

---

## 四、能力自评

### 初级

- [ ] 独立完成 CSV 清洗 + groupby 统计  
- [ ] 会画并保存 2 种图  
- [ ] 会写简短分析结论  

### 中级

- [ ] 多表 merge、时间字段处理  
- [ ] 分析过程可复现（依赖+说明）  
- [ ] 能向非技术同事讲清结论  

### 可展示

- [ ] `projects/` 下有带图与 README 的分析报告或小工具  

---

## 五、常见坑

1. 一上来就学深度学习 → 先把表洗干净  
2. 只看视频不动手 → 每节至少改一个单元格  
3. 图很多结论为零 → 强制「一图一句话」  
4. 编码混乱 → 读写统一 UTF-8  

下一步：[README.md](README.md) · [../../stage-4-tracks/data/README.md](../../stage-4-tracks/data/README.md)
