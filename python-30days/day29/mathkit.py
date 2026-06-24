"""数学工具模块。"""
from __future__ import annotations


def safe_divmod(a: float, b: float) -> tuple[int, float]:
    if b == 0:
        raise ZeroDivisionError("除数为 0")
    q = int(a // b)
    r = a - q * b
    return q, r


def clamp(x: float, lo: float, hi: float) -> float:
    if lo > hi:
        raise ValueError("下限不能大于上限")
    return max(lo, min(hi, x))
