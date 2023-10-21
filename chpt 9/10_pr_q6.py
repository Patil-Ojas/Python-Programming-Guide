
with open('logfiles.txt') as f:
    data = f.read()

if "python" in data.lower():              #case sensitive, use lower()
    print("yee")
else:
    print("nayyy")
