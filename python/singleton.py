#!/usr/bin/env python

class Singleton:
    _instance = None  # Class attribute to hold the instance

    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None:
            # If no instance exists, create one
            cls._instance = super().__new__(cls)
            cls._instance.value = 0  # Set an attribute in the instance
        return cls._instance  # Return the instance


def singleton():
    singleton1 = Singleton()
    singleton2 = Singleton()
    print("singleton1 is singleton2")
    print(singleton1 is singleton2)
    print("singleton1.value")
    print(singleton1.value)
    print("singleton1.value = 2137")
    singleton1.value = 2137
    print("singleton2.value")
    print(singleton2.value)
    print("singleton2.value = 100")
    singleton2.value = 100
    print("singleton1.value")
    print(singleton1.value)
    print("singleton2.value")
    print(singleton2.value)


singleton()
