#!/usr/bin/env python

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        raise StopIteration


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_iterator(self):
        return Iterator(self.items)


def iterator_example():
    collection = Collection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    iterator = collection.get_iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)


iterator_example()
