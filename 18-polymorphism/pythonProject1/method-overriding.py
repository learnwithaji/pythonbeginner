class Shape:
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

def print_perimeter(shape):
    print(f"The perimeter is: {shape.perimeter()}")

circle = Circle(5)
rectangle = Rectangle(3, 6)
triangle = Triangle(3, 4, 5)

print_perimeter(circle)
print_perimeter(rectangle)
print_perimeter(triangle)
