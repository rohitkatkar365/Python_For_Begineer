class Student:
    name = "null"
    __age = 0
    cname = "null"
    def set(self,name,__age,cname):
        self.name = name
        self.__age = __age
        self.cname = cname
    def get(self):
        print(f"{self.name+" "}{self.__age}' '{self.cname}")

s1 = Student()
s1.set("Ram",22,"Shivaji College")
s1.get()