# 学习仓库搭建工作流（沉淀）

> 本文记录：`learn_python` 从「一堆 md」变成「可自学仓库」的**可复用工作流**。  
> 以后搭同类仓库（别的语言/技术）可直接照此骨架改，不必重新踩坑。

---

## 1. 目标定义（先拍板再动手）

| 问题 | 本仓库的答案 |
|------|----------------|
| 给谁用？ | 已有 Python 环境、要系统练的人（环境非主线） |
| 学什么？ | 语法 → 标准库 → 工程习惯 → 方向 → 项目 |
| 怎么学？ | **先读笔记 → 再做空白作业 → 再对答案 → 再项目** |
| 仓库形态？ | 自学跟练型：notes + exercises 骨架 + solutions + 路线文档 |

**硬约束（后期别轻易推翻）：**

1. 默认读者**已装好语言运行时**  
2. **不是每篇笔记都有题**  
3. **exercises 里禁止放完整答案**  
4. **笔记练习区禁止贴答案代码**  
5. 答案只在 `solutions/`，可选自检只在 `checks/`  

---

## 2. 推荐阶段划分（骨架）

```
stage-0   可选附录（环境）——默认可跳过
stage-1   语言核心（语法）
stage-2   标准库 / 常用能力
stage-3   工程习惯（venv、调试、测试、Git）
stage-4   方向分支（路线 + starter/demo + 外部资源）
stage-5   综合项目规格 + projects/ 实现区
```

每个 `stage-N`（有练习时）目录约定：

```
stage-N-xxx/
  README.md          # 本阶段：先学后练、过关标准
  notes/             # 讲解文章（可有教学示例）
  exercises/         # 仅题目骨架 + TODO
    checks/          # 可选自检（不是作业）
  solutions/         # 参考答案（最简实现）
```

辅助目录：

```
docs/                # 总路线、地图、原则、工作流
notes/               # 学习者个人日记
bugs/                # 踩坑记录
projects/            # 综合项目代码
scripts/             # 维护脚本（check_all、改导航等）
```

---

## 3. 从零搭建：分步工作流

### 步骤 A · 总路线（1 份）

1. 写 `docs/roadmap.md`：阶段图、资源、预期  
2. 写根 `README.md`：怎么学、从哪开始（**从学笔记开始，不要一上来刷题**）  
3. 写 `docs/learning-map.md`：笔记 ↔ 练习对照表（带文章链接）  

**验收：** 新人只看 README + roadmap 知道第一天干什么。

---

### 步骤 B · 笔记（按阶段批量）

1. 一主题一篇 md，放进对应 `stage-*/notes/`  
2. 正文可写教学示例，但**不要写「与作业完全相同」的全文答案**  
3. 文末统一 **「本课衔接」**（见第 4 节）  

**验收：** 每篇能说清：上一篇是谁、下一篇是谁、本篇有没有过关题。

---

### 步骤 C · 练习原则（先定规则再写题）

写 `docs/exercise-policy.md`，固定标签：

| 标签 | 含义 |
|------|------|
| **过关** | 阶段最少完成集（技能覆盖表） |
| **加练** | 可选多练；**往往不难**，只是重复/换场景/多花时间 |
| **建议** | 低成本动手（跟命令、写日记） |
| **无** | 本篇不布置仓库题 |

**过关题设计原则：**

- 一篇过关题 ≈ 一个主技能  
- 实现必须能做成「最短脚本」  
- 过关线要短（阶段 1 建议 3～4 题，阶段 2 建议 3 题）  

**验收：** 任意「无」的笔记都不会误挂难题；任意「过关」题都有清晰技能名。

---

### 步骤 D · 写作业骨架（exercises）

每个作业文件**只允许**：

```text
# 练习：标题
# 先读笔记：xxx
# 运行：python 本文件.py
#
# 题目：
# 1. …
# 2. …
#
# TODO: 在这里写你的代码
```

**禁止：** 完整实现、`assert`、`_selfcheck`、复杂类型注解、pytest 混在作业里。

**验收：** 打开 exercises 文件，看不到「做完的样子」。

---

### 步骤 E · 写参考答案（solutions）

1. 与作业**同技能、同难度**  
2. **最简实现**（和教学水平一致，不要突然工程化）  
3. 文件名与 exercises 对应  

**验收：** 对照时能看懂；复制也能跑，但学员应先自己写。

---

### 步骤 F · 笔记文末挂题（只挂题目）

有过关/加练的笔记，文末固定：

```markdown
## 本课衔接
| 上一篇 | … |
| 下一篇 | … |
| 本篇练习 | 过关 / 加练 / 无 |

### 过关 · 题名
**题目：**
1. …
2. …
- 作业（空白）：[exercises/xxx.py](...)
- 答案（做完再看）：[solutions/xxx.py](...)
```

无独立练习的笔记：

```markdown
## 本课衔接
| 本篇练习 | 无独立新作业 |
**和前后的关系：** 回看 ex0x，思考……（具体问题）
```

**禁止：** 只丢 `exercises/README.md` 当衔接；禁止在笔记里贴答案全文。

---

### 步骤 G · 方向阶段（stage-4）

