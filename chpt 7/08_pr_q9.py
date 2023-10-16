
l1 = ['harry', 'soham', 'sachin', 'rahul']
# i = str(input("emter name"))
# if (i in l1):
#     if('s' in i):
#      print('greetings',i)
#     else:
#         print("no greets fo u",i)
# else:
#     print('nope')
for name in l1:
    if name.startswith('s'):
        print('greets', name)
