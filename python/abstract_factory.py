#!/usr/bin/env python

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Draw a circle!")


class Rectangle(Shape):
    def draw(self):
        print("Draw a rectangle!")


class Triangle(Shape):
    def draw(self):
        print("Draw a triangle!")


class ComplexCircle(Shape):
    def draw(self):
        print("Draw a complex circle!")


class ComplexRectangle(Shape):
    def draw(self):
        print("Draw a complex rectangle!")


class ComplexTriangle(Shape):
    def draw(self):
        print("Draw a complex triangle!")


class ShapeFactory(ABC):
    @abstractmethod
    def create_circle(self) -> Shape:
        pass

    @abstractmethod
    def create_rectangle(self) -> Shape:
        pass

    @abstractmethod
    def create_triangle(self) -> Shape:
        pass


class SimpleShapeFactory(ShapeFactory):
    def create_circle(self) -> Shape:
        return Circle()

    def create_rectangle(self) -> Shape:
        return Rectangle()

    def create_triangle(self) -> Shape:
        return Triangle()


class ComplexShapeFactory(ShapeFactory):
    def create_circle(self) -> Shape:
        return ComplexCircle()

    def create_rectangle(self) -> Shape:
        return ComplexRectangle()

    def create_triangle(self) -> Shape:
        return ComplexTriangle()


def abstract_factory_main():
    shapes: list = []
    simple_factory = SimpleShapeFactory()
    complex_factory = ComplexShapeFactory()
    shapes.append(simple_factory.create_circle())
    shapes.append(complex_factory.create_circle())
    shapes.append(simple_factory.create_rectangle())
    shapes.append(complex_factory.create_rectangle())
    shapes.append(simple_factory.create_triangle())
    shapes.append(complex_factory.create_triangle())

    for shape in shapes:
        shape.draw()


abstract_factory_main()
