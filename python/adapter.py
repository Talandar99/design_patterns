#!/usr/bin/env python

class OldSystem:
    def deprecated_way_to_perform_action(self):
        return "Old System's action"


class NewSystem:
    def perform_action(self):
        return "New System's action"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def perform_action(self):
        return f"Adapter's action: {self.old_system.deprecated_way_to_perform_action()}"


def adapter():
    new_system = NewSystem()
    old_system = OldSystem()
    adapter = Adapter(old_system)

    print("Client receives output from Old System:\n", adapter.perform_action())
    print()
    print("Client receives output from New System:\n", new_system.perform_action())


adapter()
