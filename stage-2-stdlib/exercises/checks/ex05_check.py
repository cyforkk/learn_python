# 【自检 · 不是作业】

import runpy
from pathlib import Path

ns = runpy.run_path(str(Path(__file__).resolve().parents[1] / "ex05_book_class.py"))
Book = ns["Book"]
b = Book("t", "a", 400)
assert b.is_long() is True
assert "t" in b.info()
print("ex05 自检通过")
