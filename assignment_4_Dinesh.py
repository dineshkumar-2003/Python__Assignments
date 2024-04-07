class BankAccount:                  #Parent class for bank account
    def __init__(self,otp):
        self.balance=1000
        self.otp=otp

    #Method to check the otp
    def check_otp(self):          
        '''
        This method is used to check the otp sent by the bank and the otp entered by the user is same or not
        '''      
        otp_check=int(input("Enter your otp number :"))
        if self.otp==otp_check:
            return True

    def wrong(self):
        print('OTP is wrong . Please re-enter the OTP')

    #Method to check the balance amount
    def check_balance(self):
        '''
        This method is used to check the balance of the user's account
        '''
        if self.check_otp():
            print(f'Your balance is {self.balance}')
        else:
            self.wrong()

# Child class for the BankAccount
class BankActions(BankAccount):

    #Method to deposit the money
    def deposit(self):
        '''
        This function is used to deposit the amount to the user's bank account
        After checking the otp the deposit amount is added to the user's balance
        '''
        if self.check_otp():
            amount=int(input('Enter the amount you need to deposit :'))
            self.balance+=amount
        else:
            self.wrong()

    #Method to withdraw the money
    def withdraw(self):
        '''
        This function is used to withdraw the amount from the user's bank account
        After checking the otp the withdrawal amount is deducted from the user's balance
        '''
        if self.check_otp():
            amount=int(input('Enter the amount you need to withdraw :'))
            if (amount>self.balance):
                print("Insufficient balance!")
            else:
                self.balance-=amount
        else:
            self.wrong()

#importing the random module
import random
flag=1

print("Welcome to the ATM ")

# Generating the 4 digits random number
otp=random.randint(1000,9999)
print('otp for bank operations is :',otp)

#Object creation
customer=BankActions(otp)
while(flag==1):
    print('Enter \n 1 . Check Balance \n 2 . Deposit \n 3 . Withdraw')
    choice=int(input('Enter your choice :'))
    match(choice):          # Using match case to match the given input
        case 1:
            customer.check_balance()
        case 2:
            customer.deposit()
        case 3:
            customer.withdraw()
        case _:
            print('Wrong choice')

    choice_2=int(input('Enter \n 1 . Continue \n 2 . Exit  : '))

    if(choice_2==2):
        flag=0

print('Thank You for using the ATM ! \n Welcome Again')        
    

'''
OUTPUT :
Welcome to the ATM 
otp for bank operations is : 1074
Enter
 1 . Check Balance
 2 . Deposit
 3 . Withdraw
Enter your choice :1
Enter your otp number :1074
Your balance is 1000
Enter
 1 . Continue
 2 . Exit  : 1
Enter
 1 . Check Balance
 2 . Deposit
 3 . Withdraw
Enter your choice :2
Enter your otp number :1074
Enter the amount you need to deposit :2000
Enter
 1 . Continue
 2 . Exit  : 1
Enter
 1 . Check Balance
 2 . Deposit
 3 . Withdraw
Enter your choice :1
Enter your otp number :1074
Your balance is 3000
Enter
 1 . Continue
 2 . Exit  : 1
Enter
 1 . Check Balance
 2 . Deposit
 3 . Withdraw
Enter your choice :3
Enter your otp number :200
OTP is wrong . Please re-enter the OTP
Enter
 1 . Continue
 2 . Exit  : 1
Enter
 1 . Check Balance
 2 . Deposit
 3 . Withdraw
Enter your choice :3
Enter your otp number :1074
Enter the amount you need to withdraw :3005
Insufficient balance!
Enter
 1 . Continue
 2 . Exit  : 2
Thank You for using the ATM !
 Welcome Again
'''    




