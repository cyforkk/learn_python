"""公开 API 查询 CLI：获取 JSONPlaceholder 上的 todo 条目。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import requests

BASE = "https://jsonplaceholder.typicode.com/todos"


def fetch_todo(todo_id: int, timeout: float = 10.0) -> dict:
    url = f"{BASE}/{todo_id}"
    try:
        r = requests.get(url, timeout=timeout)
    except requests.Timeout:
        raise SystemExit("请求超时，请检查网络后重试。") from None
    except requests.RequestException as e:
        raise SystemExit(f"网络错误: {e}") from None

    if r.status_code != 200:
        raise SystemExit(f"HTTP {r.status_code}: 无法获取 id={todo_id}")

    return r.json()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="查询 JSONPlaceholder 待办（无需 API Key）"
    )
    parser.add_argument(
        "id",
        type=int,
        nargs="?",
        default=1,
        help="待办 id，默认 1",
    )
    parser.add_argument(
        "--save",
        type=Path,
        metavar="FILE",
        help="将 JSON 保存到文件",
    )
    args = parser.parse_args(argv)

    if args.id < 1:
        print("id 必须是正整数", file=sys.stderr)
        raise SystemExit(2)

    data = fetch_todo(args.id)
    print(f"id:        {data.get('id')}")
    print(f"userId:    {data.get('userId')}")
    print(f"title:     {data.get('title')}")
    print(f"completed: {data.get('completed')}")

    if args.save:
        args.save.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"已保存到 {args.save}")


if __name__ == "__main__":
    main()
