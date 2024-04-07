from bs4 import BeautifulSoup
import math
import datetime
import random

class SuperMarket:

    def __init__(self,name,mobile_no):
        self.name=name
        self.mobile_no=mobile_no
        self.finalamount=0
        self.discount_amount=0
        self.bill_list={}
        self.grocery_list={}

    def services_available(self):
        '''
        Displaying all the services available in the super market
        '''
        services={'Grocery store','Cloth store','Jewellery store','Fashion store','Cafe'}
        return f'The services available are {services} \n Select \n1 . Grocery store \n2 . Cloth store \n3 . Jewellery store \n4 . Cafe'
    
    def initialize(self):
        '''
        Initializing the values for the items available in the super market
        '''
        self.grocery_list={'Dhal':5,'rice':10,'wheat':7,'Rice flour':12}
        self.cloth_list=['Shirt','Pant','Lowers','Saree','Chudi']
        self.jewel_list=('gold','silver','platinum')
        self.cafe_list=['Coffee','Tea','Boost','Horlicks']

    def grocery_store(self,item,quantity=1): 
        '''
        Method for purchasing items from the grocery store
        '''
        grocery_amount={'dhal':120,'rice':80,'wheat':70,'rice flour':50}
        self.purchase(grocery_amount,item,quantity)
    
    def cloth_store(self,item,quantity=1):
        '''
        Method for purchasing items from the cloth store
        '''
        cloth_price={'shirt':500,'pant':800,'lowers':300,'saree':600,'chudi':800}
        self.purchase(cloth_price,item,quantity)

    def jewellery_store(self,item,grams=1):
        '''
        Method for purchasing items from the jewellery store
        '''
        jewel_price={'gold':6390,'silver':80.80,'platinum':2433}
        self.purchase(jewel_price,item,grams)
    
    def cafe(self,item,quantity=1):
        '''
        Method for purchasing items from the Cafe
        '''
        cafe_price={'coffee':20,'tea':10,'boost':20,'horlicks':30}
        self.purchase(cafe_price,item,quantity)

    def display_items(self,choice):
        '''
        Function for displaying the items available in the shops using the match case statement
        '''
        print(f"The choice you selected is :{choice}")
        match(choice):
            case 1:
                return self.grocery_list
            case 2:
                return self.cloth_list
            case 3:
                return self.jewel_list
            case 4:
                return self.cafe_list
            case _:
                return f'Wrong choice'

    def add_value(self,list_name,new_value,key=0):
        '''
        Method to add the items to the items list based on their type [list , set , dictionary] 
        '''
        if type(list_name) is list:
            list_name.append(new_value)
            return list_name
        elif type(list_name) is set:
            list_name.add(new_value)
            return list_name
        elif type(list_name) is dict:
            list_name[new_value]=key
            return list_name
        
    def delete_value(self,list_,value):
        '''
        Method to delete the value in the items list based on their type [list,set, dictionary] using isinstance
        '''
        if isinstance(list_,list):
            list_.remove(value)
            return list_
        elif isinstance(list_,set):
            list_.discard(value)
            return list_
        elif isinstance(list_,dict):
            list_.pop(value)
            return list_
    
    def purchase(self,list_,item,quantity=1):
        '''
        Method to purchase the items from the store and to calculate the bill and final amount
        '''
        if item.lower() in list_.keys():
            self.finalamount+=list_[item]*quantity
            self.bill_list[item]=list_[item]*quantity
        else:
            return f"Item not available in the store"
    
    def print_dict(self):
        for key,value in self.bill_list.items():
            print(f'{key}         :     {value}')

    def percent(self,a,b):
        return (a/100)*b
    
    def discount(self):
        '''
        Method to calculate the discount amount for the bill
        '''
        if self.finalamount>2000:
            self.discount_amount=self.percent(5,self.finalamount)
        elif self.finalamount>3000:
            self.discount_amount=self.percent(7,self.finalamount)
        elif self.finalamount>5000:
            self.discount_amount=self.percent(10,self.finalamount)
        elif self.finalamount>7000:
            self.discount_amount=self.percent(15,self.finalamount)
        return self.discount_amount
    
    def online(self):
        '''
        displaying the item from the online for grocery store
        '''
        big_data=open('D:/Python_Assignments/Python__Assignments/bigbasket.html','+r')
        soup=BeautifulSoup(big_data.read(),'html.parser')
        product_info=soup.find(class_='Description___StyledH-sc-82a36a-2 bofYPK')
        actual_price=soup.find(class_='line-through p-0').get_text()
        discounted_price=soup.find(class_='Description___StyledTd-sc-82a36a-4 fLZywG').get_text()
        return f"Product name :{product_info.get_text() }\n Actual price :{actual_price} \n Discounted Price:{discounted_price}"

    def bill(self):
        '''
        Method to print the bill amount ,discount amount and final ampunt payable
        '''
        print('__________________________________________________________________________________________')
        self.print_dict()
        print(datetime.datetime.now())
        return f'NAME : {self.name} \nMOBILE NO : {self.mobile_no} \nFINAL AMOUNT : {self.finalamount} \nDISCOUNT AMOUNT : {self.discount_amount} \n\nFINAL AMOUNT TO BE PAYED :{math.ceil(self.finalamount-self.discount_amount)}'
    
    def lucky_draw(self,users):
        '''
        Providing lucky draw for single user by passing the objects as parameter
        '''
        select=random.choice(users)
        return f'The lucky customer who receive the gift is {select.name}'


