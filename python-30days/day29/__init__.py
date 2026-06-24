"""迷你工具包：聚合子模块。"""
from .stringkit import slug, truncate
from .mathkit import safe_divmod, clamp

__all__ = ["slug", "truncate", "safe_divmod", "clamp"]
__version__ = "0.1.0"
