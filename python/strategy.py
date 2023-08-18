#!/usr/bin/env python

from abc import ABC, abstractmethod


# Strategy interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


# Concrete strategies
class BubbleSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort:", data)


class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort:", data)


class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using Merge Sort:", data)


# Context
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def perform_sort(self, data):
        self.strategy.sort(data)


# Client code
data = [5, 2, 8, 1, 3]
sorter = Sorter(BubbleSort())
sorter.perform_sort(data)

# picking right strategy
sorter.set_strategy(QuickSort())
sorter.perform_sort(data)
