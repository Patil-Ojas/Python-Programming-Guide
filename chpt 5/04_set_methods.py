# union and intersections cmds scuffed, ez

a = set()
print(type(a))

a.add(4)
a.add(4)
a.add(5)
a.add(9)
# a.add([1,3,7])         cant add list
# a.add({2:3})           cant add dict
# a.add((1,2,3))           can add tuple
# a.remove(5)
# print(a)
# print(len(a))
# print(a.pop())           randomly yeets and returns yeeted element
# a.clear()
print(a)
a = a.union({8,9})
print(a)
a = a.intersection({8,9})
print(a)
