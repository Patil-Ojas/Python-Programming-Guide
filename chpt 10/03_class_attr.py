
class employee:
    # class attribute
    company = "Google"



harry = employee()
rajni = employee()

print(harry.company)
print(rajni.company)

employee.company = "Youtube"

print(harry.company)
print(rajni.company)

# but harry and rajni wont have the same attributes, so we have instance attributes

harry.salary = 300
rajni.salary = 400

print(harry.salary)
print(rajni.salary)

