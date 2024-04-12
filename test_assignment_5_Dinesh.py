'''
Importing necessary modules for the testing process
'''
import unittest
from assignment_5_Dinesh import SuperMarket

class Tesing(unittest.TestCase):

    def test_display_items(self):
        '''
        This function is used to test the display items function in the SuperMarket class
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertEqual(user_1.display_items(7), 'Wrong choice')

    def test_purchase_1(self):
        '''
        This function is used to test the purchase function in the SuperMarket class with assertNotEqual
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertNotEqual(user_1.purchase({'coffee':20,'tea':10,'boost':20,'horlicks':30},'coffee',3),'equal')

    def test_purchase_2(self):
        '''
        This function is used to test the purchase function in the SuperMarket class with assertEqual
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertEqual(user_1.purchase({'coffee':20,'tea':10,'boost':20,'horlicks':30},'coffe',3),'Item not available in the store')

    def test_print_dict(self):
        '''
        This function is used to test the print dict function in the SuperMarket class using assertIsNone
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertIsNone(user_1.print_dict())

    def test_is_object(self):
        '''
        This function is used to test whether user_1 is an object of the class SuperMarket
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertIsInstance(user_1,SuperMarket)

    def test_is_not_object(self):
        user_1=SuperMarket('dinesh','9659759550')
        user_2=2
        self.assertNotIsInstance(user_2,SuperMarket)

    def test_grocery_list(self):
        '''
        This function tests whether the given item is present in the list or not
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertNotIn('Potato',user_1.grocery_list)

    def test_percent(self):
        '''
        This function tests the percent function in the SuperMarket class
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertNotAlmostEqual(user_1.percent(5,20),user_1.percent(6,20))

    def test_list(self):
        '''
        This function checks whether the two lists are equal
        '''
        user_1=SuperMarket('dinesh','9659759550')
        self.assertListEqual(user_1.cafe_list,['Coffee','Tea','Boost','Horlicks'])

if __name__=='__main__':
    unittest.main()


'''
OUTPUT:
test_display_items (__main__.Tesing.test_display_items) ... The choice you selected is :7
ok
test_grocery_list (__main__.Tesing.test_grocery_list) ... ok
test_is_not_object (__main__.Tesing.test_is_not_object) ... ok
test_is_object (__main__.Tesing.test_is_object) ... ok
test_list (__main__.Tesing.test_list) ... ok
test_percent (__main__.Tesing.test_percent) ... ok
test_print_dict (__main__.Tesing.test_print_dict) ... ok
test_purchase_1 (__main__.Tesing.test_purchase_1) ... ok
test_purchase_2 (__main__.Tesing.test_purchase_2) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.005s

OK
'''