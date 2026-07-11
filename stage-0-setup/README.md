# 阶段 0 · 环境附录（可选 · 默认可跳过）

> 本仓库**默认你已经装好 Python**，主线从 [stage-1-basics](../stage-1-basics/README.md) 开始。  
> 只有装不上、命令找不到、中文乱码时，才需要看这里。

## 什么时候用

| 情况 | 建议 |
|------|------|
| `python --version` 正常 | **跳过本目录**，去 stage-1 |
| 没装 Python / PATH 不对 | 读下方文档或 [docs/windows-setup.md](../docs/windows-setup.md) |
| 只想确认能跑 | 执行一次 `hello.py` 即可 |

## 最小确认（30 秒）

```bash
python --version
# 或 Windows: py -3 --version

python stage-0-setup/hello.py
```

看到版本号和 `Hello, Python!` 就够了。

## 文档（按需点开）

| 文档 | 说明 |
|------|------|
| [notes/安装与编辑器.md](notes/安装与编辑器.md) | 安装与编辑器 |
| [notes/编码与控制台.md](notes/编码与控制台.md) | UTF-8、路径 |
| [docs/windows-setup.md](../docs/windows-setup.md) | Windows 细节 |
| [docs/faq-common-mistakes.md](../docs/faq-common-mistakes.md) | 常见报错 |

`venv`、依赖管理等到 **[stage-3](../stage-3-engineering/README.md)** 再系统学即可。

## 下一步（主线）

→ **[stage-1-basics](../stage-1-basics/README.md)**
