"""第 28 天：单元测试示例

掌握：unittest、断言、测试驱动。
把被测函数和测试放一起，演示多个用例和断言。
"""
from __future__ import annotations

import unittest


# ===== 被测代码 =====
def is_palindrome(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


def fizzbuzz(n: int) -> str:
    if n <= 0:
        raise ValueError("必须为正整数")
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# ===== 测试代码 =====
class TestPalindrome(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_palindrome("level"))

    def test_phrase(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_negative(self):
        self.assertFalse(is_palindrome("python"))


class TestFizzBuzz(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            fizzbuzz(0)


def main() -> None:
    suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"\n成功：{result.wasSuccessful()}，"
          f"用例数：{result.testsRun}")


if __name__ == "__main__":
    main()
