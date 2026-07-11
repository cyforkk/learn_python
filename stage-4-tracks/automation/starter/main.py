"""自动化方向 starter：用 requests 请求公开接口。"""

import requests

# jsonplaceholder 相对稳定；若失败可换其他公开 API
URL = "https://jsonplaceholder.typicode.com/todos/1"


def fetch_todo() -> dict:
    r = requests.get(URL, timeout=10)
    r.raise_for_status()
    return r.json()


def main() -> None:
    try:
        data = fetch_todo()
    except requests.RequestException as e:
        print("请求失败（检查网络）:", e)
        return
    print("id:", data.get("id"))
    print("title:", data.get("title"))
    print("completed:", data.get("completed"))


if __name__ == "__main__":
    main()
