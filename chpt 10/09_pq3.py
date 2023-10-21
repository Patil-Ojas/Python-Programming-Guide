
class atrrtest:
    a = 5

    
obj = atrrtest()
obj.a = 2
print(obj.a)

obj.a = 0
print(atrrtest.a)

# no it does not
# this is what does

atrrtest.a = 7
print(atrrtest.a)

