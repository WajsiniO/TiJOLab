import unittest
from src.Calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print("** test_add()")
        result = self.calc.add(3, 2)
        self.assertEqual(result, 5)

    def test_subtract(self):
        print("** test_subtract()")
        result = self.calc.subtract(3, 2)
        self.assertEqual(result, 1)

    def test_multiply(self):
        print("** test_subtract()")
        result = self.calc.multiply(3, 2)
        self.assertEqual(result, 6)

    def test_divide_by_zero(self):
        print("** test_divide_by_zero()")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        print("*** tearDown()")
        self.calc = None

if __name__ == '__main__':
    unittest.main()