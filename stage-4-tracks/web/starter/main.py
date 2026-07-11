"""Web 方向 starter：最小 Flask JSON 接口（用 test_client 一次跑通）。"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/echo/<name>")
def echo(name: str):
    return jsonify({"hello": name})


def main() -> None:
    # 不常驻起服务，用测试客户端验证路由（学习时也可改成 app.run()）
    client = app.test_client()
    r1 = client.get("/health")
    r2 = client.get("/echo/Ada")
    print("health:", r1.status_code, r1.get_json())
    print("echo:", r2.status_code, r2.get_json())
    print("若要启动服务: flask --app main run  或  app.run()")


if __name__ == "__main__":
    main()
