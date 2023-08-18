#!/usr/bin/env python

class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name, 0)


class Expression:
    def interpret(self, context):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class Minus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


def interpreter():
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 5)
    # reverse polish notation
    # + x - 15 y
    # operation
    # x + (15 - y) = 20
    expression = Plus(
        Number(context.get_variable("x")),
        Minus(Number(15), Number(context.get_variable("y")))
    )

    result = expression.interpret(context)
    print("Result:", result)  # Output: Result: 20


interpreter()
