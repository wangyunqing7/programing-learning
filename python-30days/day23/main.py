"""第 23 天：排序和搜索

掌握：sorted 的 key 函数、二分查找 bisect。
对学生按多关键字排序，并在有序列表里二分查找。
"""
from __future__ import annotations

import bisect
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


def by_score_then_name(students: list[Student]) -> list[Student]:
    """分数降序，同分按名字升序。"""
    return sorted(students, key=lambda s: (-s.score, s.name))


def rank_of(sorted_scores: list[int], target: int) -> int:
    """在有序分数列表里，用二分找 target 应插入的位置（即它的名次）。"""
    return len(sorted_scores) - bisect.bisect_right(sorted_scores, target) + 1


def main() -> None:
    students = [
        Student("Ada", 95), Student("Linus", 88), Student("Grace", 88),
        Student("Alan", 76), Student("Ken", 95),
    ]
    print("按分数降序、同分按名字：")
    for s in by_score_then_name(students):
        print(f"  {s.name:<8} {s.score}")

    # 二分查找名次
    scores_sorted = sorted(s.score for s in students)
    print(f"\n分数升序列表：{scores_sorted}")
    for target in (95, 88, 76, 60):
        print(f"  {target} 分的名次约：第 {rank_of(scores_sorted, target)} 名")

    # 边界：空列表
    print()
    print(f"空列表找 90：名次 {rank_of([], 90)}")


if __name__ == "__main__":
    main()
