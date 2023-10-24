
import random 
def game(comp, you):
    if comp==you:
        return print("tis draw")
    elif comp=='r':
        if you == 'p':
            return print("u win")
        elif you=='s':
            return print("U lose")
        elif you!='r' and you!='p' and you!='s':
            return print("invalid, nerd")    
    elif comp=='p':
        if you == 'r':
            return print("u lose")
        elif you=='s':
            return print("U win")
        elif you!='r' and you!='p' and you!='s':
            return print("invalid, nerd")    
    elif comp=='s':
        if you == 'p':
            return print("u lose")
        elif you=='r':
            return print("U win")
        elif you!='r' and you!='p' and you!='s':
            return print("invalid, nerd")


print("Comp chose, rock paper scissors")
rng = random.randint(1,3)
if rng == 1:
    comp = 'r'
elif rng == 2:
    comp = 'p'
elif rng == 3:
    comp = 's'

you = input("U choose: rock paper or scissors??\n")
print(f"comp chose {comp}")       #push up two line lmaoooooooo
game(comp, you)

