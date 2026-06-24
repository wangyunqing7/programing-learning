"""第 03 天：成绩判断器

掌握：if/elif/else 多分支。
对一批学生成绩做等级评定和加权统计，输出班级报告。
"""
from __future__ import annotations


def grade_of(score: float) -> str:
    """单科成绩 -> 等级。"""
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    elif score >= 0:
        return "不及格"
    else:
        raise ValueError(f"非法分数：{score}")


def weighted_total(scores: dict[str, float], weights: dict[str, float]) -> float:
    """按权重算加权总分。"""
    if abs(sum(weights.values()) - 1.0) > 1e-6:
        raise ValueError("权重之和必须等于 1")
    return sum(scores.get(subj, 0) * w for subj, w in weights.items())


def class_report(students: list[dict]) -> None:
    """打印班级报告：每个学生的加权分 + 等级 + 班级均值。"""
    weights = {"math": 0.5, "english": 0.3, "python": 0.2}
    print(f"{'姓名':<8}{'加权分':<10}{'等级':<8}")
    print("-" * 30)

    totals = []
    for s in students:
        try:
            total = weighted_total(s["scores"], weights)
            totals.append(total)
            print(f"{s['name']:<8}{total:<10.1f}{grade_of(total):<8}")
        except ValueError as e:
            print(f"{s['name']:<8}数据错误：{e}")

    if totals:
        print("-" * 30)
        print(f"班级加权均分：{sum(totals) / len(totals):.1f}")


def main() -> None:
    students = [
        {"name": "Ada", "scores": {"math": 95, "english": 88, "python": 92}},
        {"name": "Linus", "scores": {"math": 78, "english": 65, "python": 85}},
        {"name": "Grace", "scores": {"math": 55, "english": 72, "python": 48}},
    ]
    class_report(students)

    # 边界：非法分数
    print()
    try:
        grade_of(-10)
    except ValueError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
