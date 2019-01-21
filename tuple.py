###################################
# Tuple - Immutability
###################################
tup = (8,1,8,0,10, 55)
print(tup)
# (8, 1, 8, 0, 10, 55)

l = [tup]
print(l)
# [(8, 1, 8, 0, 10, 55)]

# Convert tupla to list
l = [*tup]
print(l)
# [8, 1, 8, 0, 10, 55]


# Create a tuple
t = ('one',2)

# Use .index to enter a value and return the index
print(t.index('one'))
# 0

# Use .count to count the number of times a value appears
print(t.count('one'))
# 1

# A tuple is immutable, but the objects inside it isn't
tp = ([1 , 2], [3, 4])
print(tp)
tp[0].append(7) # in the end
tp[0].insert(0, 8) # positional
print(tp)


