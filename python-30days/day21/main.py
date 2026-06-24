"""第 21 天：日志记录器"""

def main() -> None:
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    logging.info("开始处理学习任务")
    logging.warning("这是一个练习用警告")

if __name__ == "__main__":
    main()
