class School:
    def __init__(self, school_name, school_type, num_teachers, num_students):
        self.school_name = school_name
        self.school_type = school_type
        self.num_teachers = num_teachers
        self.num_students = num_students
        self.students = []

    def register_student(self):
        student_name = input("Enter student name: ")
        student_age = input("Enter student age: ")
        student_address = input("Enter student address: ")

        new_student = {
            "name": student_name,
            "age": student_age,
            "address": student_address
        }

        self.students.append(new_student)
        print(f"Student {student_name} registered successfully.")

    def change_principal(self, new_principal):
        self.principal = new_principal
        print(f"Principal changed to {new_principal}.")

    def add_teacher(self, teacher_name):
        self.num_teachers += 1
        print(f"Teacher {teacher_name} added successfully")


school_name = input("Enter school name: ")
school_type = input("Enter school type: ")
num_teachers = int(input("Enter number of teachers: "))
num_students = int(input("Enter number of students: "))

school = School(school_name, school_type, num_teachers, num_students)

school.register_student()

new_principal = input("Enter the new principal's name: ")
school.change_principal(new_principal)

teacher_name = input("Enter teacher's name to add: ")
school.add_teacher(teacher_name)