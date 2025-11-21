class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

        @property
        def width(self):
            return f"{self._width:.1f}cm"

        @property
        def length(self):
            return f"{self._length:.1f}cm"

        @width.setter
        def width(self, value):
            if value > 0:
                self._width = value
            else:
                print("Width must be positive.")

        @width.deleter
        def width(self):
            print("Deleting width.")
            del self._width

        @length.deleter
        def length(self):
            print("Deleting length.")
            del self._length


rectangle1 = rectangle(5, 10)
rectangle.width = 15
rectangle.length = 20
print(rectangle1.width)
