"""第 25 天：文字冒险"""

def main() -> None:
    state = "start"
    transitions = {"start": "forest", "forest": "treasure", "treasure": "end"}
    while state != "end":
        print("当前位置:", state)
        state = transitions[state]
    print("冒险结束")

if __name__ == "__main__":
    main()
