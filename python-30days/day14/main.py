"""第 14 天：图书 dataclass（图书馆）

掌握：dataclass、对象列表、库存管理。
图书馆：藏书、借阅、归还、搜索。
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    copies: int = 1

    def __str__(self) -> str:
        return f"《{self.title}》-{self.author} (馆藏 {self.copies})"


@dataclass
class Library:
    books: dict[str, Book] = field(default_factory=dict)
    borrowed: dict[str, int] = field(default_factory=dict)  # title -> 借出数

    def add(self, book: Book) -> None:
        if book.title in self.books:
            self.books[book.title].copies += book.copies
        else:
            self.books[book.title] = book

    def borrow(self, title: str) -> None:
        book = self.books.get(title)
        if book is None:
            raise KeyError(f"没有这本书：{title}")
        available = book.copies - self.borrowed.get(title, 0)
        if available <= 0:
            raise ValueError(f"《{title}》已全部借出")
        self.borrowed[title] = self.borrowed.get(title, 0) + 1

    def return_book(self, title: str) -> None:
        if self.borrowed.get(title, 0) <= 0:
            raise ValueError(f"《{title}》没有被借出")
        self.borrowed[title] -= 1

    def search(self, keyword: str) -> list[Book]:
        kw = keyword.lower()
        return [b for b in self.books.values()
                if kw in b.title.lower() or kw in b.author.lower()]

    def status(self) -> list[tuple[Book, int]]:
        return [(b, b.copies - self.borrowed.get(b.title, 0))
                for b in self.books.values()]


def main() -> None:
    lib = Library()
    lib.add(Book("流畅的Python", "Ramalho", copies=2))
    lib.add(Book("Python Cookbook", "Beazley", copies=1))
    lib.add(Book("深入理解计算机系统", "Bryant"))

    print("馆藏：")
    for book, avail in lib.status():
        print(f"  {book} | 可借 {avail}")

    lib.borrow("流畅的Python")
    lib.borrow("流畅的Python")
    print("\n借出两本《流畅的Python》后：")
    for book, avail in lib.status():
        print(f"  {book.title} 可借 {avail}")

    lib.return_book("流畅的Python")
    print("\n归还一本后可借：",
          [a for t, a in lib.status() if t.title == "流畅的Python"][0])

    # 边界：不存在
    try:
        lib.borrow("不存在的书")
    except KeyError as e:
        print(f"\n边界测试：{e}")


if __name__ == "__main__":
    main()
