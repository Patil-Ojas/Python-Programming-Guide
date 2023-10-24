
# basically things to use if u are using a custom variable cuz i dunno why u gonna be using that 

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets multiple")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 619
    
n1 = Number(4)
n2 = Number(6)
# wont work without __add__
sum = n1 + n2
print(sum)

prod = n1*n2
print(prod)

n = Number(9)
print(n)
print(len(n))