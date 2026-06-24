"""第 29 天：迷你包结构"""

def main() -> None:
    class Toolkit:
        @staticmethod
        def slug(text: str) -> str:
            return text.lower().replace(" ", "-")
    print(Toolkit.slug("Mini Package Demo"))

if __name__ == "__main__":
    main()
