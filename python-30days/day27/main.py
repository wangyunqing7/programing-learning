"""第 27 天：SQLite 记账"""

def main() -> None:
    import sqlite3
    connection = sqlite3.connect(":memory:")
    connection.execute("create table expense(name text, amount integer)")
    connection.executemany("insert into expense values (?, ?)", [("book", 52), ("tea", 18)])
    print(connection.execute("select sum(amount) from expense").fetchone()[0])

if __name__ == "__main__":
    main()
