class StudentManagement:
    """
    Klasa zarządzająca studentami i ich ocenami.
    """

    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, id: str, name: str, age: int) -> bool:
        if id in self.students:
            return False
        self.students[id] = {'name': name, 'age': age}
        self.grades[id] = {}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        if id not in self.students:
            return False
        self.students[id] = {'name': name, 'age': age}
        return True

    def remove_student(self, id: str) -> bool:
        if id not in self.students:
            return False
        del self.students[id]
        del self.grades[id]
        return True

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        valid_grades = {2.0, 3.0, 3.5, 4.0, 4.5, 5.0}
        if student_id not in self.students or grade not in valid_grades:
            return False

        if subject not in self.grades[student_id]:
            self.grades[student_id][subject] = []
        self.grades[student_id][subject].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        total = 0
        count = 0
        for student in self.grades.values():
            if subject in student:
                total += sum(student[subject])
                count += len(student[subject])
        return round(total / count, 2) if count > 0 else 0.0
