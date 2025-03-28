import unittest
from src.MoonRover import MoonRover

class testMoonRover(unittest.TestCase):
    def test_is_X_None(self):
        tester = MoonRover(None, 2)
        self.assertIsNone(tester.X)

    def test_is_X_NotNone(self):
        tester = MoonRover(1, 2)
        self.assertIsNotNone(tester.X)

    def test_is_Y_None(self):
        tester = MoonRover(2, None)
        self.assertIsNone(tester.Y)

    def test_is_Y_NotNone(self):
        tester = MoonRover(2, 1)
        self.assertIsNotNone(tester.Y)

    def test_is_rotation_angle_None(self):
        tester = MoonRover(2, 1)
        self.assertIsNone(tester.rotate(None))

if __name__ == '__main__':
    unittest.main()