sub1 = int(input("enter marks for sub1: "))
sub2 = int(input("enter marks for sub2: "))
sub3 = int(input("enter marks for sub3: "))
total = sub1+sub2+sub3

if (sub1<33):
    print("he fail in sub1")
else:
        print("he pass")
if (sub2<33):
    print("he fail in s2")
else:
        print("he pass")
if (sub3<33):
    print("he fail in s3")
else:
        print("he pass")
if (total/3<40):
    print('he bad')
else:
    print("he good")