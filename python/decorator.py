#!/usr/bin/env python

from abc import ABC, abstractmethod


# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple Coffee"


# Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", Sugar"


# The decorator pattern allows you to dynamically add new behaviors
# (in this case, coffee additions) to objects while maintaining a
# consistent interface.
def decorator():
    simple_coffee = SimpleCoffee()
    milk_coffee = MilkDecorator(simple_coffee)
    sugar_milk_coffee = SugarDecorator(milk_coffee)

    print("Simple Coffee:", simple_coffee.description(), "-",
          simple_coffee.cost())  # Output: Simple Coffee: Simple Coffee - 5
    # Output: Milk Coffee: Simple Coffee, Milk - 7
    print("Milk Coffee:", milk_coffee.description(), "-", milk_coffee.cost())
    # Output: Sugar Milk Coffee: Simple Coffee, Milk, Sugar - 8
    print("Sugar Milk Coffee:", sugar_milk_coffee.description(), "-", sugar_milk_coffee.cost())


decorator()
