list_1=["dinesh","kumar","python","java","kotlin"]

print(list_1)
# Output :   ['dinesh', 'kumar', 'python', 'java', 'kotlin']

print(list_1[2:4])
# Output :  ['python', 'java']



dir(list_1)
#  Output :   ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

list_2=list_1.copy()
print(list_2)
#  Output :   ['dinesh', 'kumar', 'python', 'java', 'kotlin']

list_2.append("django")
print(list_2)
#  Output :   ['dinesh', 'kumar', 'python', 'java', 'kotlin', 'django']

list_3=["django","flask","flutter"]
list_2.extend(list_3)
print(list_2)
#  Output :   ['dinesh', 'kumar', 'python', 'java', 'kotlin', 'django', 'django', 'flask', 'flutter']

list_2.count("flask")
#  Output :   1
list_2.count("django")
#  Output :   2

list_2.index("flask")
#  Output :   7

list_2.pop()
#  Output :   'flutter'
list_2.pop()
#  Output :   'flask'


list_2.insert(2,"swift")
print(list_2)
#  Output :   ['dinesh', 'kumar', 'swift', 'python', 'java', 'kotlin', 'django', 'django']
list_2.insert(4,"rust")
print(list_2)
#  Output :   ['dinesh', 'kumar', 'swift', 'python', 'rust', 'java', 'kotlin', 'django', 'django']

list_2.remove("django")
print(list_2)
#  Output :   ['dinesh', 'kumar', 'swift', 'python', 'rust', 'java', 'kotlin', 'django']
list_2.remove("java")
print(list_2)
#  Output :   ['dinesh', 'kumar', 'swift', 'python', 'rust', 'kotlin', 'django']

list_2.reverse()
print(list_2)
#  Output :   ['django', 'kotlin', 'rust', 'python', 'swift', 'kumar', 'dinesh']

list_2.sort()
print(list_2)
#  Output :   ['dinesh', 'django', 'kotlin', 'kumar', 'python', 'rust', 'swift']

list_2.clear()
print(list_2)
#  Output :   []



tuple_1=("dinesh","kumar","hosur","vellore","banglore")

print(tuple_1)
#  Output :   ('dinesh', 'kumar', 'hosur', 'vellore', 'banglore')

dir(tuple)
#  Output :   ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


print(tuple_1[:3])
#  Output :   ('dinesh', 'kumar', 'hosur')

tuple_1.count("kumar")
#  Output :   1

tuple_1.index("vellore")
#  Output :   3


dict_1={'name':"Dinesh","clg":'AMCET','DEPT':'CSE','Rollno':12}

print(dict_1)
#  Output :   {'name': 'Dinesh', 'clg': 'AMCET', 'DEPT': 'CSE', 'Rollno': 12}

dir(dict_1)
#  Output :   ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

dict_2=dict_1.copy()
print(dict_2)
#  Output :   {'name': 'Dinesh', 'clg': 'AMCET', 'DEPT': 'CSE', 'Rollno': 12}

dict_2.get('name')
#  Output :   'Dinesh'

dict_2.get('cgpa',9.0)
#  Output :   9.0

print(dict_2['clg'])
#  Output :   AMCET

dict_2.items()
#  Output :   dict_items([('name', 'Dinesh'), ('clg', 'AMCET'), ('DEPT', 'CSE'), ('Rollno', 12)])

dict_2.keys()
#  Output :   dict_keys(['name', 'clg', 'DEPT', 'Rollno'])

dict_2.values()
#  Output :   dict_values(['Dinesh', 'AMCET', 'CSE', 12])

dict_2.popitem()
#  Output :   ('Rollno', 12)
print(dict_2)
#  Output :   {'name': 'Dinesh', 'clg': 'AMCET', 'DEPT': 'CSE'}

dict_2.pop('clg')
#  Output :   'AMCET'
print(dict_2)
#  Output :   {'name': 'Dinesh', 'DEPT': 'CSE'}

dict_3={'area':'vellore','home':'hosur'}
dict_2.update(dict_3)
print(dict_2)
#  Output :   {'name': 'Dinesh', 'DEPT': 'CSE', 'area': 'vellore', 'home': 'hosur'}

dict_4=dict.fromkeys(('x','y','z'),0)
print(dict_4)
#  Output :   {'x': 0, 'y': 0, 'z': 0}

dict_2.setdefault('year',3)
3
print(dict_2)
#  Output :   {'name': 'Dinesh', 'DEPT': 'CSE', 'area': 'vellore', 'home': 'hosur', 'year': 3}

dict_2.clear()
print(dict_2)
#  Output :   {}