"""第 18 天：日期计划表"""

def main() -> None:
    from datetime import date, timedelta
    today = date.today()
    plan = [today + timedelta(days=offset) for offset in range(3)]
    for item in plan:
        print(item.isoformat())

if __name__ == "__main__":
    main()
