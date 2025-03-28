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

    def test_is_rotation_angle_Not_None(self):
        tester = MoonRover(2, 1)
        tester.rotate(90)
        self.assertEqual(tester.angle, 90)

    def test_is_drive_forward_value_None(self):
        tester = MoonRover(0,0)
        self.assertIsNone(tester.driveForward(None), None)

    def test_is_drive_forward_value_Not_None(self):
        tester = MoonRover(0,0)
        tester.driveForward(1)
        self.assertEqual(tester.Y, 1)

    def test_is_drive_forward_value_Not_None_Rotated_Right(self):
        tester = MoonRover(0,0)
        tester.rotate(90)
        tester.driveForward(1)
        self.assertEqual(tester.X, 1)

    def test_is_drive_forward_value_Not_None_Rotated_Right_on_minus(self):
        tester = MoonRover(0,0)
        tester.rotate(-270)
        tester.driveForward(1)
        self.assertEqual(tester.X, 1)

    def test_is_drive_forward_value_Not_None_Rotated_to_back(self):
        tester = MoonRover(0,0)
        tester.rotate(180)
        tester.driveForward(1)
        self.assertEqual(tester.Y, -1)

    def test_is_drive_forward_value_Not_None_Rotated_to_back_on_minus(self):
        tester = MoonRover(0,0)
        tester.rotate(-180)
        tester.driveForward(1)
        self.assertEqual(tester.Y, -1)

    def test_is_drive_forward_value_Not_None_Rotated_Left(self):
        tester = MoonRover(0,0)
        tester.rotate(270)
        tester.driveForward(1)
        self.assertEqual(tester.X, -1)

    def test_is_drive_forward_value_Not_None_Rotated_Left_on_minus(self):
        tester = MoonRover(0,0)
        tester.rotate(-90)
        tester.driveForward(1)
        self.assertEqual(tester.X, -1)

    def test_is_drive_backward_value_None(self):
        tester = MoonRover(0, 0)
        self.assertIsNone(tester.driveBackward(None), None)

    def test_is_drive_backward_value_Not_None(self):
        tester = MoonRover(0, 0)
        tester.driveBackward(1)
        self.assertEqual(tester.Y, -1)

    def test_is_drive_backward_value_Not_None_Rotated(self):
        tester = MoonRover(0, 0)
        tester.rotate(90)
        tester.driveBackward(1)
        self.assertEqual(tester.X, -1)



if __name__ == '__main__':
    unittest.main()