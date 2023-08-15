#!/usr/bin/env python

class Ship:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        print("Ship parts:", ", ".join(self.parts))


class Shipyard:
    def __init__(self):
        self.ship = Ship()

    def build_hull(self):
        self.ship.add_part("Ship Hull")
        return self

    def build_engine(self):
        self.ship.add_part("Ship Engine")
        return self

    def build_deck(self):
        self.ship.add_part("Ship Deck")
        return self

    def finish_construction(self):
        finished_ship = self.ship
        self.ship = Ship()
        return finished_ship


def builder():
    shipyard = Shipyard()
    ship = shipyard.build_deck().build_engine().build_hull().finish_construction()
    ship.show()


builder()
