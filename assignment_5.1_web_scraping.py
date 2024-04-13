'''
Importing the necessary packages for web scraping
'''
from bs4 import BeautifulSoup
import requests 
import pandas as pd

class WebScraping:

    def __init__(self):
        pass
    
    def get_html_content(self):        
        '''
        This function uses the requests module to get the html contents of the web page
        '''
        url='https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        try:
            self.response=requests.get(url)
            self.response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return 'Error occured',e
        
    def get_product_name(self):
        '''
        This function is used to get the product name of all the laptops in the web page
        '''
        self.soup=BeautifulSoup(self.response .content,'html.parser')
        self.product_name=self.soup.findAll('div',class_='_4rR01T')
        # print(len(self.product_name))
        if self.product_name:
            print(f'Product Name  : {self.product_name[0].text}')
        else:
            print('Error !!  Product name not found')
        # for ele in product_name:
        #     print(ele.text)

    def get_original_price(self):
        '''
        This function is used to get the original price of all the laptops in the web page
        '''
        self.original_price=self.soup.findAll('div',class_='_3I9_wc _27UcVY')
        # print(len(self.original_price))
        if self.original_price:
            print(f'Original Price  : {self.original_price[0].text}')
        else:
            print('Error !! Price not found')
        # for ele in original_price:
        #     print(ele.text)

    def get_discounted_price(self):
        '''
        This function is used to get the discounted price of all the laptops in the web page
        '''
        self.discounted_price=self.soup.findAll('div',class_='_30jeq3 _1_WHN1')
        # print(len(self.discounted_price))
        if self.discounted_price:
            print(f'Discounted price  : {self.discounted_price[0].text}')
        else:
            print('Error !!  Discounted price not found')
        # for ele in product_name:
        #     print(ele.text)

    def get_ratings(self):
        '''
        This function is used to get the product ratings of all the laptops in the web page
        '''
        self.ratings=self.soup.findAll('div',class_='_3LWZlK')
        # print(len(self.ratings))
        if self.ratings :
            print(f' Ratings   : {self.ratings [0].text}')
        else:
            print('Error !!  Ratings not found') 

    def get_specifications(self):
        '''
        This function is used to get the specifications of all the laptops in the web page
        '''
        self.specs=self.soup.find_all('ul',class_='_1xgFaf')
        if self.specs:
                print('Specifications :')
                for ele in self.specs[0]:
                    print(ele.text)
        else:
            print("Error !! Specifications not found")

    def laptop_page(self):
        '''
        This function is used to navigate to the laptop page which is selected
        '''
        web_link='https://www.flipkart.com'
        link=self.soup.find('a',class_='_1fQZEK')
        if link:
            self.next_link=web_link+link['href']

    def get_laptop_page(self):
        '''
        This function is used to get the html content of the selected laptop page
        '''
        try:
            self.response_2=requests.get(self.next_link)
            self.response_2.raise_for_status()
            # print(self.next_link)
        except requests.exceptions.RequestException as e:
            return 'Error occured',e
        
    def offers(self):
        '''
        This fuction is used to get the offers available for the laptop
        '''
        if self.response_2.status_code == 200:
            self.next_soup=BeautifulSoup(self.response_2.content,'html.parser')
        else:
            print('Error occoured next page not found')
        offer=self.next_soup.find('div',class_='_3TT44I')
        if offer:
            for item in offer:
                print(item.text)
        else:
            print('Offers not available')

    def highlights(self):
        '''
        This function is used to get the highlights of the selected laptop
        '''
        highlight=self.next_soup.find('div',class_='_2418kt')
        if highlight:
            print('Highlights :')
            for item in highlight:
                print(item.text)
        else:
            print("Erroe highlight not found")

    def display_as_table(self):
        '''
        This function is used to display the info of the laptop in the table format
        '''
        dict={'Name':self.product_name , 'Original Price':self.original_price,'Discounted price':self.discounted_price}
        df=pd.DataFrame(dict)
        print(df)
        
    def initialize_search_page(self):
        '''
        This function initializes the functions for getting the details from the search page
        '''
        self.get_html_content()
        self.get_product_name()
        self.get_original_price()
        self.get_discounted_price()
        self.get_ratings()
        self.get_specifications()

    def initialize_laptop_page(self):
        '''
        This function initializes the functions for getting the details from the selected laptop page
        '''
        self.laptop_page()
        self.get_laptop_page()
        self.offers()
        self.highlights()


web=WebScraping()
web.initialize_search_page()
web.initialize_laptop_page()
web.display_as_table()

web_1=WebScraping()
web_1.initialize_search_page()



