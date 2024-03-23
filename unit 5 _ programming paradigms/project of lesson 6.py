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
        print(f"Teacher {teacher_name} added successfully.")

class HighSchool(School):
    def __init__(self, school_name, num_teachers, num_students, sports_team):
        super().__init__(school_name, school_type="High School", num_teachers=num_teachers, num_students=num_students)
        self.sports_team = sports_team

    def organize_pe_class(self):
        print(f"PE class organized for {self.school_name}.")


school_name = input("Enter school name: ")
num_teachers = int(input("Enter number of teachers: "))
num_students = int(input("Enter number of students: "))
sports_team = input("Enter sports team name: ")

high_school = HighSchool(school_name, num_teachers, num_students, sports_team)

high_school.register_student()

new_principal = input("Enter the new principal's name: ")
high_school.change_principal(new_principal)

teacher_name = input("Enter teacher's name to add: ")
high_school.add_teacher(teacher_name)

high_school.organize_pe_class()