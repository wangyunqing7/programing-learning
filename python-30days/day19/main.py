"""第 19 天：路径整理器"""

def main() -> None:
    from pathlib import Path
    paths = [Path("notes/day01.md"), Path("src/main.py"), Path("README.md")]
    for path in paths:
        print(path.suffix or "<no suffix>", path.name)

if __name__ == "__main__":
    main()
