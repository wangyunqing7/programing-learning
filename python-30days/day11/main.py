"""第 11 天：JSON 任务数据"""

def main() -> None:
    import json
    tasks = [{"title": "学习 json", "done": False}, {"title": "保存数据", "done": True}]
    text = json.dumps(tasks, ensure_ascii=False, indent=2)
    print(text)
    print("已完成:", sum(1 for item in json.loads(text) if item["done"]))

if __name__ == "__main__":
    main()
