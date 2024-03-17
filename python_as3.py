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





        