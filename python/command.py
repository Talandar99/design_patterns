#!/usr/bin/env python

from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver class
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


def command():
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    commands: list = []
    commands.append(light_on)
    commands.append(light_off)
    commands.append(light_on)
    commands.append(light_off)
    commands.append(light_off)
    commands.append(light_off)
    # invoker
    for command in commands:
        command.execute()


command()
