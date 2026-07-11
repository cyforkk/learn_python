# 【自检 · 不是作业】检查 level 函数
# 新手可忽略本文件

import runpy
from pathlib import Path

ex = Path(__file__).resolve().parents[1] / "ex05_refactor_functions.py"
ns = runpy.run_path(str(ex))
level = ns.get("level")
assert callable(level), "需要定义函数 level"
assert level(95) == "A"
assert level(85) == "B"
assert level(70) == "C"
assert level(50) == "D"
print("ex05 自检通过")
