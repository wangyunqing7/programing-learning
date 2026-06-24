"""第 17 天：CSV 成绩表"""

def main() -> None:
    import csv
    from io import StringIO
    data = "name,score\nAda,95\nLinus,88\n"
    rows = list(csv.DictReader(StringIO(data)))
    print("最高分:", max(rows, key=lambda row: int(row["score"])))

if __name__ == "__main__":
    main()
