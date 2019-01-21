lista = ["0 - A", "1 - B", "2 - C", "3 - D", "4 - E", "5 - F", "6 - G", "7 - H"]

print(lista)
# ['0 - A', '1 - B', '2 - C', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H']

print(lista[1:])
# ['1 - B', '2 - C', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H']
print(lista[2:])
# ['2 - C', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H']
print(lista[2:5])
# ['2 - C', '3 - D', '4 - E']
print(lista[:3])
# ['0 - A', '1 - B', '2 - C']
print(lista[-1]) # ultimo elemento
# 7 - H
print(lista[-2:-1])
# ['6 - G']


# Adiciona o item no final da lista
lista.append("_")
lista.append("X")
print(lista)
# ['0 - A', '1 - B', '2 - C', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H', '_', 'X']

# Verifica se o item existe numa lista usando o IN
print( "X" in lista)
# True

print("Qty", len(lista))
print("Deleta o item 2")
del lista[2]
print("Qty", len(lista))
# Qty 10
# Deleta o item 2
# Qty 9


# List of string 
listOfStrings = ['Hi' , 'hello', 'at', 'this', 'there', 'from']

if 'at' in listOfStrings :
    print("Yes, 'at' found in List : " , listOfStrings)
    
if listOfStrings.count('at') > 0 :
    print("Yes, 'at' found in List : " , listOfStrings)
# Yes, 'at' found in List :  ['Hi', 'hello', 'at', 'this', 'there', 'from']
# Yes, 'at' found in List :  ['Hi', 'hello', 'at', 'this', 'there', 'from']


# Pega objetos da lista de 2 em 2 do elemento 2 ate o 7: [2:8:2]
print(listOfStrings[2:8:2])
# ['at', 'there']

#Investir order de uma string  ----- [::-1]
print("He said his name is Fabio and he is 21 years old."[::-1])
# .dlo sraey 12 si eh dna oibaF si eman sih dias eH

# Add posicao, objeto
# Adiciona o item na posicao que quiser
lista.insert(0, "A - A(novo)")
print(lista)
# ['A - A(novo)', '0 - A', '1 - B', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H', '_', 'X']


# Pega um item e remove da lista valor padrao eh -1
# POP - Pega o item e remove da lista
lista.pop(-1)
print(lista)
# ['A - A(novo)', '0 - A', '1 - B', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H', '_']

# Reverse - Investe, mas nao muda o object
lista.reverse()
print(lista)
# ['_', '7 - H', '6 - G', '5 - F', '4 - E', '3 - D', '1 - B', '0 - A', 'A - A(novo)']

# Ordenacao - muda o object
# Sort lista
lista.sort(reverse=True)
print(lista)
# ['_', 'A - A(novo)', '7 - H', '6 - G', '5 - F', '4 - E', '3 - D', '1 - B', '0 - A']

# Using Sorted - sort, but don't change the object
print(sorted(lista))
# ['0 - A', '1 - B', '3 - D', '4 - E', '5 - F', '6 - G', '7 - H', 'A - A(novo)', '_']
print(lista)
# ['_', 'A - A(novo)', '7 - H', '6 - G', '5 - F', '4 - E', '3 - D', '1 - B', '0 - A']

# Quantas vezes o item aparece na lista
print("Conta quantas vezes o item aparece na lista")
print(lista.count("6 - G"))
# 1

# Pega a posicao do object ### se o item nao existir retorn erro ValueError
print("Pega a posicao do object '6 - G'")
print(lista.index("6 - G"))
# 3


# Concatenar lista
x = [1, 2, 3]
y = [4, 5, 6]
# Extend
x.extend(y)
print(x)
# [1, 2, 3, 4, 5, 6]

# Clean list
x.clear()
print(x)
# []

# Adding
my_list = ['one','two','three',4,5]
my_list += ['new item']
print(my_list)
# ['one', 'two', 'three', 4, 5, 'new item']

