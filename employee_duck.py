class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}."

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions


emp1 = employee("John Brandews", "Developer")
emp2 = employee("Father looks", "Manager")
print(emp1.get_info())
print(employee.is_valid_position("CEO"))
