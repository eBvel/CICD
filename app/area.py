from math import pi


class Shape:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculation_area(self) -> float:
        return self.a * self.b


class Square(Shape):
    def __init__(self, a: float):
        super().__init__(a, a)


class Rectangle(Shape):
    pass


class Triangle(Shape):
    def __init__(self, a: float, h: float):
        super().__init__(a, h)

    def calculation_area(self) -> float:
        result = super().calculation_area()
        return result / 2


class Circle(Shape):
    def __init__(self, r: float):
        super().__init__(r, r)

    def calculation_area(self) -> float:
        result = super().calculation_area()
        return round(pi * result, 2)
