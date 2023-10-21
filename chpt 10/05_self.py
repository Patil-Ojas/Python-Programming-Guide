

class employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")
        print("Salary for ", self.company, "is", self.salary)
    
    # harry.getSalary() = employee.getSalary(harry)
    # harry.greet() = employee.greet()
    @staticmethod
    def greet():
        print("Good morning Sir")

    @staticmethod
    def signature(sign):
        print("signature is ", sign)

harry = employee()
harry.salary = 1000
harry.getSalary()

# however if we remove self we get error as follows:
# takes 0 positional arg but 1 was given, this is cuz the above line can also be written in the format (equivalent statements)

employee.getSalary(harry)

# with the help of self we can use both class and object attributes just by writing self. 

# honestly cwh goat

# suppose we wish to define a function which is not related to any object, like greet then theres rlly no need of the self param
harry.greet()
harry.signature("abadakadabra")

