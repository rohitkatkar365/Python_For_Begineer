import pickle
pw = open("Sample.txt","rb")
di = {1:1,2:2}

# pickle.dump(di,pw)

print(pickle.load(pw))
pw.close()