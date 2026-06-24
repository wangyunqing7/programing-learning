"""第 20 天：参数解析器"""

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Python 学习者")
    args = parser.parse_args([])
    print(f"你好，{args.name}")

if __name__ == "__main__":
    main()
