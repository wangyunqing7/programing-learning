"""第 23 天：排序和搜索"""

def main() -> None:
    students = [{"name": "Ada", "score": 95}, {"name": "Linus", "score": 88}]
    students.sort(key=lambda item: item["score"], reverse=True)
    print(students)
    print(next(item for item in students if item["name"] == "Ada"))

if __name__ == "__main__":
    main()
