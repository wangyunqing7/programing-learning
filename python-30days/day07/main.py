"""第 07 天：单位换算函数"""

def main() -> None:
    def kilometers_to_miles(km: float) -> float:
        return km * 0.621371

    for km in [1, 5, 10]:
        print(f"{km} km = {kilometers_to_miles(km):.2f} miles")

if __name__ == "__main__":
    main()
