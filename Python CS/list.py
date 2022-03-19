# # List --> It is datatype to store multiple values
# # [ ] --> square brackets

# numbers = [45,12,26,98,"Ptyhon",23.23]
# print(numbers)

# # Empty list 
# num = []
# print(num)

# nums = list()
# print(nums)


# # Nested List
# a = [45,23,[23,6,[23,12,56]],89]
# print(a)


# # Accessing Lists
# #     -5 -4 -3 -2 -1 
# b = [45,12,56,23,20]
# #     0  1  2  3  4 ---> indexing

# # whole list 
# print(b)

# # printing elements
# print(b[4])
# print(b[-2])

# comments --> #

# Traversing a list 
b = [45,12,56,23,20]

for i in b:
    print(i)


# List : Built-in Functions 
n = [12,12,23,56,12,23,89,23]

# 1. append()
n.append(90)

# 2. insert()
n.insert(1,40)

# 3. extend()
l1 = [96,23,56]
n.extend(l1)
print(n)

# 4. sum()
print(sum(n))


# 5. count()
print(n.count(12))

# 6. len()
print(len(n))

# 7. index()
print(n.index(56))

# 8. min()
print(min(n))

# 9. max()
print(max(n))

# 10. reverse()
n.reverse()
print(n)

# 11. pop()
print(n.pop())

# 12. remove()
n.remove(89)
print(n)

# 13. sort()
n.sort()
print(n)

# 14. list()
s = 'python'
new_string = list(s)
print(new_string)

# 15. clear()
l1.clear()
print(l1)

