class Instructor:
    def __init__(self,name,address,subject,exp):
        self.name = name
        self.address = address
        self.subject = subject
        self.exp = exp
    def show_inst_info(self):
        print("Name Of Instructor :",self.name)
        print("Address :",self.address)
        print("Subject :",self.subject)
        print("Experience :",self.exp)

i1 = Instructor("Krishna","A/P Divad,Tal-Man,Dist-Satara","JAVA",2)
i1.show_inst_info()