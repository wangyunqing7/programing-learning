"""字符串工具模块。"""


def slug(text: str) -> str:
    """转成 URL 友好的 slug。"""
    return "-".join(text.lower().split())


def truncate(text: str, width: int) -> str:
    if width < 3:
        raise ValueError("宽度至少 3")
    return text if len(text) <= width else text[: width - 3] + "..."
