"""第 22 天：递归目录摘要"""

def main() -> None:
    def total_files(tree: dict) -> int:
        return sum(1 if value == "file" else total_files(value) for value in tree.values())
    project = {"src": {"main.py": "file"}, "README.md": "file"}
    print("文件数量:", total_files(project))

if __name__ == "__main__":
    main()
