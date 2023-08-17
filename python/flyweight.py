#!/usr/bin/env python

class Character:
    def __init__(self, symbol, size, color):
        self.symbol = symbol
        self.size = size
        self.color = color

    def display(self):
        return f"Character: {self.symbol}, Size: {self.size}, Color: {self.color}"


class CharacterFactory:
    characters = {}

    @staticmethod
    def get_character(symbol, size, color):
        if symbol not in CharacterFactory.characters:
            CharacterFactory.characters[symbol] = Character(symbol, size, color)
        return CharacterFactory.characters[symbol]


def flyweight_example():
    factory = CharacterFactory()

    char1 = factory.get_character('A', 12, 'red')
    char2 = factory.get_character('B', 14, 'blue')
    char3 = factory.get_character('A', 12, 'red')  # Reusing existing 'A' character

    print(char1.display())  # Output: Character: A, Size: 12, Color: red
    print(char2.display())  # Output: Character: B, Size: 14, Color: blue
    print(char3.display())  # Output: Character: A, Size: 12, Color: red (Reused)


flyweight_example()

