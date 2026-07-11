"""核心函数测试：pytest test_todo.py -q"""

from pathlib import Path

from todo import add_todo, delete_todo, format_list, load_todos, mark_done, save_todos


def test_add_and_mark(tmp_path: Path) -> None:
    path = tmp_path / "t.json"
    todos: list[dict] = []
    add_todo(todos, "任务A")
    add_todo(todos, "任务B")
    assert mark_done(todos, 1) is True
    assert todos[0]["done"] is True
    save_todos(todos, path)
    loaded = load_todos(path)
    assert len(loaded) == 2
    assert loaded[0]["text"] == "任务A"


def test_delete_and_format() -> None:
    todos: list[dict] = []
    add_todo(todos, "x")
    add_todo(todos, "y")
    assert delete_todo(todos, 1) is True
    assert len(todos) == 1
    assert "y" in format_list(todos)
    assert delete_todo(todos, 9) is False
