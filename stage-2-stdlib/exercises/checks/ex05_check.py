# 【自检 · 不是作业】请先自己完成 ../ex05_book_class.py

import runpy
import sys
from pathlib import Path

ex = Path(__file__).resolve().parents[1] / "ex05_book_class.py"
ns = runpy.run_path(str(ex))
Book = ns.get("Book")
if Book is None:
    print("请先在 ex05_book_class.py 里定义 Book 类，再运行自检")
    sys.exit(1)
b = Book("t", "a", 400)
assert b.is_long() is True
assert "t" in b.info()
print("ex05 自检通过")
