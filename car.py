class car:
    def __init__(self, model, year, color, sale):
        self.model = model
        self.year = year
        self.color = color
        self.sale = sale

    def drive(self):
        print(f"you drive a{self.model} {self.year} {self.color} car")

    def stop(self):
        print("you stop the car")


car1 = car("toyota", 2020, "red", True)
car1.drive()
