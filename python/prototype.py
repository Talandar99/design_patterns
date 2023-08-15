#!/usr/bin/env python

import copy


class Prototype:
    def clone(self):
        pass


class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


def prototype():
    prototype = ConcretePrototype(42)
    clone1 = prototype.clone()
    clone2 = prototype.clone()

    print("prototype.value")
    print(prototype.value)
    print("clone1.value")
    print(clone1.value)
    print("clone2.value")
    print(clone2.value)

    print("clone1.value = 100")
    clone1.value = 100
    print("prototype.value")
    print(prototype.value)
    print("clone1.value")
    print(clone1.value)
    print("clone2.value")
    print(clone2.value)


prototype()
