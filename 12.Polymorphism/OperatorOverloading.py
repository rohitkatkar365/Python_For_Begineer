# Operator overloading is a feature in programming languages that allows you to redefine the behavior of
# operators (like +, -, *, etc.) for user-defined types (like classes).
# This enables you to use these operators in a way that is natural and intuitive for the types you define.

class ComplexNumber:
    def __init__(self,real,imajinary):
        self.real = real
        self.imajinary = imajinary

    def __add__(self, other):
        return f"{self.real+other.real} + {self.imajinary+other.imajinary}i"

c1 = ComplexNumber(1,2)
c2 = ComplexNumber(2,3)
print(c1+c2)
