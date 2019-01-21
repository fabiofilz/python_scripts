##############################################
# SET
# remove duplicated itens and put in order
##############################################

x = set()
# We add to sets with the add() method
x.add(1)
print(x)
# {1}


# Converting list to set
print(set([2,1,7,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,6,1,1,1,1,1]))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# converting set to list
print(list(set([2,1,7,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,6,1,1,1,1,1])))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


a = {1, 2, 3, 4, 5}
b = {1, 2, 6, 7, 8}
print(a.union(b))
# {1, 2, 3, 4, 5, 6, 7, 8}

print(a.intersection(b))
# {1, 2}
#Esta no A, mas nao esta no B

print(a.difference(b))
# {3, 4, 5}
