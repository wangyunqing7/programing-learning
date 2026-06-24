"""第 15 天：列表推导统计

掌握：列表/字典/集合推导式、过滤、多维统计。
对一组学生成绩做多角度统计。
"""
from __future__ import annotations

import statistics


def analyze(students: list[dict]) -> None:
    # 把每个学生的 python 分数抽出来
    python_scores = [s["python"] for s in students]
    # 过滤出及格的
    passed = [s for s in python_scores if s >= 60]
    # 推导 + 条件表达式打标签
    tags = [f"{s['name']}:{'优' if p>=90 else '良' if p>=75 else '及格'}"
            for s in students if (p := s["python"]) >= 60]
    # 字典推导：名字 -> 总分
    totals = {s["name"]: s["math"] + s["english"] + s["python"] for s in students}

    print(f"  Python 均分：{statistics.mean(python_scores):.1f}")
    print(f"  Python 中位数：{statistics.median(python_scores)}")
    print(f"  及格人数：{len(passed)} / {len(students)}")
    print(f"  标准差：{statistics.pstdev(python_scores):.1f}")
    print(f"  等级：{tags}")
    print(f"  各人总分：{totals}")


def main() -> None:
    students = [
        {"name": "Ada", "math": 95, "english": 88, "python": 92},
        {"name": "Linus", "math": 78, "english": 65, "python": 85},
        {"name": "Grace", "math": 55, "english": 72, "python": 48},
        {"name": "Alan", "math": 88, "english": 90, "python": 76},
    ]
    print("成绩统计：")
    analyze(students)

    # 边界：空列表
    print()
    try:
        analyze([])
    except statistics.StatisticsError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
