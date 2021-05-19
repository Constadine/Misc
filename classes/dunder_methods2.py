from random import randrange, seed
from datetime import datetime


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1

    def __lt__(self, other):
        return self.grade < other.grade

    def __str__(self) -> str:
        return f"{self.full_name}({self.grade})"


def grade_student(student):
    student.grade = randrange(0, 11)


def average(l):
    s = 0
    for student in students:
        s += student.grade

    print("Average: " + str(s//len(students)))


names = ["Antonia Archer",
         "Kaira Zavala",
         "Paddy Spencer",
         "Jaiden Bate",
         "Taylor Guzman",
         "Alfie Betts",
         "Conner Wade",
         "Judy Sexton",
         "Warwick Cooper",
         "Abbi Reese"]

students = [Student(names[i]) for i in range(len(names))]

for student in students:
    grade_student(student)

average(students)

students.sort(reverse=True)

for student in students:
    print(student)
