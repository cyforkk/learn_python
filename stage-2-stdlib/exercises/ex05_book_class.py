# 练习：Book 类（最简单版）
# 先读笔记：面向对象入门
# 运行：python ex05_book_class.py


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"《{self.title}》- {self.author}, {self.pages}页"

    def is_long(self):
        return self.pages >= 300


b1 = Book("Python 入门", "张三", 200)
b2 = Book("厚书", "李四", 500)

print(b1.info(), "长书?", b1.is_long())
print(b2.info(), "长书?", b2.is_long())
