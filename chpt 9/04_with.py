#if u r lazy to type f.close(), use tis method

with open('lasample.txt', 'r') as f:
    ee = f.read()
print(ee)

with open('lasample.txt', 'a') as f:
    ee = f.write(" meh")
print(ee)

