
import os

with open("yeet.txt") as f:
    data = f.read()

with open("renamed_yes_deff.txt", 'w') as f:
    f.write(data)

os.remove("yeet.txt")
