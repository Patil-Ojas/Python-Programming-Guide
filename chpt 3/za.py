#Replace all ______ with rjust, ljust or center. 

thickness = int(input('A    ')) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).ljust(thickness-1)+c+(c*i).rjust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2)+(c*thickness).ljust(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2)+(c*thickness).ljust(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).ljust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))