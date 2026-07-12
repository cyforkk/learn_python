# 【自检 · 不是作业】请先自己完成 ../ex05_refactor_functions.py

import runpy
import sys
from pathlib import Path

ex = Path(__file__).resolve().parents[1] / "ex05_refactor_functions.py"
text = ex.read_text(encoding="utf-8")
if "TODO: 在这里写你的代码" in text and text.count("\n") < 20:
    # 仍是骨架时给出提示
    ns = {}
    try:
        ns = runpy.run_path(str(ex))
    except Exception:
        pass
    if "level" not in ns:
        print("请先在 ex05_refactor_functions.py 里写 level 函数，再运行自检")
        sys.exit(1)

ns = runpy.run_path(str(ex))
level = ns.get("level")
assert callable(level), "需要定义函数 level"
assert level(95) == "A"
assert level(85) == "B"
assert level(70) == "C"
assert level(50) == "D"
print("ex05 自检通过")
