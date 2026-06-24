"""第 09 天：文本统计器

掌握：字符串处理、collections.Counter、Top-N。
统计词频、字符数、最长词，并输出 Top-N。
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

# 简单的英文停用词
STOP_WORDS = {"the", "a", "an", "is", "to", "of", "and", "in", "it", "for"}


@dataclass
class Stats:
    chars: int
    words: list[str]
    top: list[tuple[str, int]]

    def render(self) -> None:
        print(f"  字符数：{self.chars}")
        print(f"  单词数：{len(self.words)}")
        longest = max(self.words, key=len) if self.words else ""
        print(f"  最长单词：{longest}")
        print("  词频 Top 5：")
        for word, n in self.top:
            print(f"    {word:<12} {n}")


def analyze(text: str, top_n: int = 5, remove_stop: bool = True) -> Stats:
    if not text.strip():
        raise ValueError("文本为空")
    # 标点简单清洗：替换成空格
    cleaned = text
    for ch in ",.;:!?\"'()[]":
        cleaned = cleaned.replace(ch, " ")
    words = [w.lower() for w in cleaned.split() if w]
    if remove_stop:
        words = [w for w in words if w not in STOP_WORDS]
    counter = Counter(words)
    top = counter.most_common(top_n)
    return Stats(chars=len(text.replace(" ", "")), words=words, top=top)


def main() -> None:
    text = ("Python is a great language and python is easy to learn. "
            "Many people love python for its simple syntax.")
    print("全文统计：")
    analyze(text).render()

    # 边界
    print()
    try:
        analyze("   ")
    except ValueError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
