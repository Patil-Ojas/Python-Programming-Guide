def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [98, 67, 78, 83]
percent1 = percent(marks1)
print(percent1)

marks2 = [55, 66, 77, 88]
percent2 = (sum(marks2)/400)*100           #inbuilt function
print(percent2)

