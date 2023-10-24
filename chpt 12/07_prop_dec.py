# meh

class Employee:
    company = "Bharat Gas"
    salary = 500
    bonus = 250

    @property
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.getter
    def totalSalary(self, val):
        self.bonus = val - self.salary

e = Employee
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.bonus)