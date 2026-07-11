"""数据分析方向 starter：pandas 读 CSV 做简单统计。"""

from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).with_name("sample.csv")


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    print("行数:", len(df))
    print("平均分:", round(float(df["score"].mean()), 2))
    print("按城市人数:")
    print(df.groupby("city").size())


if __name__ == "__main__":
    main()
