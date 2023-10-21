
with open("pems.txt", 'r') as f:
    data = f.read()

with open("pemscopy.txt", 'w') as f:
    f.write(data)
