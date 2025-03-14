import unittest
from src.students import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.sm = StudentManagement()
        self.sm.add_student("1", "Jan Kowalski", 22)
        self.sm.add_grade("1", "Matematyka", 5.0)
        self.sm.add_grade("1", "Matematyka", 4.0)

    def test_add_student_success(self):
        result = self.sm.add_student("2", "Anna Nowak", 21)
        self.assertTrue(result)
        self.assertIn("2", self.sm.students)

    def test_add_duplicate_student(self):
        result = self.sm.add_student("1", "Jan Kowalski", 22)
        self.assertFalse(result)

    def test_update_student_success(self):
        result = self.sm.update_student("1", "Jan Nowak", 23)
        self.assertTrue(result)
        self.assertEqual(self.sm.students["1"]["name"], "Jan Nowak")

    def test_update_nonexistent_student(self):
        result = self.sm.update_student("999", "Test", 99)
        self.assertFalse(result)

    def test_remove_student_success(self):
        result = self.sm.remove_student("1")
        self.assertTrue(result)
        self.assertNotIn("1", self.sm.students)

    def test_remove_nonexistent_student(self):
        result = self.sm.remove_student("999")
        self.assertFalse(result)

    def test_add_valid_grade(self):
        result = self.sm.add_grade("1", "Fizyka", 4.5)
        self.assertTrue(result)
        self.assertIn(4.5, self.sm.grades["1"]["Fizyka"])

    def test_add_invalid_grade(self):
        result = self.sm.add_grade("1", "Matematyka", 1.5)
        self.assertFalse(result)

    def test_avg_grades_calculation(self):
        avg = self.sm.avg_grades("Matematyka")
        self.assertEqual(avg, 4.5)

    def test_avg_grades_no_data(self):
        avg = self.sm.avg_grades("Chemia")
        self.assertEqual(avg, 0.0)

    def tearDown(self):
        self.sm = None

if __name__ == '__main__':
    unittest.main()
