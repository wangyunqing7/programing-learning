"""第 24 天：支出统计器"""

def main() -> None:
    expenses = [{"tag": "book", "amount": 52}, {"tag": "food", "amount": 34}, {"tag": "book", "amount": 20}]
    summary = {}
    for item in expenses:
        summary[item["tag"]] = summary.get(item["tag"], 0) + item["amount"]
    print(summary)

if __name__ == "__main__":
    main()
