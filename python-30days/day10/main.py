"""第 10 天：临时笔记文件"""

def main() -> None:
    from pathlib import Path
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp:
        note = Path(tmp) / "note.txt"
        note.write_text("今天学习文件读写", encoding="utf-8")
        print(note.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
