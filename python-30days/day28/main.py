"""第 28 天：单元测试示例"""

def main() -> None:
    import unittest

    def add(left, right):
        return left + right

    class AddTest(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)

    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(AddTest))
    print("测试通过:", result.wasSuccessful())

if __name__ == "__main__":
    main()
