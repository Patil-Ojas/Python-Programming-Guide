n1 = 'samsung'
n2 = "one plus'"
n3 = ''' all'can"be used '''
# print(n1, n2, n3)

m1 = 'we can '
m2 = 'connect two strings'
# print(m1 + m2)

x = 'Letter'
# print(x[0])
# print(x[1])
# string slicing
print(x[0:3])   #considers  0,1,2 only.
print(x[:4])     #same as 0:4
print(x[0:])     #same as 0:5, used to find length of str

# negative indices used to pritn letters from behind
x = "bruhyomo"
print(x[-1])
print(x[-5:-2]) 
print(x[-6:-2:2]) 

# string skipping
y = 'abiglengthyword'
print(y[0:15:2])

