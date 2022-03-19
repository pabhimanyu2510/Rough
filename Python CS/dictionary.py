# dictionary --> it is unoredered collections of data values.

# words : meaning 
# keys : values
# run : bhagna

# key + values : item
# {} --> curly brackets
# Creating a dictionary 
dict = {
    'key' : 'values',
    'run' : 'bhagna',
    23:8923,
    'pass' : 5623
}


# Accessing a dictionary 

# whole dictionary
print(dict)

# print a value
print(dict['pass'])

# Nested Dictionary

nest = {
    'dict' : {'key' : 'values','run' : 'bhagna',23:8923, 'pass' : 5623 },
    'jump'  : 'kudna',
    20 : 'python'
}

print(nest['dict'])
print(nest[20])

# dictionary Built-in Functions
dict = {
    'key' : 'values',
    'run' : 'bhagna',
    23:8923,
    'pass' : 5623
}

# 1. len()
print(len(dict))

# 2. get()
print(dict['pass'])

# 3. items()
print(dict.items())

# 4. keys()
print(dict.keys())

# 5. values()
print(dict.values())

# 6. update()
num = {
    45:89,
    'p' : 5989,
    'name' : 'rohan'
}

dict.update(num)
print(dict)

# 7. fromkeys()
key = [12,23,56,56]
value = dict.fromkeys(key)
print(value)

# 8. copy()
dic1 = dict.copy()
print(dic1)


nums  = {
    'rohan' : 56,
    'sohan' : 89,
    'rita' : 23
}
# # 9. max()
# print(max(nums))

# # 10. min()
# print(min(num))