'''
OUTPUT :
Product Name  : Acer Aspire 3 Intel Core i3 12th Gen 1215U - (8 GB/512 GB SSD/Windows 11 Home) A315-59-36HE Thin and L...
Original Price  : ₹44,100
Discounted price  : ₹29,990
 Ratings   : 4.6
Specifications :
Intel Core i3 Processor (12th Gen)
8 GB DDR4 RAM
Windows 11 Operating System
512 GB SSD
39.62 cm (15.6 inch) Display
1 Year Onsite Warranty
Bank Offer5% Cashback on Flipkart Axis Bank CardT&C
Bank Offer10% off on Citi-branded Credit Card EMI Transactions, up to ₹2,000 on orders of ₹5,000 and aboveT&C
Bank OfferFlat ₹1,250 off on HDFC Bank Credit Card EMI Txns on 6 and 9 months tenure, Min. Txn Value: ₹15,000T&C
Special Price Get extra 6% off (price inclusive of cashback/coupon)T&CView 25 more offers
Highlights :
Thin and Light Laptop15.6 inch Full HD
                                                 Name  Original Price Discounted price
0   [Acer Aspire 3 Intel Core i3 12th Gen 1215U - ...  [₹,  , 44,100]        [₹29,990]
1   [Infinix X3 Slim Intel Intel Core i3 12th Gen ...  [₹,  , 54,990]        [₹29,990]
2   [Infinix INBook X2 Plus Intel Core i3 11th Gen...  [₹,  , 36,470]        [₹25,990]
3   [HP 15s Intel Core i3 12th Gen 1215U - (8 GB/5...  [₹,  , 56,260]        [₹37,290]
4   [DELL Intel Core i3 12th Gen 1215U - (8 GB/512...  [₹,  , 51,335]        [₹34,990]
5   [Lenovo V15 AMD Ryzen 3 Quad Core 7320U - (8 G...  [₹,  , 39,157]        [₹27,990]
6   [MSI GF63 Intel Core i5 11th Gen 11260H - (16 ...  [₹,  , 70,990]        [₹43,990]
7   [CHUWI Intel Celeron Quad Core 12th Gen N100 -...  [₹,  , 34,990]        [₹18,990]
8   [HP 255 G9 AMD Ryzen 3 Dual Core R3 3250 - (8 ...  [₹,  , 37,188]        [₹25,490]
9   [Apple 2020 Macbook Air Apple M1 - (8 GB/256 G...  [₹,  , 99,900]        [₹73,990]
10  [ASUS Vivobook S 14 Intel EVO H-Series Intel C...  [₹,  , 86,990]        [₹61,990]
11  [ASUS Vivobook 15 Intel Core i3 12th Gen 1215U...  [₹,  , 56,990]        [₹35,990]
12  [Lenovo V15 Series AMD Athlon Dual Core 7120U ...  [₹,  , 38,000]        [₹24,162]
13  [walker Intel Celeron Dual Core N4020 - (4 GB/...  [₹,  , 30,000]        [₹12,990]
14  [Lenovo IdeaPad Slim 3 Intel Core i5 12th Gen ...  [₹,  , 76,890]        [₹47,990]
15  [Acer Aspire 7 Intel Core i5 12th Gen 12450H -...  [₹,  , 83,999]        [₹52,990]
16  [HP Intel Core i5 12th Gen 1235U - (16 GB/512 ...  [₹,  , 68,223]        [₹52,990]
17  [Lenovo IdeaPad Slim 3 Intel Core i5 13th Gen ...  [₹,  , 81,890]        [₹59,390]
18  [ASUS Vivobook 15 Intel Core i3 11th Gen 1115G...  [₹,  , 44,990]        [₹28,990]
19  [MSI GF63 Intel Core i5 11th Gen 11260H - (16 ...  [₹,  , 84,990]        [₹50,990]
20  [ASUS Vivobook 15 Intel Core i5 12th Gen 1235U...  [₹,  , 74,990]        [₹51,990]
21  [HP 2023 Intel Core i3 12th Gen 1215U - (8 GB/...  [₹,  , 51,266]        [₹34,990]
22  [HP 255 G9 AMD Ryzen 3 Dual Core AMD Ryzen3 32...  [₹,  , 44,912]        [₹25,740]
23  [Lenovo V15 Intel Celeron Dual Core 4th Gen - ...  [₹,  , 42,032]        [₹21,990]
Product Name  : CHUWI Intel Celeron Quad Core 12th Gen N100 - (8 GB/256 GB SSD/Windows 11 Home) GemiBook X_Pro Laptop
Original Price  : ₹34,990
Discounted price  : ₹18,990
 Ratings   : 3.9
Specifications :
Intel Celeron Quad Core Processor (12th Gen)
8 GB LPDDR5 RAM
64 bit Windows 11 Home Operating System
256 GB SSD
35.81 cm (14.1 inch) Display
WPS Office, Operating System Software
1 Year Onsite Warranty
'''