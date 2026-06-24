"""第 30 天：学习仪表盘"""

def main() -> None:
    skills = {"基础": 10, "文件": 4, "数据": 6, "测试": 2}
    completed = sum(skills.values())
    for name, count in skills.items():
        print(f"{name}: {count}")
    print("总练习点:", completed)

if __name__ == "__main__":
    main()
