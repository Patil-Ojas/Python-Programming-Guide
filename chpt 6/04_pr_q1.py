a = int(input("enter no "))
b = int(input("enter no "))
c = int(input("enter no "))
d = int(input("enter no "))

if (a>b) and (a>c) and (a>d):
    print(a, "is the greatest")
elif (b>a) and (b>c) and (b>d):
    print(b, "is the greatest")
elif (c>a) and (c>b) and (c>d):
    print(c, "is greatest")
else:
    print(d, "is greatest")


