"""第 18 天：日期计划表

掌握：datetime、timedelta、日期运算。
做一个学习计划排期表，带倒计时。
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class Plan:
    start: date
    tasks: list[str]

    def schedule(self) -> list[tuple[date, str]]:
        return [(self.start + timedelta(days=i), t)
                for i, t in enumerate(self.tasks)]

    def countdown(self, today: date, target: date) -> int:
        return (target - today).days


def render(plan: Plan, today: date) -> None:
    print(f"今天：{today}（周{today.weekday() + 1}）")
    for d, task in plan.schedule():
        days = (d - today).days
        tag = "今天" if days == 0 else f"{days:+d}天"
        print(f"  {d} [{tag}] {task}")


def main() -> None:
    today = date.today()
    plan = Plan(start=today,
                tasks=["基础语法", "数据结构", "函数", "文件IO", "面向对象"])
    render(plan, today)

    # 倒计时：距离计划结束还有几天
    end = plan.schedule()[-1][0]
    print(f"\n距离计划最后一天（{end}）还有 {plan.countdown(today, end)} 天")

    # 边界：过去日期
    print()
    past = today - timedelta(days=10)
    print(f"10 天前是 {past}，到今天的倒计时：{plan.countdown(past, today)} 天")


if __name__ == "__main__":
    main()
