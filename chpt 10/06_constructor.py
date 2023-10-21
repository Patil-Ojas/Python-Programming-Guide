class employee:
    company = "Google"

    # constructor basically runs when object is born
    def __init__(self, name, salary, comp):
        print("Employee is created")
        # usually same vars preferred
        self.name = name
        self.salary = salary
        self.comp = comp
    
    def printDetails(self):
        print("Name is ", self.name)
        print("salary is ", self.salary)
        print("company is ", self.comp)
    

harry = employee("Harry", "100,000", "Youtube")
harry.printDetails()
