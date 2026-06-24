"""第 09 天：文本统计器"""

def main() -> None:
    text = "Python makes small tools pleasant"
    words = text.split()
    print("单词数:", len(words))
    print("最长单词:", max(words, key=len))

if __name__ == "__main__":
    main()
