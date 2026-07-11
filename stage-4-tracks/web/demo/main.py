"""Web 中型 demo：内存待办 API（test_client 验证，可不常驻服务）。"""

from flask import Flask, jsonify, request

app = Flask(__name__)
_todos: list[dict] = []
_next_id = 1


@app.get("/todos")
def list_todos():
    return jsonify(_todos)


@app.post("/todos")
def add_todo():
    global _next_id
    body = request.get_json(force=True, silent=True) or {}
    text = (body.get("text") or "").strip()
    if not text:
        return jsonify({"error": "text required"}), 400
    item = {"id": _next_id, "text": text, "done": False}
    _next_id += 1
    _todos.append(item)
    return jsonify(item), 201


def main() -> None:
    client = app.test_client()
    r1 = client.post("/todos", json={"text": "学习 Flask"})
    r2 = client.get("/todos")
    print("POST", r1.status_code, r1.get_json())
    print("GET", r2.status_code, r2.get_json())
    print("启动服务: flask --app main run")


if __name__ == "__main__":
    main()
