#!/usr/bin/env python

# Subsystem classes
class SubsystemA:
    def operation_a(self):
        return "Subsystem A operation"


class SubsystemB:
    def operation_b(self):
        return "Subsystem B operation"


class SubsystemC:
    def operation_c(self):
        return "Subsystem C operation"


# Facade is operation agregation
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def perform_subsystems_operations(self):
        result = []
        result.append(self.subsystem_a.operation_a())
        result.append(self.subsystem_b.operation_b())
        result.append(self.subsystem_c.operation_c())
        return "\n".join(result)


def facade():
    facade = Facade()
    result = facade.perform_subsystems_operations()
    print(result)
    # Subsystem A operation
    # Subsystem B operation
    # Subsystem C operation


facade()
