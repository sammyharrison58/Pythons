class students:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        students.num_students += 1


student1 = students("Alice", 20)
student2 = students("Bob", 21)
student3 = students("Charlie", 19)
print(student1.name)
print(f"my grade of {students.class_year} has {students.num_students} students")
