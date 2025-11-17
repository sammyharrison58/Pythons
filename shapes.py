class shape:
    def __init__(
        self,
        color,
        filled,
    ):
        self.color = color
        self.filled = filled

    def describe(self):
        return (
            f"A {self.color} shape that is {'filled' if self.filled else 'not filled'}."
        )


class circle(
    shape,
):
    def __init__(self, color, filled, radius):
        super().__init__(
            color,
            filled,
        )
        self.rdius = radius

    def area(self):
        return 3.14 * self.rdius * self.rdius


class square(
    shape,
):
    def __init__(self, color, filled, side):
        super().__init__(
            color,
            filled,
        )
        self.side = side

    def area(self):
        return self.side * self.side


class triangle(
    shape,
):
    def __init__(self, color, filled, base, height):
        super().__init__(
            color,
            filled,
        )
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle1 = circle("red", True, 5)

print(f"Circle area: {circle1.area()}")
square1 = square("blue", False, 4)
print(f"Square area: {square1.area()}")
triangle1 = triangle("green", True, 3, 6)
print(f"Triangle area: {triangle1.area()}")
