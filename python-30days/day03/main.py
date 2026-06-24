"""第 03 天：成绩判断器"""

def main() -> None:
    score = 86
    if score >= 90:
        level = "优秀"
    elif score >= 75:
        level = "良好"
    else:
        level = "继续练习"
    print(f"分数 {score}：{level}")

if __name__ == "__main__":
    main()
