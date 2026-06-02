from pytest import mark

from app.area import Circle, Rectangle, Square, Triangle


@mark.parametrize(
    "shape, expected_area",
    [
        (Square(10), 100),
        (Rectangle(6, 7), 42),
        (Triangle(7, 4), 14),
        (Circle(10), 314.16),
    ],
)
def test_calculation_area(shape, expected_area):
    area = shape.calculation_area()
    assert area == expected_area, "FAILED: incorrect area result!"
    print("PASSED: area is correct!")
