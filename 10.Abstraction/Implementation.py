from abc1 import Vehicle
from abc import ABC,abstractmethod
# class Bike(ABC):
#     def __init__(self,n,color):
#         self.no_of_tyre = n
#         self.color = color
#     @abstractmethod
#     def start(self):
#         # print("Start By USing Kick")
#         pass

class Bike(Vehicle):
    def __init__(self,n,color):
        self.no_of_tyre = n
        self.color = color
    def start(self):
        print("Start By USing Kick")

class Car(Vehicle):
    def __init__(self,n,color):
        self.no_of_tyre = n
        self.color = color
    def start(self):
        print("Start By Using Button")
    def display(self):
        print("I am car")