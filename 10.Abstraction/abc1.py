from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyre = n
    @abstractmethod
    def start(self):
        pass
    def display(self):
        print("I am abstarct Class")