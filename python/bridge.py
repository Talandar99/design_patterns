#!/usr/bin/env python

# Implementor hierarchy
class Color:
    def fill_color(self):
        pass


class RedColor(Color):
    def fill_color(self):
        return "Red"


class BlueColor(Color):
    def fill_color(self):
        return "Blue"


# Abstraction hierarchy
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return f"Drawing a {self.color.fill_color()} circle"


class Square(Shape):
    def draw(self):
        return f"Drawing a {self.color.fill_color()} square"


def bridge():
    red_color = RedColor()
    blue_color = BlueColor()

    red_circle = Circle(red_color)
    blue_square = Square(blue_color)

    print(red_circle.draw())  # Output: "Drawing a Red circle"
    print(blue_square.draw())  # Output: "Drawing a Blue square"


bridge()

