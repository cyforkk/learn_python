# 公开 API 查询 CLI（api-cli）

对应规格：`stage-5-projects/exercises/project_spec_03_api_cli.md`

使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 演示，**无需 API Key**。

## 安装与运行

```bash
cd projects/api-cli
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python main.py              # 查询 id=1
python main.py 5            # 查询 id=5
python main.py 3 --save out.json
python main.py -h           # 帮助
```

## 错误处理

- 超时 / 断网：打印友好中文提示后退出  
- 非 200：打印 HTTP 状态码  
