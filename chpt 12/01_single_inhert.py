
class Employee:
    company = "Google"

    def showDetails(self):
        print("These are details of an emplyee")
    
# has access to the employee class
class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print("Language is ", self.language)

    # if we have method ovveriding, this gets preferece
    def showDetails(self):
        print("This is programmer")


emp = Employee()
emp.showDetails()

prog = Programmer()
prog.showDetails()
print(prog.company)
