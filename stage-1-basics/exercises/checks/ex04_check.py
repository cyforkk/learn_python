# 【自检 · 不是作业】检查九九表是否打印了 9 行
# 新手可忽略本文件

import io
import runpy
import sys
from pathlib import Path

ex = Path(__file__).resolve().parents[1] / "ex04_multiplication_table.py"
buf = io.StringIO()
old = sys.stdout
sys.stdout = buf
try:
    runpy.run_path(str(ex), run_name="__main__")
finally:
    sys.stdout = old

lines = [ln for ln in buf.getvalue().splitlines() if ln.strip()]
assert len(lines) == 9, f"应打印 9 行，实际 {len(lines)} 行"
assert "1*1=1" in lines[0].replace(" ", "")
print("ex04 自检通过")
