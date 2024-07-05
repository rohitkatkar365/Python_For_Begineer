class A:
    def __init__(self,name):
        print("I am A Class Constructor")
        self.name = name

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")

class B(A):
    def __init__(self,name):
        super().__init__(name)
        print("I am B class Constructor")

    def f1(self):
        super().f1()
        print("f1.2")

    def f2(self):
        print("f2.2")

    def f3(self):
        print("f3")

class C(B):
    def f1(self):
        super().f1()
        print("f1.3")

    def f4(self):
        print("f4")

# obj1 = A()
obj2 = B("Ram")
# obj3 = C()

# print(obj2.f1())
print(obj2.name)