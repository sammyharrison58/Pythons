from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        area = 0
        return area


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius**2)
        return area


class square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        return area


class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height
        return area


class pizza(circle):
    def __init__(self, radius):
        self.radius = radius


Shapes = [circle(5), square(4), triangle(3, 6), pizza(8)]
for shape in Shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
