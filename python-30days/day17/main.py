"""第 17 天：CSV 成绩表

掌握：csv 读写、聚合统计。
把成绩写进 CSV，再读回来做最高分、均分、排名。
"""
from __future__ import annotations

import csv
import statistics
from pathlib import Path
from tempfile import NamedTemporaryFile


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "math", "english", "python"])
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict]:
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # 把分数字段转成 int
        return [{"name": r["name"],
                 "math": int(r["math"]),
                 "english": int(r["english"]),
                 "python": int(r["python"])} for r in reader]


def report(rows: list[dict]) -> None:
    for subj in ("math", "english", "python"):
        scores = [r[subj] for r in rows]
        print(f"  {subj:<8} 均 {statistics.mean(scores):.1f}  "
              f"最高 {max(scores)}  最低 {min(scores)}")
    # 按总分排名
    ranked = sorted(rows, key=lambda r: r["math"] + r["english"] + r["python"],
                    reverse=True)
    print("  排名：")
    for i, r in enumerate(ranked, 1):
        total = r["math"] + r["english"] + r["python"]
        print(f"    {i}. {r['name']:<8} {total}")


def main() -> None:
    data = [
        {"name": "Ada", "math": 95, "english": 88, "python": 92},
        {"name": "Linus", "math": 78, "english": 65, "python": 85},
        {"name": "Grace", "math": 55, "english": 72, "python": 48},
    ]
    with NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        path = Path(tmp.name)
    write_csv(path, data)
    print(f"已写入：{path.name}")

    rows = read_csv(path)
    print("统计报告：")
    report(rows)
    path.unlink()

    # 边界：空表
    print()
    try:
        report([])
    except statistics.StatisticsError as e:
        print(f"边界测试：{e}")


if __name__ == "__main__":
    main()
