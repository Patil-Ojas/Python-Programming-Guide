
# why is it autospacef for the love of god
# procedural oriented programming

a = 12
b = 14
print("sum is ", a+b)

# to implement the same using oop

# classes is a blueprint, it doesnt require memory, memeory is allocated only after obj instantiation
# PascalCase used

class Number:
    def sum(self):
        return self.a + self.b
    
num = Number()
num.a = 12
num.b = 14
s = num.sum()
print(s)

# railway

class railwayss:
    formType = "RailwayForm"
    def printData(self):
        print("Name is ", self.name)
        print("Train is ", self.train)

appplc = railwayss()
appplc.name = "jin mori"
appplc.train = "rajdhani express"
appplc.printData()