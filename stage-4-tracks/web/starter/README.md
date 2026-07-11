# Web starter

```bash
cd stage-4-tracks/web/starter
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

默认用 Flask `test_client` 验证接口，无需浏览器。  
真正起服务可执行：`flask --app main run`
