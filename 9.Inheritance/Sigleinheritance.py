class Vehicle:
    def __init__(self):
        self.type = "Top"

    def color(self,color):
        self.color = color

    def work(self):
        print("I Can Work")
class Creta(Vehicle):
    def __init__(self,name):
        super().__init__()
        self.name = name
        print("I am Creta")
    def model(self):
        print("Top Model")
    def work(self):
        super().work()
        print("I Can Code")

o1 = Creta()

# o1.model()
# o1.color("White")

# print(o1.color)

# o1.work()
# print(o1.name)
print(o1.type)