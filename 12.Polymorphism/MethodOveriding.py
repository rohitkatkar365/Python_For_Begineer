class A:
    def a(self):
        print("a")

class B(A):
    def a(self):
        print(("a.1"))


b1 = B()
b1.a()
