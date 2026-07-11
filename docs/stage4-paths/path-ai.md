# AI / 机器学习 / LLM 应用：从零路线与资源（已有 Python 基础）

> 目标：理解「数据 → 模型/规则 → 预测/生成」流水线，能跑通经典 ML 小项目或实用 LLM 小工具（二选一深挖亦可）。  
> 本仓库：[stage-4-tracks/ai/](../../stage-4-tracks/ai/)  
> **建议顺序**：规则/经典 ML 直觉 → 再 LLM API；不要零基础直接啃大模型训练源码。

---

## 一、你需要已经会的（检查清单）

- [ ] Python 语法与函数、文件、venv 熟练  
- [ ] 最好有一点 **pandas 读 CSV**（没有就先花 3～5 天补数据路线阶段 1）  
- [ ] 会安装第三方库；会读英文报错关键词  

数学：**线性代数/微积分先懂直觉即可**（向量、拟合、过拟合概念）；不必先刷完高数再开工。

---

## 二、两条分叉（先选主路径）

| 路径 | 适合谁 | 产出 |
|------|--------|------|
| **A. 经典 ML** | 想理解模型、表格预测、打基础 | 分类/回归小项目 + 指标 |
| **B. LLM 应用** | 想快做智能工具、聊天/摘要 | CLI/小服务调 API |
| **A+B** | 时间多 | 先 A 4 周再 B 2～3 周 |

本仓库 starter/demo 是 **规则版流水线**，两条路径都适用作「输入→处理→输出」热身。

---

## 三、学习路线

### 第 0 步：本仓库热身（1 天）

```bash
cd stage-4-tracks/ai/starter
python main.py

cd ../demo
python main.py
```

**想清楚**：规则版与「真模型」差在哪（泛化、数据、评估）。

---

### 路径 A：经典机器学习（约 5～8 周）

#### A1 · 概念与 scikit-learn 第一周

**学什么**

| 主题 | 要点 |
|------|------|
| 问题类型 | 分类 / 回归 / 聚类（先会前两个） |
| 流程 | 拆训练测试集 → 训练 → 预测 → 评估 |
| 指标 | 准确率、混淆矩阵；回归看误差 |
| 过拟合 | 训练集很好、测试集很差 |

**资源**

- scikit-learn 用户指南：https://scikit-learn.org/stable/user_guide.html  
- 官方 examples：https://scikit-learn.org/stable/auto_examples/index.html  

**练什么**

跑通 iris 或 digits 官方示例，改打印内容，理解每一步变量形状。

#### A2 · 课程跟学（约 3～5 周，只跟一门）

| 课程 | 链接 | 说明 |
|------|------|------|
| ML for Beginners（微软） | https://github.com/microsoft/ML-For-Beginners | **首选**，有周次与项目 |
| Google ML Crash Course | https://developers.google.com/machine-learning/crash-course | 概念强 |
| Kaggle Learn Intro to ML | https://www.kaggle.com/learn/intro-to-machine-learning | 短平快 |

**验收**：独立完成「读 CSV → 训练 → 测试集指标 → 简短结论」。

#### A3 · 作品集项目（约 1～2 周）

放 `projects/ai-ml-xxx/`：

1. 明确预测目标  
2. 数据来源与清洗说明  
3. 模型（先 LogisticRegression / RandomForest 即可）  
4. 指标与失败案例分析  
5. README 可复现  

---

### 路径 B：LLM 应用开发（约 3～5 周）

#### B1 · API 最小闭环（1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| 提示词 | 角色、任务、格式、示例 |
| API 调用 | 官方 SDK 或 HTTP；流式可后学 |
| 安全 | Key 在环境变量；不提交 Git |
| 失败 | 超时、限流、内容过滤 |

**资源**

- 各家官方 API 文档（OpenAI 兼容接口常见）  
- [openai/openai-python](https://github.com/openai/openai-python) examples  

**练什么**

CLI：输入文本 → 摘要/翻译/分类（先做一种）。Key 放 `.env`。

#### B2 · 应用模式（1～2 周）

| 模式 | 说明 |
|------|------|
| 聊天循环 | 多轮上下文（注意长度） |
| 工具雏形 | 模型输出 JSON，你的代码执行（慎用） |
| RAG 概念 | 先检索本地文档再回答（向量库可后上） |

**资源**

- 官方 cookbook / examples  
- Hugging Face 课程（有基础后）：https://huggingface.co/learn  

#### B3 · 作品集（1 周）

`projects/ai-llm-xxx/`：一个真正解决你自己问题的小工具 + README + 无密钥泄露。

---

### 路径 C：深度学习（可选，经典 ML 之后）

| 资源 | 说明 |
|------|------|
| AI for Beginners（微软） | https://github.com/microsoft/AI-For-Beginners |
| PyTorch 官方 Tutorials | https://pytorch.org/tutorials/ |
| fastai 课程 | 实践向，英语 |

**不建议**在 Python 基础刚过就上大型训练；先会用再谈训。

---

## 四、资源总表

### 课程与书

| 资源 | 路径 | 链接 |
|------|------|------|
| ML for Beginners | A | https://github.com/microsoft/ML-For-Beginners |
| AI for Beginners | C | https://github.com/microsoft/AI-For-Beginners |
| scikit-learn 文档 | A | https://scikit-learn.org/stable/ |
| Made With ML | A 进阶工程 | https://github.com/GokuMohandas/Made-With-ML |
| 《机器学习实战》等 | A  ent | 按兴趣选一本 |

### GitHub

完整表：[stage4-github-projects.md](../stage4-github-projects.md) 路线 D  

| 用途 | 仓库 |
|------|------|
| 课程 | microsoft/ML-For-Beginners |
| 库 examples | scikit-learn/scikit-learn |
| SDK | openai/openai-python |
| 模型生态 | huggingface/transformers（按文档最小例子） |

### 工具栈建议

```
# 路径 A
scikit-learn
pandas
numpy
matplotlib

# 路径 B
openai 或 兼容 SDK
python-dotenv
requests/httpx

# 共用
pytest（测纯函数与数据处理）
```

---

## 五、能力自评

### 路径 A 初级

- [ ] 会 train/test 拆分与基本分类指标  
- [ ] 能解释过拟合  
- [ ] 有一个可复现的小预测项目  

### 路径 B 初级

- [ ] 会安全调用 LLM API  
- [ ] 会写清晰提示词并约束输出格式  
- [ ] 有一个解决真实小问题的 CLI/工具  

### 可展示

- [ ] README 含：环境、如何运行、示例输入输出、局限说明  

---

## 六、常见坑

1. 跳过数据清洗直接调参  
2. 只追新模型论文，没有可运行作品  
3. API Key 提交到 GitHub  
4. 把规则 demo 说成「训练了大模型」——表达要诚实  
5. 同时开 PyTorch + TF + 三门课 → 只留一条主路径  

---

## 七、和本仓库其他方向的关系

| 需要时 | 去补 |
|--------|------|
| 表格很乱 | [path-data.md](path-data.md) |
| 要把模型包成 API | [path-web.md](path-web.md) |
| 批量跑数据/调接口 | [path-automation.md](path-automation.md) |

下一步：[README.md](README.md) · [../../stage-4-tracks/ai/README.md](../../stage-4-tracks/ai/README.md)
