words = ["bro","yes","back"]

with open('eee5.txt', 'r') as f:
    data = f.read()

for wor in words:
    data = data.replace(wor, "qqqqq")
    with open('eee5.txt','w') as f:
        f.write(data) 
