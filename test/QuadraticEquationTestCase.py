import unittest
from src.QuadraticEquation import QuadraticEquation


class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):

        a, b, c = 0, 2, 4
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_raise_error_when_not_enough_arguments(self):
        a, b = 1, 2
        self.assertRaises(TypeError, QuadraticEquation, a, b)

    def test_solve_with_two_real_roots(self):
        a, b, c = 1, -3, 2
        equation = QuadraticEquation(a, b, c)
        roots = equation.solve()
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 2)
        self.assertAlmostEqual(roots[1], 1)

    def test_solve_with_one_real_root(self):
        a, b, c = 1, -2, 1
        equation = QuadraticEquation(a, b, c)
        roots = equation.solve()
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], 1)

    def test_solve_with_no_real_roots(self):
        a, b, c = 1, 2, 5
        equation = QuadraticEquation(a, b, c)
        roots = equation.solve()
        self.assertIsNone(roots)


    if __name__ == '__main__':
        unittest.main()