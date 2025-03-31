class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

# Create a list of students
students = [
    Student("Tom", 12),
    Student("Alice", 13),
    Student("Bob", 14)
]

for student in students:
    student.eat()
