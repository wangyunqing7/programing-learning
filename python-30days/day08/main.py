"""第 08 天：密码建议器

掌握：random、字符串方法、函数组合、强度评估。
按规则生成密码并打分。
"""
from __future__ import annotations

import random
import string


def generate(length: int = 12,
             use_upper: bool = True,
             use_digit: bool = True,
             use_symbol: bool = True) -> str:
    if length < 4:
        raise ValueError("密码至少 4 位")
    pool = list(string.ascii_lowercase)
    required = [random.choice(string.ascii_lowercase)]
    if use_upper:
        pool += list(string.ascii_uppercase)
        required.append(random.choice(string.ascii_uppercase))
    if use_digit:
        pool += list(string.digits)
        required.append(random.choice(string.digits))
    if use_symbol:
        pool += list("!@#$%^&*")
        required.append(random.choice("!@#$%^&*"))
    # 剩余位数从全池子随机补齐，再打乱
    rest = [random.choice(pool) for _ in range(length - len(required))]
    chars = required + rest
    random.shuffle(chars)
    return "".join(chars)


def strength(pwd: str) -> str:
    """根据长度和字符种类打分。"""
    kinds = sum([
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in "!@#$%^&*" for c in pwd),
    ])
    score = len(pwd) + kinds * 4
    if score >= 24:
        return "强"
    elif score >= 16:
        return "中"
    return "弱"


def main() -> None:
    random.seed(42)  # 固定随机种子，让每次输出可复现
    configs = [
        {"length": 8},
        {"length": 12},
        {"length": 16, "use_symbol": False},
    ]
    for cfg in configs:
        pwd = generate(**cfg)
        print(f"  {pwd:<20} 强度：{strength(pwd)}")

    # 边界
    try:
        generate(3)
    except ValueError as e:
        print(f"\n边界测试：{e}")


if __name__ == "__main__":
    main()
