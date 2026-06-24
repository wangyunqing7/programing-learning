"""第 14 天：图书 dataclass"""

def main() -> None:
    from dataclasses import dataclass
    @dataclass
    class Book:
        title: str
        pages: int
    books = [Book("Python 入门", 180), Book("自动化脚本", 220)]
    print(max(books, key=lambda book: book.pages))

if __name__ == "__main__":
    main()
