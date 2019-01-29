"""
    *args
    Tupla
    *args = (1, 2, 3, 4, 5)
    funcao(*nome_lista/tupla)
"""

def mult(name, *args):
    print(name)
    print(*args)
    print(args) # casting to tuple
    print(type(args))
  
  
mult("fabio", 1,23,3,4,5,5,67,7,8,5,4,3,3,2,1)
# fabio
# 1 23 3 4 5 5 67 7 8 5 4 3 3 2 1
# (1, 23, 3, 4, 5, 5, 67, 7, 8, 5, 4, 3, 3, 2, 1)
# <class 'tuple'>

param = [1, 2, 3, 4,5]
name = 'Fabio'

mult(name, *param)
# Fabio
# 1 2 3 4 5
# (1, 2, 3, 4, 5)
# <class 'tuple'>


"""
    **Kwargs
    Dictionary **kwargs => a=1, b=2, c=3, d=4
    funcao(**nome_dicionario)
"""

def mult(name, **kwargs):
    print(name)
    print(kwargs["description"], ' - ', kwargs["feedback"])
  
  
mult("Fabio", description="descricao", feedback="feed", other="outros")
# Fabio
# descricao  -  feed


d = {"description":"descricao", "feedback":"feed", "other":"outros"}
print(d)
# {'description': 'descricao', 'feedback': 'feed', 'other': 'outros'}

mult("Fabio", **d)
# Fabio
# descricao  -  feed





###################

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' And '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')
print()
myfunc('eggs',fruit='cherries',juice='orange')





def myfunc(*args):
    return sum(args)*.05

print(myfunc(40,60,20))
# 6.0


