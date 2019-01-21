"""
    ENUMERATE
Allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element). The function itself is equivalent 
"""

# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
              
lst = ['a','b','c']

for number,item in enumerate(lst):
    print(number, ' - ',item)
# 0  -  a
# 1  -  b
# 2  -  c
    
    
#enumerate() becomes particularly useful when you have a case where you need 
#to have some sort of tracker. For example:
for count, item in enumerate(lst):
  if count >= 2:
    break
  else:
    print(item)
# a
# b    

# enumerate() takes an optional "start" argument to override the default 
#value of zero:
months = ['March','April','May','June']
print(list(enumerate(months,start=3)))
# [(3, 'March'), (4, 'April'), (5, 'May'), (6, 'June')]

"""
    ZIP

zip() makes an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables.

Let's see it in action in some examples:
"""

# def zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)

x = [1,2,3]
y = [4,5,6,7,8]

# Zip the lists together
print(list(zip(x,y)))
# [(1, 4), (2, 5), (3, 6)]

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5, 'f': 7}

print(list(zip(d1,d2)))
# [('a', 'c'), ('b', 'd')]
print(list(zip(d2,d1.values())))
# [('c', 1), ('d', 2)]

list_zip = zip(x, y)
print(list_zip)
# <zip object at 0x10da84c88>
z = dict(list_zip)
print(z)
# {1: 4, 2: 5, 3: 6}

##########################
# Using as parameter
##########################
def pessoa(nome, sobrenome, idade):
  print(f"O nome eh {nome} {sobrenome} e a idade {idade}")

parametros = ['nome','sobrenome', 'idade']
valores = ['Fabio', 'de Simoni', 38]

pessoa(**dict(zip(parametros, valores)))
# O nome eh Fabio de Simoni e a idade 38





def concatenate(L1, L2, connector):
  l = []
  for (x, y) in zip(L1, L2):
    l.append(x+connector+y)
  return l

print(concatenate(['A','B'],['a','b'],'-'))
# ['A-a', 'B-b']

#or

def concatenate2(L1, L2, connector):
  return [word1+connector+word2 for (word1, word2) in zip(L1, L2)]

print(concatenate2(['A','B'],['a','b'],'-'))
# ['A-a', 'B-b']



"""
    RANDON
"""
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
shuffle(mylist)
mylist
# [40, 10, 100, 30, 20]

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100)
# 25

# Return random integer in range [a, b], including both end points.
randint(0,100)
# 91

