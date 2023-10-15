comment = str(input("enter the comment"))

if("more money" in comment):
    spam = True
elif("click here"):
    spam = True
else:
    spam = False

if spam:
    print("tis spam")
else:
    print("tis not spam")