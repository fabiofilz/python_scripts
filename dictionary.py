#####################################
# DICTIONARIES
#####################################

all_studants = [
    {"name":"Fabio", "studant_id":1, "depto":"IT" },
    {"name":"Fernanda", "studant_id":2, "depto":"Teaching" },
    {"name":"Felipe", "studant_id":3, "depto":"Engineering" }
]

print(all_studants[0]["name"])
# Fabio
print(all_studants[0].get("last_name", "Unknow"))   #### retorna como se fosse o valor do campo
# Unknow

print(all_studants[0].keys())
# dict_keys(['name', 'studant_id', 'depto'])
print(all_studants[0].values())
# dict_values(['Fabio', 1, 'IT'])
print(all_studants[0].items())
# dict_items([('name', 'Fabio'), ('studant_id', 1), ('depto', 'IT')])

print(all_studants[0])
# {'name': 'Fabio', 'studant_id': 1, 'depto': 'IT'}

# Removing item name from element 0
del all_studants[0]["name"]
print(all_studants[0])
# {'studant_id': 1, 'depto': 'IT'}


def add_studant(name, studant_id, depto):
  stud = {"name": name, "studant_id": studant_id, "depto":depto }
  all_studants.append(stud)

# Adding new item
add_studant("Rita", 40, "Retired")
print(all_studants)
# [{'studant_id': 1, 'depto': 'IT'}, {'name': 'Fernanda', 'studant_id': 2, 'depto': 'Teaching'}, {'name': 'Felipe', 'studant_id': 3, 'depto': 'Engineering'}, {'name': 'Rita', 'studant_id': 40, 'depto': 'Retired'}]

def get_student_title():
  stud = []
  
  for student in all_studants:
    stud.append(student.get("name", "Unknow").title())
    
  return stud

print("LearnerAnswersStore.list_learners: ", get_student_title())
# LearnerAnswersStore.list_learners:  ['Unknow', 'Fernanda', 'Felipe', 'Rita']

# PPRINT
######################33
import pprint
pprint.pprint(all_studants)
# [{'depto': 'IT', 'studant_id': 1},
#  {'depto': 'Teaching', 'name': 'Fernanda', 'studant_id': 2},
#  {'depto': 'Engineering', 'name': 'Felipe', 'studant_id': 3},
#  {'depto': 'Retired', 'name': 'Rita', 'studant_id': 40}]



# Percorrendo
########################
qty = 0
for student_d in all_studants:
  qty += 1
  print("--------------------")
  qty2 = 0
  for student in student_d:
      qty2 += 1
      print("Item ", qty , " - elemento: ", qty2 ," Key: ", student, ", valor: ", student_d[student])

# --------------------
# Item  1  - elemento:  1  Key:  studant_id , valor:  1
# Item  1  - elemento:  2  Key:  depto , valor:  IT
# --------------------
# Item  2  - elemento:  1  Key:  name , valor:  Fernanda
# Item  2  - elemento:  2  Key:  studant_id , valor:  2
# Item  2  - elemento:  3  Key:  depto , valor:  Teaching
# --------------------
# Item  3  - elemento:  1  Key:  name , valor:  Felipe
# Item  3  - elemento:  2  Key:  studant_id , valor:  3
# Item  3  - elemento:  3  Key:  depto , valor:  Engineering
# --------------------
# Item  4  - elemento:  1  Key:  name , valor:  Rita
# Item  4  - elemento:  2  Key:  studant_id , valor:  40
# Item  4  - elemento:  3  Key:  depto , valor:  Retired


d = {'k1':1,'k2':2,'k3':3}
for item, value in d:
    print(item, '-', value)


print(list(d.keys()))
# ['k1', 'k2', 'k3']

# Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():
print(sorted(d.values()))
# [1, 2, 3]