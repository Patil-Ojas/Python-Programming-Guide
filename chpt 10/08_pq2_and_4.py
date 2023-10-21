
class calculator:
    def __init__(self, number):
        self.number = number

    def sqr(self):
        print(self.number*self.number)

    def cr(self):
        print(self.number**3)
    
    def sqrt(self):
        print(self.number**0.5)

    @staticmethod
    def greed():
        print("I summon pizza")

brug = calculator(int(input()))
brug.sqr()
brug.cr()
brug.sqrt()
brug.greed()
