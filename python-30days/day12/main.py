"""第 12 天：安全除法"""

def main() -> None:
    def safe_divide(left: float, right: float) -> float | None:
        try:
            return left / right
        except ZeroDivisionError:
            return None

    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

if __name__ == "__main__":
    main()
