f = open('pems.txt', 'r')
data = str(f.read())
print(data)

if 'twinkle' in data:
    print("ye")
else:
    print("nay")
    
f.close()
