with open('pems.txt','r') as f:
    data = f.read()

with open("pemscopy.txt",'r') as f:
    newdata = f.read()

if data == newdata:
    print("tis same")
else:
    print("tis diff")
