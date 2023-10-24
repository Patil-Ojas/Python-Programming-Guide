
class employee:
    company = "camel"
    salary = 100
    location = "Delhi"

    def changeSalary(self, sal):
        # dunder methods?
        self.__class__.salary = sal

    @classmethod
    def changeSalaryyes(cls, sal):
        cls.salary = sal

e = employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(employee.salary)
e.changeSalaryyes(450)
print(e.salary)
print(employee.salary)

