class student:
    Total_gpa = 0
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.Total_gpa += gpa
        student.count += 1

    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total of student: {cls.count}"


student1 = student("David", 3.5)
student2 = student("Eva", 3.8)


@classmethod
def average_gpa(cls):
    if cls.count == 0:
        return 0
    else:
        print(f"{cls.Total_gpa} / {cls.count}")


print(student1.get_count())
