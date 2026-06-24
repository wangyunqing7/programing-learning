"""第 20 天：参数解析器

掌握：argparse、多参数、子命令。
一个有 add/list 子命令的小 CLI。
"""
from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo",
                                     description="迷你 TODO CLI")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="添加任务")
    p_add.add_argument("title", help="任务标题")
    p_add.add_argument("--priority", type=int, default=2, choices=[1, 2, 3])

    p_list = sub.add_parser("list", help="列出任务")
    p_list.add_argument("--all", action="store_true", help="包含已完成")

    return parser


def dispatch(args: argparse.Namespace, store: list) -> None:
    if args.command == "add":
        store.append({"title": args.title, "priority": args.priority, "done": False})
        if args.verbose:
            print(f"[详细] 添加了 P{args.priority}: {args.title}")
        else:
            print(f"已添加：{args.title}")
    elif args.command == "list":
        items = store if args.all else [t for t in store if not t["done"]]
        if not items:
            print("（空）")
        for i, t in enumerate(items, 1):
            mark = "x" if t["done"] else " "
            print(f"  {i}. [{mark}] (P{t['priority']}) {t['title']}")


def run(argv: list[str], store: list) -> None:
    args = build_parser().parse_args(argv)
    dispatch(args, store)


def main() -> None:
    store: list = []
    # 演示：依次执行几条命令
    for argv in [
        ["add", "学完 day20", "--priority", "1"],
        ["add", "写 argparse 练习"],
        ["-v", "add", "复习子命令"],
        ["list"],
        ["list", "--all"],
    ]:
        print(f"$ todo {' '.join(argv)}")
        run(argv, store)
        print()

    # 边界：缺子命令
    print("$ todo")
    try:
        run([], store)
    except SystemExit:
        print("  （argparse 缺子命令时自动报错退出）")


if __name__ == "__main__":
    main()
