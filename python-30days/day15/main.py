"""第 15 天：列表推导统计"""

def main() -> None:
    import statistics
    numbers = [12, 18, 21, 30, 33, 42]
    evens = [n for n in numbers if n % 2 == 0]
    print("偶数:", evens)
    print("平均值:", statistics.mean(numbers))

if __name__ == "__main__":
    main()
