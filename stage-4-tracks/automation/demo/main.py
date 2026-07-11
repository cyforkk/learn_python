"""自动化中型 demo：拉多个公开 todo 并保存为 JSON。"""

from __future__ import annotations

import json
from pathlib import Path

import requests

OUT = Path(__file__).with_name("todos_sample.json")
BASE = "https://jsonplaceholder.typicode.com/todos"


def fetch_todos(ids: list[int]) -> list[dict]:
    items: list[dict] = []
    for i in ids:
        r = requests.get(f"{BASE}/{i}", timeout=10)
        r.raise_for_status()
        items.append(r.json())
    return items


def main() -> None:
    ids = [1, 2, 3]
    try:
        data = fetch_todos(ids)
    except requests.RequestException as e:
        print("请求失败:", e)
        return
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"已保存 {len(data)} 条到 {OUT.name}")
    for item in data:
        print("-", item.get("id"), item.get("title", "")[:40])


if __name__ == "__main__":
    main()
