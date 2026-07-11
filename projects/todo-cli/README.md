# 命令行待办清单（todo-cli）

对应规格：`stage-5-projects/exercises/project_spec_01_todo_cli.md`

## 运行

```bash
cd projects/todo-cli
python todo.py
```

## 命令

| 命令 | 说明 |
|------|------|
| `add 买牛奶` | 添加任务 |
| `list` | 列出全部 |
| `done 1` | 标记第 1 条完成 |
| `delete 1` | 删除第 1 条 |
| `quit` | 保存并退出 |

数据文件：同目录 `todos.json`（UTF-8）。

## 测试

```bash
pip install pytest
pytest -q
```
