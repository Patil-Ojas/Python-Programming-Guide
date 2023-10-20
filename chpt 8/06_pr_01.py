def great(num1, num2, num3):
    if (num1>num2) and (num1>num3):
        return print(num1, "is the greatest")
    if (num2>num1) and (num2>num3):
        return print(num2, "is the greatest")
    else:
        return print(num3, "is the greatest")

nu1 = int(input('first:'))
nu2 = int(input("second:"))
nu3 = int(input("third:"))

great(nu1, nu2, nu3)


