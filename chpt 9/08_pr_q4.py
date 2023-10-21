
with open('textfpodonk.txt', 'r') as f:
    data = f.read()

if 'donk' in data:
    newdata=data.replace('donk', 'bonk')
    print(newdata)
else:
    print("no donks")

with open("textfpodonk.txt", 'w') as f:
    f.write(newdata)
    