"""第 04 天：乘法表生成器"""

def main() -> None:
    for row in range(1, 6):
        line = [f"{row}x{col}={row * col:2d}" for col in range(1, 6)]
        print("  ".join(line))

if __name__ == "__main__":
    main()
