"""
    Python's list comprehensions

 vals = [expression 
        for value in collection 
        if condition]

This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)
""" 

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)
# [0, 4, 16, 36, 64]


#############

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print([x * y for x in lst1 for y in lst2])
# [3, 4, 5, 6, 8, 10, 9, 12, 15]

print([x for x in lst1 if 4 > x > 1])
# [2, 3]

# Check if a condition is true for any items.
# "any" returns true if any item in the list is true.
print(any([i % 3 for i in [3, 3, 4, 4, 3]]))
# True

# This is because 4 % 3 = 1, and 1 is true, so any()
# returns True.

# Check for how many items a condition is true.
print(sum(1 for i in [3, 3, 4, 4, 3] if i == 4))
# 2

del lst1[0]
print(lst1)
#[2, 3]
del lst1
# print(lst1) ## error



# Grab every letter in string
lst = [x for x in 'word']
print(lst)
# ['w', 'o', 'r', 'd']

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)
# [32.0, 50.0, 68.18, 94.1]

lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)
# [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]