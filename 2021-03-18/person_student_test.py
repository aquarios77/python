from student import Student
from person import Person

person = Person("Laima", 23)
print(f'person: {person}')
print(f"person's name: {person.get_name()}")
print(f"person's age: {person.get_age()}")
print()
student = Student("Misha", 22, "102")
print(f'student: {student}')
print(f"student's name: {student.get_name()}")
print(f"student's age: {student.get_age()}")

Person.print_info(student)