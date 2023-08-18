#!/usr/bin/env python

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def accept(self, visitor):
        visitor.visit_square(self)


class AreaCalculator:
    def visit_circle(self, circle):
        print(f"Calculating area of circle with radius {circle.radius}")

    def visit_square(self, square):
        print(f"Calculating area of square with side length {square.side_length}")


class PerimeterCalculator:
    def visit_circle(self, circle):
        print(f"Calculating perimeter of circle with radius {circle.radius}")

    def visit_square(self, square):
        print(f"Calculating perimeter of square with side length {square.side_length}")


def visitor():
    circle = Circle(5)
    square = Square(4)

    area_calculator = AreaCalculator()
    perimeter_calculator = PerimeterCalculator()

    circle.accept(area_calculator)
    circle.accept(perimeter_calculator)

    square.accept(area_calculator)
    square.accept(perimeter_calculator)


visitor()
