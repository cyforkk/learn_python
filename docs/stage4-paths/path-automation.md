# 自动化 / 脚本：从零路线与资源（已有 Python 基础）

> 目标：能独立写「可重复运行」的脚本——读文件、调 API、批处理、简单定时，并会处理错误与日志。  
> 本仓库：[stage-4-tracks/automation/](../../stage-4-tracks/automation/)

---

## 一、你需要已经会的（检查清单）

- [ ] 函数、字典/列表、文件读写、`pathlib`、异常  
- [ ] `venv` + `pip install` + `requirements.txt`  
- [ ] 会读 Traceback；会用 `encoding="utf-8"`  
- [ ] 基础 Git：`add` / `commit`  

若有缺口，先回 stage-1～3。

---

## 二、学习路线（建议 4～6 周，每天 1～2 小时）

### 第 0 步：本仓库热身（1～2 天）

```bash
cd stage-4-tracks/automation/starter
pip install -r requirements.txt
python main.py

cd ../demo
pip install -r requirements.txt
python main.py
```

**验收**：理解 `requests.get`、超时、JSON 解析、写文件。

---

### 阶段 1：HTTP 与公开 API（约 1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| HTTP 基础 | GET/POST、状态码 200/4xx/5xx、JSON |
| requests | `get/post`、`timeout`、`raise_for_status`、headers |
| 错误处理 | 网络失败、超时、非 200 的友好提示 |
| 持久化 | 结果存 JSON/CSV |

**练什么**

1. 从 [public-apis](https://github.com/public-apis/public-apis) 选 1 个免 Key 接口  
2. 做成 CLI：参数 → 请求 → 打印关键字段 → 可选 `--save`  
3. 可参考本仓库 [projects/api-cli](../../projects/api-cli/)

**验收**：断网或错误 URL 时程序不裸崩。

---

### 阶段 2：文件与批处理（约 1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| pathlib | 遍历、后缀、mkdir、rename/move |
| 安全 | **dry-run** 默认；重要目录先副本 |
| 文本/表格 | csv 模块或 openpyxl / 轻量 pandas |
| 日志 | `print` 分级或 `logging` 入门 |

**练什么**

1. 按扩展名整理文件夹（对照 [file-organizer](../../projects/file-organizer/)）  
2. 批量重命名（先 plan 再 apply）  
3. 读一文件夹文本，统计行数/关键字，输出报告  

**验收**：任何「移动/删除」类操作都有 dry-run。

---

### 阶段 3：解析与定时（可选 1 周）

**学什么**

| 主题 | 要点 |
|------|------|
| BeautifulSoup | 解析 HTML（仅合规公开页） |
| 定时 | 系统计划任务 / `schedule` 库（二选一先会一种） |
| 配置 | 路径、URL 放配置或环境变量，不写死密钥 |

**练什么**

1. 抓取**允许**的公开数据页，提取表格存 CSV（注意 robots/条款）  
2. 每天备份某目录为带日期的 zip  

**验收**：脚本可隔天再跑结果一致；README 写清依赖与风险。

---

### 阶段 4：工程化小作品（约 1 周）

**交付一个「作品集级」脚本项目**（放 `projects/automation-xxx/`）：

- README：如何安装、如何运行、示例输出  
- `requirements.txt`  
- 基本错误处理  
- （加分）`pytest` 测纯函数部分  

**选题池**

1. 多 API 聚合日报（JSON 汇总）  
2. 发票/账单文件名规范化（副本目录）  
3. 监控某目录新增文件并记日志  

---

## 三、资源清单

### 官方与系统教程

| 资源 | 说明 | 链接 |
|------|------|------|
| Automate the Boring Stuff | 自动化圣经，可免费在线读 | https://automatetheboringstuff.com/ |
| 书配套代码 | 对照章节练 | https://github.com/asweigart/automate-the-boring-stuff |
| requests 文档 | HTTP 客户端首选 | https://requests.readthedocs.io/ |
| pathlib 文档 | 路径处理 | https://docs.python.org/zh-cn/3/library/pathlib.html |
| logging 文档 | 日志 | https://docs.python.org/zh-cn/3/library/logging.html |

### 视频 / 课程（选一门即可）

| 资源 | 说明 |
|------|------|
| freeCodeCamp / B 站「Python 自动化」完整向 | 跟完一本即可，勿同时开三门 |
| 官方 requests 快速入门章节 | 优先于杂乱博客 |

### GitHub 读码与练手

完整表：[stage4-github-projects.md](../stage4-github-projects.md) 路线 A  

| 优先 | 仓库 |
|------|------|
| 读 | asweigart/automate-the-boring-stuff、psf/requests |
| 练 | public-apis/public-apis |
| 结构 | yt-dlp（只看入口与目录） |

### 工具栈建议（够用即可）

```
requests
pathlib（标准库）
python-dotenv（可选，管配置）
openpyxl 或 pandas（做 Excel 时再装）
schedule 或 系统计划任务
pytest（测纯函数）
```

---

## 四、能力自评

### 初级（方向及格线）

- [ ] 会调公开 API 并落盘  
- [ ] 会批处理文件且有 dry-run  
- [ ] 会写 requirements 与 README  

### 中级

- [ ] 会简单 HTML 解析（合规）  
- [ ] 会定时或可被外部调度  
- [ ] 核心逻辑有测试  

### 可展示

- [ ] `projects/` 下有一个别人能按 README 跑通的自动化工具  

---

## 五、与爬虫的关系

爬虫 = 自动化 + 解析 + **强烈合规意识**。  
学完阶段 1～2 再碰；优先 API，其次公开数据，避免对抗反爬与侵权。

下一步总入口：[README.md](README.md) · 阶段 4：[../../stage-4-tracks/automation/README.md](../../stage-4-tracks/automation/README.md)
