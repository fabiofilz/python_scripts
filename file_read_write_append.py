##############################################
# READ / WRITE / APPEND FILE
##############################################


def save(student, tp):
  try:
    f = open("students.txt", tp) ### append 
    f.write(str(student) + "\n")
    f.close()
  except Exception:
    print("Cannot save")

def read_file():
  try:
    f = open("students.txt", "r") ### read
    for student in f.readlines():
      print(student)
    f.close()
  except Exception:
    print("Cannot read")
    
    
all_studants = [
    {"name":"Fabio", "studant_id":1, "depto":"IT" },
    {"name":"Fernanda", "studant_id":2, "depto":"Teaching" },
    {"name":"Felipe", "studant_id":3, "depto":"Engineering" }
]

for s in all_studants:
  a = "a" # APPEND
  save(s, a)
  
read_file()

# WRITE
{'name': 'Felipe', 'studant_id': 3, 'depto': 'Engineering'}
{'name': 'Fabio', 'studant_id': 1, 'depto': 'IT'}
{'name': 'Fernanda', 'studant_id': 2, 'depto': 'Teaching'}
# READ
{'name': 'Felipe', 'studant_id': 3, 'depto': 'Engineering'}
{'name': 'Fabio', 'studant_id': 1, 'depto': 'IT'}
{'name': 'Fernanda', 'studant_id': 2, 'depto': 'Teaching'}

# print PATH
print(pwd)
"/Users/fabiodesimoni/Development/Python/scripts/tempCodeRunnerFile.py#

# Seek to the start of file (index 0)
my_file.seek(0)

# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()

