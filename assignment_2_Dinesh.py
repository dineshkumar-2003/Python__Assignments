#Creating a nested dictionary
dict_1={'college': 'AMCET', 'student_1': {'name': 'Dinesh', 'rollno': 12, 'marks': {'c': 90, 'python': 95}}, 'student_2': {'name': 'Kumar', 'rollno': 13, 'marks': {'c': 95, 'python': 90}}}

#printing the nested dictionary
print(dict_1)       
# Output :  {'college': 'AMCET', 'student_1': {'name': 'Dinesh', 'rollno': 12, 'marks': {'c': 90, 'python': 95}}, 'student_2': {'name': 'Kumar', 'rollno': 13, 'marks': {'c': 95, 'python': 90}}}

#Accessing specofic values from the nested dictionary through get()
dict_1.get('college')
# Output :  'AMCET'

dict_1.get('student_1')       
# Output :  {'name': 'Dinesh', 'rollno': 12, 'marks': {'c': 90, 'python': 95}}

dict_1.get('student_2')         
# Output :  {'name': 'Kumar', 'rollno': 13, 'marks': {'c': 95, 'python': 90}}

#Accessing the values of nested dictionary through direct keys
print(dict_1['student_1'])        
# Output :  {'name': 'Dinesh', 'rollno': 12, 'marks': {'c': 90, 'python': 95}}

print(dict_1['student_1']['marks'])         
# Output :  {'c': 90, 'python': 95}

print(dict_1['student_2']['marks'])       
# Output :  {'c': 95, 'python': 90}

#Creating another nested dictionary with more than 3 nested values
dict_2={'Transport':'car','name':{'car_1':'BMW' ,'car_2':'Tesla' ,'car_3':{'model':'Ferrari','speed':{'in_km':90,'in_miles':17}}}}
           
dict_2.keys()           
# Output :  dict_keys(['Transport', 'name'])

dict_2.values()         
# Output :  dict_values(['car', {'car_1': 'BMW', 'car_2': 'Tesla', 'car_3': {'model': 'Ferrari', 'speed': {'in_km': 90, 'in_miles': 17}}}])

dict_2.get('name')           
# Output :  {'car_1': 'BMW', 'car_2': 'Tesla', 'car_3': {'model': 'Ferrari', 'speed': {'in_km': 90, 'in_miles': 17}}}

print(dict_2['name']['car_3'])         
# Output :  {'model': 'Ferrari', 'speed': {'in_km': 90, 'in_miles': 17}}


#Creating a set
set_1={'dinesh','kumar','suba','srinivasan'}

#set is unordered so the output may be random
print(set_1)       
# Output :  {'srinivasan', 'suba', 'kumar', 'dinesh'}

#checking the built in functions for set
dir(set_1)
           
# Output :  ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#copying the set
set_2=set_1.copy()           
print(set_2)           
# Output :  {'srinivasan', 'suba', 'kumar', 'dinesh'}

#Adding values to the set
set_2.add('python')          
print(set_2)           
# Output :  {'srinivasan', 'python', 'suba', 'kumar', 'dinesh'}

#Using difference to find the element that is not common
set_1.difference(set_2)           
set()
set_2.difference(set_1)           
# Output :  {'python'}

#using difference_update()
set_3={'srinivasan', 'python', 'suba', 'kumar', 'dinesh','java'}
set_3.difference_update(set_2)          
print(set_3)          
# Output :  {'java'}

#Using discard to remove specific element in the set
set_2.discard('suba')           
print(set_2)         
# Output :  {'srinivasan', 'python', 'kumar', 'dinesh'}

#getting common elements using intersection
set_1.intersection(set_2)         
# Output :  {'srinivasan', 'kumar', 'dinesh'}

#intersection_update() finds common element and removes other element
set_1.intersection_update(set_2)          
print(set_1)           
# Output :  {'srinivasan', 'kumar', 'dinesh'}

#isdisjoint() returns true if there is no common elements
set_1.isdisjoint(set_3)          
# Output :  True

#pop() removes a random element
set_2.pop()          
# Output :  'srinivasan'

#remove() deletes a specific element
set_1.remove('kumar')          
print(set_1)          
# Output :  {'srinivasan', 'dinesh'}

#issubset() method
set_1.issubset(set_2)       
# Output :  False

#union() returns all the elements from both the list
set_2.union(set_3)         
# Output :  {'java', 'python', 'kumar', 'dinesh'}

#update() is used to join two sets
set_2.update(set_3)
print(set_2)          
# Output :  {'python', 'java', 'kumar', 'dinesh'}



#if elif else

#to check if the number is +ve or -ve

num=int(input("Enter the number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("zero")
'''
Output:
 Enter the number:10
 Positive number
 '''

#to check even or odd

num=int(input("Enter the number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")
'''
Output:
Enter the number:17
Odd number
'''

#for loop -- to iterate through a range of numbers

for itr in range(11):
    print(itr)
'''
Output:
0
1
2
3
4
5
6
7
8
9
10
'''

#for loop using enumerate-- used to print the values with the index

list_1=['Dinesh','Kumar','Python','Java']
for index,val in enumerate(list_1):
    print(index," : ",val)

'''
Output:
0  :  Dinesh
1  :  Kumar
2  :  Python
3  :  Java
'''

#for loop with break-- stops the loop when condition is met

for itr in range(10):
    if itr==7:
        break
    else:
        print(itr)

'''
Output:
0
1
2
3
4
5
6
'''

#for loop with continue --it is used to skip a particular iteration

for itr in range(11):
    if itr==5:
        continue
    else:
        print(itr)

'''
Output:
0
1
2
3
4
6
7
8
9
10
'''

#Printing words except w and o using continue
str='hello world'
for char in str:
    if char=='w' or char=='o':
        continue
    else:
        print(char,end='')

'''
OUTPUT :
hell rld
'''

#To count numner of o's in str using continue
str='Welcome to python'
count=0
for char in str:
    if char=='o':
        print(char)
        count+=1
    else:
        continue
print(f'Count of o in {str} is : {count}')

'''
OUTPUT:
o
o
o
Count of o in Welcome to python is : 3
'''