"""第 08 天：密码建议器"""

def main() -> None:
    import random
    import string
    random.seed(30)
    chars = string.ascii_letters + string.digits
    password = "".join(random.choice(chars) for _ in range(10))
    print("建议密码:", password)

if __name__ == "__main__":
    main()
