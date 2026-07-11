"""数据中型 demo：清洗 + 分组汇总 + 导出。"""

from pathlib import Path

import pandas as pd

SRC = Path(__file__).with_name("sales.csv")
OUT = Path(__file__).with_name("summary_by_city.csv")


def main() -> None:
    df = pd.read_csv(SRC)
    df = df.dropna()
    df["amount"] = df["amount"].astype(int)
    summary = df.groupby("city", as_index=False)["amount"].sum()
    summary = summary.sort_values("amount", ascending=False)
    summary.to_csv(OUT, index=False, encoding="utf-8")
    print(summary)
    print("已导出", OUT.name)


if __name__ == "__main__":
    main()
