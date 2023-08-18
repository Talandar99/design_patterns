#!/usr/bin/env python

from abc import ABC, abstractmethod


# State interface
class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_drink(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


# Concrete states
class NoCoinState(State):
    def insert_coin(self):
        print("Coin inserted")
        return CoinInsertedState()

    def select_drink(self):
        print("Insert a coin first")

    def dispense(self):
        print("Insert a coin first")


class CoinInsertedState(State):
    def insert_coin(self):
        print("Coin already inserted")

    def select_drink(self):
        print("Drink selected")
        return DrinkSelectedState()

    def dispense(self):
        print("Select a drink first")


class DrinkSelectedState(State):
    def insert_coin(self):
        print("Coin already inserted")

    def select_drink(self):
        print("Drink already selected")

    def dispense(self):
        print("Drink dispensed")
        return NoCoinState()


class VendingMachine:
    def __init__(self):
        self.state = NoCoinState()

    def insert_coin(self):
        self.state = self.state.insert_coin()

    def select_drink(self):
        self.state = self.state.select_drink()

    def dispense(self):
        self.state = self.state.dispense()


# Client code
def state_example():
    vending_machine = VendingMachine()
    vending_machine.select_drink()  # Output: "Insert a coin first"
    vending_machine.insert_coin()   # Output: "Coin inserted"
    vending_machine.select_drink()  # Output: "Drink selected"
    vending_machine.dispense()      # Output: "Drink dispensed"
    vending_machine.insert_coin()   # Output: "Coin already inserted"
    vending_machine.dispense()      # Output: "Drink dispensed"


state_example()
