#!/usr/bin/env python

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("draw a rectangle!")


class Circle(Shape):
    def draw(self):
        print("draw a circle!")


class Triangle(Shape):
    def draw(self):
        print("draw a triangle!")


class ShapeFactory:
    def create_circle(self):
        return Circle()

    def create_rectangle(self):
        return Rectangle()

    def create_triangle(self):
        return Triangle()


def factory_main():
    shapes: list = []
    shape_factory = ShapeFactory()
    shapes.append(shape_factory.create_circle())
    shapes.append(shape_factory.create_rectangle())
    shapes.append(shape_factory.create_triangle())

    for shape in shapes:
        shape.draw()


factory_main()

