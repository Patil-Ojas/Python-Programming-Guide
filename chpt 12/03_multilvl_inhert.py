

class Person:
    country = "India"
    def __init__(self):
        print("Initializing person...")

    def takeBreak(self):
        print("I am underthewater")

class employee(Person):
    company = "honda"

    def __init__(self):
        super().__init__()
        print("Initializing employee...")

    def getSal(self):
        print("Salary is ", self.salary)

    def takeBreak(self):
        super().takeBreak()
        print("I am emp luck waterunder")
    
class programmer(employee):
    company = "Fiverr"

    def __init__(self):
        super.__init__()
        print("Initializing programmer...")

    def getsal(self):
        print("No salary for programmers")

    def takeBreak(self):
        # "mere uppar wale ka run kr"
        super().takeBreak()
        print("I am emp luck waterunder")

# uses latest if not defined
p = Person()
p.takeBreak()

e = employee
e.takeBreak

pr = programmer()
pr.takeBreak()      

# super + constuructor = if we call only programmer both person and employee constuctors automatically get called

