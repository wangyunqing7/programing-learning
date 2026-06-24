"""第 22 天：递归目录摘要

掌握：递归思想、嵌套结构遍历。
递归统计一个「目录树」里的文件数和总大小，并打印缩进树。
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Summary:
    files: int = 0
    size: int = 0

    def add(self, size: int) -> None:
        self.files += 1
        self.size += size

    def __add__(self, other: "Summary") -> "Summary":
        return Summary(self.files + other.files, self.size + other.size)


def summarize(node) -> Summary:
    """node 要么是 int（文件大小），要么是 dict（子目录）。"""
    if isinstance(node, int):
        return Summary(1, node)
    total = Summary()
    for child in node.values():
        total = total + summarize(child)
    return total


def render_tree(node, name: str = ".", indent: int = 0) -> None:
    pad = "  " * indent
    if isinstance(node, int):
        print(f"{pad}{name} ({node} B)")
    else:
        s = summarize(node)
        print(f"{pad}{name}/ [{s.files} 文件, {s.size} B]")
        for child_name, child in node.items():
            render_tree(child, child_name, indent + 1)


def main() -> None:
    # 一棵模拟的目录树（不碰真实磁盘）
    tree = {
        "src": {
            "main.py": 1200,
            "utils": {"helper.py": 800, "config.py": 300},
        },
        "tests": {"test_main.py": 500},
        "README.md": 250,
    }
    render_tree(tree)
    print()
    print(f"总计：{summarize(tree)}")


if __name__ == "__main__":
    main()
