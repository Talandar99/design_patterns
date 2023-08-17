#!/usr/bin/env python

from abc import ABC, abstractmethod


# Component interface
class Component(ABC):
    @abstractmethod
    def calculate_price(self):
        pass


# Leaf class representing a Product
class Product(Component):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price


# Composite class representing a Box
class Box(Component):
    def __init__(self, name, price):
        self.name = name
        self.items = []
        self.price = price

    def add(self, item):
        self.items.append(item)

    def calculate_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.calculate_price()
        return total_price + self.price


def composite():
    apple = Product("Apple", 1)
    banana = Product("Banana", 2)
    orange = Product("Orange", 3)

    fruit_box = Box("Fruit Box", 2)
    fruit_box.add(apple)
    fruit_box.add(banana)
    fruit_box.add(orange)

    small_box = Box("Small Box", 2)
    small_box.add(fruit_box)

    print(apple.calculate_price())  # Output: 1
    print(fruit_box.calculate_price())  # Output: 8 (1 + 2 + 3 + 2)
    print(small_box.calculate_price())  # Output: 10 (8 + 2)


composite()