1. 每个方向：`README` + `starter/`（能跑）+ 可选 `demo/`  
2. `docs/stage4-paths/path-xxx.md`：有语言基础后的从零路线与资源  
3. `docs/stage4-github-projects.md`：读码/练手 GitHub 清单  
4. 顺序：**路线文章 → starter/demo → 外部资源 → 自己的 projects/**  

---

### 步骤 H · 综合项目（stage-5 + projects）

1. `exercises/project_spec_*.md`：只写规格  
2. `projects/项目名/`：可运行实现 + README  
3. 笔记可讲思想，**规格与实现分离**  

---

### 步骤 I · 工程与发布

1. `.gitignore`：venv、缓存、本地数据、密钥  
2. `LICENSE` / `CONTRIBUTING`（若开源）  
3. `scripts/check_all.py`：检查 **solutions** 与语法，**不要求** 空 exercises 能跑业务  
4. GitHub：`gh repo create` + `git push`  
5. CI：可选，对 solutions / pytest 做冒烟  

---

## 4. 「本课衔接」模板（复制即用）

### 4.1 有过关题

```markdown
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [xxx.md](xxx.md) |
| **下一篇** | [yyy.md](yyy.md) |
| **本篇练习** | **过关 1 题** |

### 过关 · 题目标题

**题目：**

1. …
2. …

- 作业（空白）：[exercises/ex0x_….py](../exercises/ex0x_….py)
- 答案（做完再看）：[solutions/ex0x_….py](../solutions/ex0x_….py)
```

### 4.2 无独立练习

```markdown
---

## 本课衔接

| | |
|--|--|
| **上一篇** | [函数.md](函数.md)（应已做过 ex05） |
| **下一篇** | 阶段结束 → [下一 stage README](…) |
| **本篇练习** | **无独立新作业** |

**和前后的关系：**

1. 打开你写的 [ex05 作业](../exercises/…)  
2. 思考：……（本篇概念如何套到已做题上）  
```

---

## 5. 过关题设计检查清单

写下一道「过关」前打勾：

- [ ] 对应**一个**刚学完的主技能  
- [ ] 不依赖后面章节  
- [ ] 可用最短脚本实现（预计新手 20～40 分钟）  
- [ ] exercises 只有题目，无答案  
- [ ] solutions 最简且能跑  
- [ ] 笔记文末只有题目 + 双链接  
- [ ] 已更新 learning-map / progress 的过关列表  

---

## 6. 迭代中沉淀的避坑（本仓库踩过）

| 坑 | 表现 | 改法 |
|----|------|------|
| 环境当主线 | 读者已有 Python 仍被 stage-0 挡住 | 环境降级为可选附录 |
| 上来就刷题 | README 直接 `--check` | 入口改为「先读 notes」 |
| 篇篇挂题 | 基本类型挂字典大题 | 练习原则 + 无/过关/加练 |
| 作业=答案 | exercises 里写满实现 | 骨架 TODO + solutions |
| 笔记贴答案 | 「与仓库题一致」整段代码 | 只挂题目与链接 |
| 选做=更难 | 读者误解 | 改名「加练」，注明难度相近 |
| 衔接割裂 | 作用域链到练习总表 | 本课衔接：上/下篇 + 回看 ex0x |
| 测试吓人 | assert/pytest 混作业 | checks/ 与 test_ 文件单独说明 |
| 答案过工程 | 类型注解、max(key=)、多文件过度拆 | solutions 与 exercises 同级简单 |

---

## 7. 维护节奏（仓库活着之后）

| 频率 | 做什么 |
|------|--------|
| 加一篇笔记 | 写正文 → 写本课衔接 → 更新 learning-map |
| 加一道过关题 | 按第 5 节检查清单 → 更新 progress |
| 改难度政策 | 先改 exercise-policy，再批量改导航 |
| 发版/推送 | `check_all` 过 solutions → commit → push |

可用脚本（本仓库）：

- `scripts/check_all.py`：冒烟 solutions  
- `scripts/rewrite_note_footers.py`：批量本课衔接（改后需人工审）  
- `scripts/rename_exercise_labels.py`：标签重命名历史参考  

---

## 8. 最小可运行「新仓库」清单

从零复制时，至少有这些再宣布「能学了」：

- [ ] README（先学后练）  
- [ ] docs/roadmap.md  
- [ ] docs/learning-map.md  
- [ ] docs/exercise-policy.md  
- [ ] docs/repo-build-workflow.md（本文）  
- [ ] 至少一个 stage 的 notes + 2～4 道过关骨架 + solutions  
- [ ] progress.md  
- [ ] .gitignore  
- [ ] （可选）GitHub remote  

---

## 9. 本仓库关键入口索引

| 文档 | 路径 |
|------|------|
| 总入口 | [../README.md](../README.md) |
| 总路线 | [roadmap.md](roadmap.md) |
| 学习地图 | [learning-map.md](learning-map.md) |
| 练习原则 | [exercise-policy.md](exercise-policy.md) |
| 方向路线 | [stage4-paths/README.md](stage4-paths/README.md) |
| GitHub 清单 | [stage4-github-projects.md](stage4-github-projects.md) |
| 进度 | [../progress.md](../progress.md) |

---

## 10. 一句话工作流

```
定目标与硬约束
  → 搭 stage 骨架
  → 写路线与地图
  → 定练习原则（过关/加练/无）
  → 写笔记 + 本课衔接
  → 写空白 exercises + 最简 solutions
  → 方向与项目
  → check + GitHub
  → 按避坑表迭代
```

**记住：** 学习仓库的产品是「可跟的路径」，不是「代码越多越好」。  
路径清晰、作业空白、答案分离、衔接不断裂——四件事做到，仓库就立得住。
