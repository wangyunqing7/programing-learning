"""第 05 天：任务列表"""

def main() -> None:
    tasks = ["安装 Python", "运行脚本"]
    tasks.append("修改列表")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    main()
