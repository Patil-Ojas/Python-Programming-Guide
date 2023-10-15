# dictionary = (key: value)

dict = {
     "harry": "a coder",
     "fast": "in a quick manner",
     "marks": [1, 2, 5],
     "dict2": {'harry': 'player'},
     1: 2
} 

# print(dict.items())
# print(dict.keys())
# print(dict.values())

print(list(dict.keys()))               # good shit
print(type(dict))
     
# updict = { 
#     "bru": "bruhhh",
#     "harry": "a ytber"           #yeets the previous value of the same key
# }
# dict.update(updict)
# print(dict)

# print(dict["harry3"])              # gives error if key isnt there (both give same if key present)
print(dict.get("harry3"))            # returns none if key isnt there
