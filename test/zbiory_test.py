import unittest
from src.zbiory import zbiory

class TestZbiory(unittest.TestCase):
    def isListNotNone(self, lista):
        self.assertGreater(len(lista), 0)
        