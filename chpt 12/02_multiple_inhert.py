
class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    lvl = 2

    def upgradelevel(self):
        self.lvl += 1

# this order defines priority
class Programmer(Employee, Freelancer):
    name = "Rohit"


prg = Programmer()
print(prg.lvl)
prg.upgradelevel()
print(prg.lvl)

