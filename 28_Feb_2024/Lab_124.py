# Inheritance = Abstraction
from abc import ABC, abstractmethod


class ATB(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_task1(self):
        pass

    # once declared abstract method, then need to complete the whole method  it in inherited class.
    def perform_task2(self):
        pass


class A(ATB):
    def perform_task1(self):
        print("task 1 is performed")


a = A("rahul")
a.perform_task1()
