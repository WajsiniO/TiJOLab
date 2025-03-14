from students import students

def main():
    student = students()
    student.add_student("Aleksander Wajs")
    print(student.students_signed())

if __name__ == '__main__':
    main()