"""第 01 天：Hello CLI

今天掌握三件事：print 输出、变量与字符串、以及脚本入口 __name__。
这个小程序能根据你传入的名字打招呼，还能切换语言、打印一张文字名片。
运行：python main.py [你的名字]
"""

from __future__ import annotations

import sys


# 不同语言的问候模板，用字典做一张「语言 -> 模板」的映射表
GREETINGS: dict[str, dict[str, str]] = {
    "zh": {"hello": "你好，{name}！欢迎开始 Python 30 天之旅。", "lang_name": "中文"},
    "en": {"hello": "Hello, {name}! Welcome to the 30-day Python journey.", "lang_name": "English"},
    "ja": {"hello": "こんにちは、{name}さん！Python 30 日旅へようこそ。", "lang_name": "日本語"},
}


def pick_name(argv: list[str]) -> str:
    """从命令行参数里取名字；没给就用默认值。

    边界处理：argv 可能没传名字，或传了多个（只取第一个）。
    """
    if len(argv) >= 2 and argv[1].strip():
        return argv[1].strip()
    return "Python 学习者"


def greet(name: str, lang: str = "zh") -> str:
    """根据语言返回问候语。

    .format(name=name) 会把模板里的 {name} 替换成实际名字。
    如果语言不存在，就退回中文，避免 KeyError。
    """
    template = GREETINGS.get(lang, GREETINGS["zh"])
    return template["hello"].format(name=name)


def make_card(name: str, lang: str) -> str:
    """用字符串拼接和居中对齐，生成一张文字名片。"""
    bar = "+" + "-" * 26 + "+"
    lines = [
        bar,
        "|" + "Python 30 天 · Day 01".center(24) + "  |",
        "|" + "-".center(24) + "  |",
        "|" + name.center(24) + "  |",
        "|" + GREETINGS[lang]["lang_name"].center(24) + "  |",
        bar,
    ]
    return "\n".join(lines)


def list_languages() -> None:
    """列出所有可选语言，演示如何遍历字典。"""
    print("可选语言：")
    for code, info in GREETINGS.items():
        print(f"  {code} -> {info['lang_name']}")


def main() -> None:
    name = pick_name(sys.argv)

    print("=" * 40)
    print(greet(name))
    print("=" * 40)

    # 演示切换语言
    for lang in ("zh", "en", "ja"):
        print(greet(name, lang))

    print()
    print(make_card(name, "zh"))
    print()
    list_languages()

    # 课后练习提示：试试在终端运行 python main.py 你的名字


if __name__ == "__main__":
    main()
