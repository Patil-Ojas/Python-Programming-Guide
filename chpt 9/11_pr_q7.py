
data = True
i = 1
with open("logfiles.txt") as f:
    while data:
        data = f.readline()
        if "python" in data.lower():
            print(f"ye tis there at {i}")
            print(data)
        i = i+1 