# Tuple --> It is datatypes to store multiple datatype

# list vs tuple
# list : mutuble (can change)
# tuple : immutable (cannot change)

# ( ) --> round brackets
tup = (89,23,56,78)


# Accessing tuple
print(tup)

print(tup[2])

# Empty tuple 

tups = ()
print(tups)

tupl = tuple()
print(tupl)


# Tuple : Built-in Functions
num = (23,89,56,23,23,47,16,2)

# 1. len()
print(len(num))


# 2. count()
print(num.count(23))

# 3. max()
print(max(num))

# 4. min()
print(min(num))

# 5. sorted()
sorted(num)
print(num)

# 6. index()
print(num.index(23))

# 7. tuple()
s = 'Namaste world'
new = tuple(s)
print(new)

# 8. sum()
print(sum(num))

# 9. reversed()
t = reversed(num)

for i in t:
    print(i)


# deleting a tuple 
del (tup)
print(tup) # get en error 