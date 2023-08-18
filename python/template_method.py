#!/usr/bin/env python

from abc import ABC, abstractmethod


# Abstract Class - Template Method
class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")


# Concrete Classes
class Coffee(Beverage):
    def brew(self):
        print("Brewing coffee")

    def add_condiments(self):
        print("Adding sugar and milk")


class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")


def template_method():
    coffee = Coffee()
    tea = Tea()

    print("Preparing coffee:")
    coffee.prepare()

    print("\nPreparing tea:")
    tea.prepare()


template_method()
