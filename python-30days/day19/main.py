"""第 19 天：路径整理器

掌握：pathlib 路径分析、PurePath。
把一堆杂乱的路径字符串整理成统计报告（不实际改文件）。
"""
from __future__ import annotations

from pathlib import PurePath, PureWindowsPath, PurePosixPath


def normalize(raw: str) -> PurePath:
    """根据分隔符猜测是 Windows 还是 Posix 路径。"""
    if "\\" in raw:
        return PureWindowsPath(raw)
    return PurePosixPath(raw)


def summarize(paths: list[str]) -> None:
    exts: dict[str, int] = {}
    print(f"{'路径':<40}{'根':<8}{'父目录':<16}{'文件名'}")
    print("-" * 80)
    for raw in paths:
        p = normalize(raw)
        ext = p.suffix.lower() or "(无)"
        exts[ext] = exts.get(ext, 0) + 1
        print(f"{str(p):<40}{p.anchor or '-':<8}{str(p.parent):<16}{p.name}")
    print("-" * 80)
    print("扩展名统计：", exts)


def main() -> None:
    paths = [
        r"C:\Users\ada\project\main.py",
        r"C:\Users\ada\project\README.md",
        "/home/linus/app/utils.py",
        "/var/log/app.log",
        "notes.txt",
    ]
    summarize(paths)


if __name__ == "__main__":
    main()
