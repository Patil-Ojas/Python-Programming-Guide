
# now comes the ambiguity that is both instance and class have the instantiations with the same name, which will be given preference
# first preference given to instance/object attribute then preference given to class attribute if neither gives error

class employee():
    company = "Google"
    salary = 100

harry = employee()
rajni = employee()
brug = employee()

harry.salary = 300
rajni.salary = 400

print(harry.salary)
print(rajni.salary)
print(brug.salary)

# we can see object instantiation gets first preference