#Creating first object for SuperMarket
user_1=SuperMarket('Dinesh','9384548176')
user_1.initialize()
print(user_1.services_available())
print(user_1.display_items(1))
user_1.grocery_store('dhal',2)
user_1.cloth_store('shirt',2)
user_1.jewellery_store('platinum',0.5)
user_1.cafe('coffee',1)
user_1.discount()
print(user_1.bill())
user_1.cafe_list=user_1.add_value(user_1.cafe_list,'Ginger tea')
print(user_1.display_items(4))
user_1.cafe_list=user_1.delete_value(user_1.cafe_list,'Horlicks')
print(user_1.display_items(4))

#Creating second object for SuperMarket
user_2=SuperMarket('Raman','9659759550')
user_2.initialize()
user_2.grocery_store('rice',20)
user_2.cafe('tea',4)
user_2.cloth_store('shirt',5)
user_2.cloth_store('pant',3)
user_2.discount()
print(user_2.bill())

#Creating third object for SuperMarket
user_3=SuperMarket('kumar','9659759550')
user_3.initialize()
user_3.grocery_store('rice flour',20)
user_3.cafe('boost',4)
user_3.jewellery_store('gold',5)
user_3.cloth_store('saree',3)
user_3.discount()
print(user_3.bill())

users=[user_1,user_2,user_3]
print(user_1.lucky_draw(users))   #Passing objects as parameter to the method

print(user_1.online())


'''
OUTPUT :
The services available are {'Grocery store', 'Cloth store', 'Fashion store', 'Jewellery store', 'Cafe'} 
 Select
1 . Grocery store
2 . Cloth store
3 . Jewellery store
4 . Cafe
The choice you selected is :1
{'Dhal': 5, 'rice': 10, 'wheat': 7, 'Rice flour': 12}
__________________________________________________________________________________________
dhal         :     240
shirt         :     1000
platinum         :     1216.5
coffee         :     20
2024-04-02 20:33:43.366825
NAME : Dinesh
MOBILE NO : 9384548176
FINAL AMOUNT : 2476.5
DISCOUNT AMOUNT : 123.825

FINAL AMOUNT TO BE PAYED :2353
The choice you selected is :4
['Coffee', 'Tea', 'Boost', 'Horlicks', 'Ginger tea']
The choice you selected is :4
['Coffee', 'Tea', 'Boost', 'Ginger tea']
__________________________________________________________________________________________
rice         :     1600
tea         :     40
shirt         :     2500
pant         :     2400
2024-04-02 20:33:43.377949
NAME : Raman
MOBILE NO : 9659759550
FINAL AMOUNT : 6540
DISCOUNT AMOUNT : 327.0

FINAL AMOUNT TO BE PAYED :6213
__________________________________________________________________________________________
rice flour         :     1000
boost         :     80
gold         :     31950
saree         :     1800
2024-04-02 20:33:43.381322
NAME : kumar
MOBILE NO : 9659759550
FINAL AMOUNT : 34830
DISCOUNT AMOUNT : 1741.5

FINAL AMOUNT TO BE PAYED :33089
The lucky customer who receive the gift is Raman
Product name :Fresho Carrot - Orange (Loose), 1 kg 
 Actual price :84.93
 Discounted Price:Price: 44
'''