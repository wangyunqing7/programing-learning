"""第 10 天：临时笔记文件

掌握：pathlib、文件读写、临时目录。
在临时目录里建一个多页笔记本，读写并列表。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from tempfile import TemporaryDirectory


@dataclass
class Notebook:
    root: Path
    pages: list[str] = field(default_factory=list)

    def write(self, name: str, content: str) -> Path:
        path = self.root / f"{name}.md"
        path.write_text(content, encoding="utf-8")
        if name not in self.pages:
            self.pages.append(name)
        return path

    def read(self, name: str) -> str:
        path = self.root / f"{name}.md"
        if not path.exists():
            raise FileNotFoundError(f"没有这页笔记：{name}")
        return path.read_text(encoding="utf-8")

    def list_pages(self) -> list[Path]:
        return sorted(self.root.glob("*.md"))


def main() -> None:
    with TemporaryDirectory() as d:
        nb = Notebook(Path(d))
        nb.write("day10", "# 临时笔记\n今天学习 pathlib 读写文件。")
        nb.write("todo", "# TODO\n- 练习 read_text\n- 练习 glob")

        print(f"笔记目录：{nb.root}")
        print("所有笔记文件：")
        for p in nb.list_pages():
            print(f"  {p.name} ({p.stat().st_size} 字节)")

        print("\n读取 day10：")
        print(nb.read("day10"))

        # 边界：读不存在的页
        print()
        try:
            nb.read("missing")
        except FileNotFoundError as e:
            print(f"边界测试：{e}")

    print(f"\n临时目录已自动清理：{not Path(d).exists()}")


if __name__ == "__main__":
    main()
