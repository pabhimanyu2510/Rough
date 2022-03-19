# slicing operations
# list , tuple , string

# slicing - parts
s = [12,23,56,52,78,89,23]
#     0  1  2  3  4  5  6

# [start: (stop-1) : (step-1)]

# forward slicing
print(s[0:3])

print(s[:2])
print(s[2:])

print(s[1:5:2])

# backward slicing
print(s[5:2:-1])