import unittest
from src.zbiory import Zbiory


class TestZbiory(unittest.TestCase):

    def test_is_list_not_none(self):
        zbior = Zbiory([1, 2, 3, 4, 5], 1)
        self.assertGreater(len(zbior.list_), 0)

    def test_is_list_none(self):
        zbior = Zbiory(None, 1)
        self.assertEqual(len(zbior.list_), 0)

    def test_repeated_elements(self):
        zbior = Zbiory([1, 1, 2, 2, 2, 3, 4, 4, 4, 5], 2)
        self.assertEqual(zbior.list_checkers(), [1])

    def test_repeated_elements_none(self):
        zbior = Zbiory(None, 2)
        self.assertEqual(zbior.list_checkers(), [])

    def test_no_repeated_elements(self):
        zbior = Zbiory([1, 2, 3, 4, 5], 2)
        self.assertEqual(zbior.list_checkers(), [])


if __name__ == '__main__':
    unittest.main()
