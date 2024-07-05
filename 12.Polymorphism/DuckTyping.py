# Duck typing is a concept in programming, particularly in dynamic languages like Python, where the type or
# the class of an object is determined by its behavior (methods and properties) rather than its explicit
# inheritance from a particular class.

# The name "duck typing" comes from the saying:
# "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
class Duck:
    def swim(self):
        print("Duck Can Swim")
    def speak(self):
        print("Duck Can Speak")
class Dog:
    def swim(self):
        print("Dog Can Swim")
    def Speak(self):
        print("Dog Can Speak")

def display(obj):
    obj.swim()
    obj.speak()

d1 = Duck()
display(d1)