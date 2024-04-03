class Calculator:

    def __init__(self,num_1,num_2): #using __init__ to initialize the variables
        self.num_1=num_1
        self.num_2=num_2

    def display(self):
        print(f"The parameters passed through __init__ are  num_1 ={self.num_1} and num_2={self.num_2}")

    def addition(self,num_3=0): # num_3=0 is the Kwarg
        return self.num_1+self.num_2+num_3
    
    def subtraction(self):
        choice=int(input("Enter 1 for num1 - num2 or 2 for num2 - num1: "))
        match choice:   #Using match case
            case 1:
                return self.num_1-self.num_2        #Accessing vslues through self
            case 2:
                return self.num_2-self.num_1    
            
    def multiplication(self,num_1,num_2,*arg):   #Using arg
        ans=num_1*num_2        # Accessing values from parameters 
        for args in arg:
            ans=ans*args
            return ans
        
    def division(self,num_1,num_2):
        try:        #Using try and except
            ans=num_1//num_2
        except ZeroDivisionError as e:
            print("Divide by zero is not possible :",e)

            
obj_1=Calculator(10,20)  #Creating the object for the class

obj_1.display()

#Calling addition method with the kwarg
result_add=obj_1.addition(30)
print("The added value is ",result_add)

#caliing the subtraction method with the match - case
result_sub=obj_1.subtraction()
print("The subtracted value is ",result_sub)

#calling the multiplication method with args
result_mul=obj_1.multiplication(10,20,3)
print("The multiplied value is ",result_mul)

#Calling division with try and catch
result_div=obj_1.division(10,0)
print("The divided value is ",result_div)


'''
OUTPUT:
The parameters passed through __init__ are  num_1 =10 and num_2=20
The added value is  60
Enter 1 for num1 - num2 or 2 for num2 - num1: 2
The subtracted value is  10
The multiplied value is  600
Divide by zero is not possible : integer division or modulo by zero
The divided value is  None
'''

import statistics
class College:

    def __init__(self,name,rollno,dept):
        self.students={}
        self.students['Name']=name
        self.students['Rollno']=rollno
        self.students['Department']=dept

    def student_mark(self,sub_1,sub_2,sub_3):
        '''
        This method is used to assign the marks to the student
        '''
        self.marks={'Subject 1':sub_1,'Subject 2':sub_2,'Subject 3':sub_3}

    def average(self):
        mark_1=self.marks['Subject 1']
        mark_2=self.marks['Subject 1']
        mark_3=self.marks['Subject 1']
        return statistics.mean([mark_1,mark_2,mark_3])
    
    def student_grade(self):
        average=self.average()
        match (average):
            case x if average>90:
                print('O Grade')
            case x if average>80 and average<=90:
                print("A Grade")
            case x if average>70 and average<=80:
                print("B Grade")
            case x if average>60 and average<=70:
                print("A+ Grade")
            case _:
                print("Fail")
    
    def report_card(self):
        '''
        Method to print the Rank card
        '''
        print()
        print("--------------Report Card---------------")
        for key,value in self.students.items():
            print(f'{key}   :  {value}')
        for key,value in self.marks.items():
            print(f'{key}   :  {value}')
        print('Grade :',end='')
        self.student_grade()

    def ranks(self,student):
        '''
        Method to print ranks
        '''
        stu_1=student[0]
        stu_2=student[1]
        stu_3=student[2]
        average_marks=[stu_1.average(),stu_2.average(),stu_3.average()]
        average_marks.sort()
        print(f'Ranks for high marks :\n 1 . {average_marks[0]}\n 2 . {average_marks[1]}\n 3 . {average_marks[2]}')


student_1=College('Dinesh',12,'CSE')
student_1.student_mark(89,85,78)
student_1.report_card()

student_2=College('Kumar',16,'CSE')
student_2.student_mark(80,95,78)
student_2.report_card()

student_3=College('Raman',17,'CSE')
student_3.student_mark(99,85,78)
student_3.report_card()

student=[student_1,student_2,student_3]
student_1.ranks(student)

'''
OUTPUT:
--------------Report Card---------------
Name   :  Dinesh
Rollno   :  12
Department   :  CSE
Subject 1   :  89
Subject 2   :  85
Subject 3   :  78
Grade :A Grade

--------------Report Card---------------
Name   :  Kumar
Rollno   :  16
Department   :  CSE
Subject 1   :  80
Subject 2   :  95
Subject 3   :  78
Grade :B Grade

--------------Report Card---------------
Name   :  Raman
Rollno   :  17
Department   :  CSE
Subject 1   :  99
Subject 2   :  85
Subject 3   :  78
Grade :O Grade
Ranks for high marks :
 1 . 80
 2 . 89
 3 . 99
'''


        