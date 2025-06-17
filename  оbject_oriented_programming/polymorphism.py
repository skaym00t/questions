import math

class Shape:
    """Не понимаю зачем по ТЗ, кажется лучше создать интерфейс"""

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0

class Rectangle(Shape):
    """Прямоугольник"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Периметр прямоугольника"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Круг"""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Площадь круга"""

        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Периметр круга"""

        return 2 * math.pi * self.radius

s = Shape()
r = Rectangle(10,20)
c = Circle(13)

shapes = [s, r, c]

for shape in shapes:
    print(f'фигура: {shape.__class__.__name__}, {shape.__dict__}, площадь: {shape.area():.2f}, периметр: {shape.perimeter():.2f}')
