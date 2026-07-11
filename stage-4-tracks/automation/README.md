# 方向：自动化 / 脚本

## 常见技能

- `requests`：HTTP 请求  
- 文件批量处理：`pathlib`  
- Excel：`openpyxl` 或轻量使用 `pandas`  
- 网页解析：`BeautifulSoup`（注意合规）

## 入门资源

- Automate the Boring Stuff：https://automatetheboringstuff.com/  
- requests 文档：https://requests.readthedocs.io/

## 先跑 starter → 再跑 demo

- [starter/](starter/)：`pip install -r requirements.txt` → `python main.py`  
- [demo/](demo/)：批量请求并保存 JSON  

## GitHub：读码与练手

完整表见 → **[docs/stage4-github-projects.md](../../docs/stage4-github-projects.md)**（路线 A）

| 类型 | 仓库 | 你怎么做 |
|------|------|----------|
| 读码 | [asweigart/automate-the-boring-stuff](https://github.com/asweigart/automate-the-boring-stuff) | 对照书中某一章代码，看文件/Excel/请求怎么写 |
| 读码 | [psf/requests](https://github.com/psf/requests) | 看 README 与文档示例，对照本仓库 starter |
| 练手 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 选 1 个免 Key API，写查询并落盘（可扩展 demo） |
| 练手 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 读一个简单算法文件并默写；或小贡献文档/测试 |
| 进阶结构 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 只看 CLI 入口与目录分层，不求全懂 |

## 最小 demo 选题

1. 调用公开 API，把结果存成 JSON/CSV  
2. 按扩展名整理某个文件夹  
3. 批量重命名文件（先在副本目录试）

代码建议路径：`projects/automation-demo/`
