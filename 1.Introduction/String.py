# String is a collection of character
fname = "Rohit"
lname = "Katkar"

print(fname[0:2])
print(fname[-1::-1])
print(fname +" "+ lname)
print(fname.find("i",0, len(fname)))
print("_".join(fname))
print(fname.count("k",0,len(fname)))
print(lname.index("a",0,len(fname)))
print(fname.capitalize())
print(fname.casefold())
print(fname.endswith("t"))
print(fname.isascii())
print(lname.isupper())
print(lname.lower())
print(lname.partition("-"))
print(fname.replace("Rohit","Tohit",1))
print(fname.swapcase())