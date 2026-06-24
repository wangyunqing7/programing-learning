"""第 21 天：日志记录器

掌握：logging 模块、分级、格式化、多 handler。
同时输出到控制台和文件，带时间戳和级别。
"""
from __future__ import annotations

import logging
from pathlib import Path
from tempfile import NamedTemporaryFile


def setup_logger(logfile: Path) -> logging.Logger:
    logger = logging.getLogger("day21")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s",
                            datefmt="%H:%M:%S")

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)

    file_h = logging.FileHandler(logfile, encoding="utf-8")
    file_h.setLevel(logging.DEBUG)
    file_h.setFormatter(fmt)

    logger.addHandler(console)
    logger.addHandler(file_h)
    return logger


def do_work(logger: logging.Logger) -> None:
    logger.debug("这是 debug，只在文件里出现")
    logger.info("开始处理任务")
    logger.info("任务进行中 50%")
    logger.warning("这是个警告，磁盘空间不足")
    logger.info("任务完成 100%")


def main() -> None:
    with NamedTemporaryFile("w", suffix=".log", delete=False, encoding="utf-8") as tmp:
        logfile = Path(tmp.name)
    logger = setup_logger(logfile)
    do_work(logger)

    print(f"\n日志文件内容（{logfile.name}）：")
    print(logfile.read_text(encoding="utf-8"))

    # 先关闭 handler（释放文件占用），再删除，避免 Windows 上文件被锁
    for h in logger.handlers:
        h.close()
    logfile.unlink()


if __name__ == "__main__":
    main()
