'''
Importing necessary modules for the implementation
'''
import csv
from dateutil.parser import parse
from datetime import datetime

class Csv:
    def __init__(self):
        self.male=[]
        self.female=[]
        self.employee=[]
        self.date_dict=dict()

    def read_csv(self):
        '''
        Function to read the csv file using the csv reader function and to print the name of the columns
        '''
        with open('people-1000.csv','r+',newline='') as csvfile:
            reader=csv.reader(csvfile)
            columns=[]
            rows=[]
            columns=next(reader)
            for row in reader:
                rows.append(row)
            return f'The columns are :' + ', '.join(col for col in columns)

    def number_of_rows(self):
         '''
         Function to return the number of rows available in the csv file
         '''
         with open('people-1000.csv','r+') as csvfile:
            reader_=csv.reader(csvfile)
            return f'Number of rows are: {len(list(reader_))-1}'

    def read_dict_csv(self):
        '''
        Function to read the contents of the csv file in the dictionary format and to return the dictionary
        '''
        with open('people-1000.csv','r+',newline='') as csvfile:
            reader=csv.DictReader(csvfile)
            data_list=[]
            for row in reader:
                data_list.append(row)
            return data_list

    def filter_gender(self):
        '''
        Function used to filter the people details in the csv file based on the gender and store it in separate lists
        '''
        csvfile=open('people-1000.csv','r+',newline='')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['Sex'] == 'Male':    
                self.male.append(row['First Name'])
            else:
                self.female.append(row['First Name'])

    def display_gender(self,choice):
        '''
        Function to display the list of male or female people based on the argument
        '''
        if choice=='Male' or choice=='male' or choice=='m' or choice=='M':
            return self.male
        elif choice=='Female' or choice=='female' or choice=='f' or choice=='F':
            return self.female
        else:
            return f"Wrong choice"
        
    def filter_job_role(self,job):
        '''
        Function to display the first name of people who work in a specific job
        '''
        with open('people-1000.csv','r+',newline='') as csvfile:
            csvreader=csv.DictReader(csvfile)
            count=0
            for row in csvreader:
                if row['Job Title']==job:
                    self.employee.append(row['First Name'])
                    count+=1
                else:
                    continue
            return f'The employees working in {job} are {count}:\n'+'\n'.join(name for name in self.employee)
        
    def write_csv(self,new_row):
        '''
        Function to add a new row to the csv using writer function of csv
        '''
        with open('people-1000.csv','a',newline='') as csvwriter:
            writer=csv.writer(csvwriter)
            writer.writerow(new_row)
            csvwriter.close()

    def write_csv_dict(self,new_dict_row):
        '''
        Function to add a new row to the csv using the DictWriter function
        '''
        with open('people-1000.csv','a',newline='') as csv_dict_writer:
            columns=['Index', 'User Id', 'First Name', 'Last Name', 'Sex', 'Email', 'Phone', 'Date of birth', 'Job Title']
            dict_writer=csv.DictWriter(csv_dict_writer,fieldnames=columns)
            dict_writer.writerow(new_dict_row)
            csv_dict_writer.close()

    def filter_date(self,date):
        '''
        This function is used to return the name and date greater than a specific date
        '''
        dict_list=self.read_dict_csv()
        parserinfo=None
        for row in dict_list:
            self.date_dict['First Name']=row['First Name']
            date_string=row['Date of birth']
            date_=parse(date_string,parserinfo=parserinfo)
            self.date_dict['DOB']=date_
            if date < date_:
                print(f'Name  :  {row['First Name']}           DOB   :   {date_} ' )
            else:
                continue
                 
    def get_phone_number(self,index):
        '''
        This function is used to return the name and phone number of the specified index
        '''
        dict_list=self.read_dict_csv()
        for row in dict_list:
            if row.get('Index') == index:
                return f'  Name  : {row.get('First Name')}     Phone number  : {row['Phone']}'

    def display(self,list_):
        '''
        function used to print the rows of the csv file in dictionary format
        '''
        for row in list_:
            print(row)
        
def main():
    csv_1=Csv()
    print(csv_1.read_csv())
    print(csv_1.number_of_rows())
    dict_rows=csv_1.read_dict_csv()
    csv_1.filter_gender()
    print(csv_1.display_gender('Female'))
    print(csv_1.filter_job_role('Editor, film/video'))
    csv_2=Csv()
    print(csv_2.filter_job_role('Health visitor'))
    csv_3=Csv()
    new_row=['1003','3rfdggfffg','Ram','Kumar','Male','dineshram@gmail.com','+919884548276','2013-11-23','Programmer']
    csv_3.write_csv(new_row)
    print(csv_3.number_of_rows())
    new_dict={'Index':1004, 'User Id':'ewdx5eee66dfg', 'First Name':'Noelle', 'Last Name':'Silva', 'Sex':'Female', 'Email':'blackclover2@gmail.com', 'Phone':'+43759675475', 'Date of birth':'2007-06-15', 'Job Title':'Programmer'}
    csv_3.write_csv_dict(new_dict)
    print(csv_3.filter_job_role('Programmer'))
    dict_rows_2=csv_3.read_dict_csv()
    print(csv_2.get_phone_number('1002'))
    date=datetime(2005,1,1)
    csv_3.filter_date(date)
    csv_3.display(dict_rows_2)

if __name__=='__main__':
    main()


'''
OUTPUT:

The columns are :Index, User Id, First Name, Last Name, Sex, Email, Phone, Date of birth, Job Title
Number of rows are: 1004
The employees working in Editor, film/video are 2:
Lydia
Francisco
The employees working in Health visitor are 3:
Ernest
Damon
Duane
Number of rows are: 1005
The employees working in Programmer are 6:
Dinesh
Asta
Ram
Noelle
  Name  : Asta     Phone number  : +43959759675475
Name  :  Shelia           DOB   :   2014-01-27 00:00:00
Name  :  Sheryl           DOB   :   2013-11-25 00:00:00 
Name  :  Whitney           DOB   :   2012-11-17 00:00:00
Name  :  Doris           DOB   :   2016-12-02 00:00:00
Name  :  Cheryl           DOB   :   2012-12-16 00:00:00
Name  :  Casey           DOB   :   2020-04-17 00:00:00
Name  :  Priscilla           DOB   :   2014-03-16 00:00:00
Name  :  Carly           DOB   :   2007-10-27 00:00:00
Name  :  Perry           DOB   :   2006-11-24 00:00:00
Name  :  Roger           DOB   :   2008-09-09 00:00:00
Name  :  Ethan           DOB   :   2018-07-17 00:00:00
Name  :  Catherine           DOB   :   2007-08-22 00:00:00
Name  :  Corey           DOB   :   2014-06-05 00:00:00
Name  :  Todd           DOB   :   2019-11-30 00:00:00
Name  :  Adrienne           DOB   :   2019-06-16 00:00:00
Name  :  Erik           DOB   :   2019-05-06 00:00:00
Name  :  Norma           DOB   :   2012-01-17 00:00:00
Name  :  Amy           DOB   :   2011-08-22 00:00:00
Name  :  Stephanie           DOB   :   2012-08-02 00:00:00 
Name  :  Carly           DOB   :   2006-07-28 00:00:00
Name  :  Erica           DOB   :   2018-08-01 00:00:00
Name  :  Dana           DOB   :   2020-10-22 00:00:00
Name  :  Tracie           DOB   :   2016-02-06 00:00:00
Name  :  David           DOB   :   2010-09-23 00:00:00
Name  :  Derrick           DOB   :   2020-08-21 00:00:00
Name  :  Teresa           DOB   :   2015-12-23 00:00:00
Name  :  Malik           DOB   :   2022-03-28 00:00:00
Name  :  Jesus           DOB   :   2019-10-28 00:00:00
Name  :  Jenny           DOB   :   2022-01-26 00:00:00
Name  :  Daryl           DOB   :   2010-03-11 00:00:00
Name  :  Angelica           DOB   :   2013-08-11 00:00:00
Name  :  Janice           DOB   :   2015-08-22 00:00:00
Name  :  Jimmy           DOB   :   2005-08-21 00:00:00
Name  :  Jo           DOB   :   2019-11-05 00:00:00 
Name  :  Nancy           DOB   :   2009-08-15 00:00:00
Name  :  Jennifer           DOB   :   2019-02-12 00:00:00
Name  :  Candice           DOB   :   2021-10-24 00:00:00
Name  :  Maxwell           DOB   :   2014-09-03 00:00:00
Name  :  Debra           DOB   :   2010-01-24 00:00:00
Name  :  Shane           DOB   :   2007-01-18 00:00:00
Name  :  Phillip           DOB   :   2006-12-05 00:00:00
Name  :  Lucas           DOB   :   2019-11-03 00:00:00
Name  :  Anthony           DOB   :   2021-11-10 00:00:00
Name  :  Isaiah           DOB   :   2012-08-08 00:00:00
Name  :  Clayton           DOB   :   2006-08-17 00:00:00
Name  :  Yvette           DOB   :   2006-08-14 00:00:00
Name  :  Kerri           DOB   :   2011-06-30 00:00:00
Name  :  Steven           DOB   :   2015-09-14 00:00:00 
Name  :  Dwayne           DOB   :   2011-06-13 00:00:00
Name  :  Marc           DOB   :   2018-04-04 00:00:00
Name  :  Kristin           DOB   :   2007-09-04 00:00:00
Name  :  Emily           DOB   :   2014-10-17 00:00:00
Name  :  Edward           DOB   :   2008-05-20 00:00:00
Name  :  Hector           DOB   :   2013-10-11 00:00:00
Name  :  Hunter           DOB   :   2008-12-29 00:00:00
Name  :  Jonathan           DOB   :   2005-05-29 00:00:00
Name  :  Randall           DOB   :   2012-01-31 00:00:00
Name  :  Earl           DOB   :   2015-08-25 00:00:00
Name  :  Heather           DOB   :   2010-08-11 00:00:00
Name  :  Robyn           DOB   :   2007-03-07 00:00:00
Name  :  Susan           DOB   :   2021-09-17 00:00:00
Name  :  Tommy           DOB   :   2020-11-19 00:00:00
Name  :  Bryce           DOB   :   2018-04-07 00:00:00 
Name  :  Natalie           DOB   :   2008-12-27 00:00:00
Name  :  Sarah           DOB   :   2018-09-28 00:00:00
Name  :  Dustin           DOB   :   2019-05-18 00:00:00
Name  :  Regina           DOB   :   2006-02-20 00:00:00
Name  :  Kathleen           DOB   :   2021-08-09 00:00:00
Name  :  Caitlyn           DOB   :   2007-02-24 00:00:00
Name  :  Peggy           DOB   :   2021-10-22 00:00:00
Name  :  Melinda           DOB   :   2010-03-13 00:00:00 
Name  :  Melissa           DOB   :   2021-01-18 00:00:00
Name  :  Melvin           DOB   :   2013-06-14 00:00:00
Name  :  Kaylee           DOB   :   2014-06-19 00:00:00
Name  :  Gina           DOB   :   2021-09-13 00:00:00
Name  :  Alex           DOB   :   2015-07-24 00:00:00
Name  :  Shelia           DOB   :   2008-07-26 00:00:00
Name  :  Dominic           DOB   :   2016-06-26 00:00:00
Name  :  Alex           DOB   :   2021-02-28 00:00:00
Name  :  Allen           DOB   :   2010-03-08 00:00:00
Name  :  Dakota           DOB   :   2005-04-12 00:00:00
Name  :  Darren           DOB   :   2012-06-07 00:00:00
Name  :  Darryl           DOB   :   2009-07-08 00:00:00
Name  :  Maxwell           DOB   :   2013-11-11 00:00:00
Name  :  Nicole           DOB   :   2006-03-07 00:00:00 
Name  :  Gail           DOB   :   2009-03-07 00:00:00
Name  :  Jade           DOB   :   2021-02-15 00:00:00
Name  :  Ross           DOB   :   2021-07-07 00:00:00
Name  :  Breanna           DOB   :   2015-07-26 00:00:00
Name  :  Wyatt           DOB   :   2012-02-27 00:00:00
Name  :  Kenneth           DOB   :   2019-10-18 00:00:00
Name  :  Jody           DOB   :   2017-03-19 00:00:00
Name  :  Vickie           DOB   :   2016-03-20 00:00:00
Name  :  George           DOB   :   2005-02-21 00:00:00
Name  :  Kelly           DOB   :   2016-09-06 00:00:00 
Name  :  Troy           DOB   :   2014-05-26 00:00:00
Name  :  Norman           DOB   :   2017-09-27 00:00:00
Name  :  Vernon           DOB   :   2014-04-20 00:00:00
Name  :  Sarah           DOB   :   2006-11-04 00:00:00
Name  :  Jo           DOB   :   2011-08-21 00:00:00
Name  :  Caitlin           DOB   :   2011-03-23 00:00:00
Name  :  Peggy           DOB   :   2011-12-28 00:00:00
Name  :  Mariah           DOB   :   2011-08-27 00:00:00
Name  :  Leon           DOB   :   2018-12-02 00:00:00
Name  :  Anthony           DOB   :   2008-12-26 00:00:00
Name  :  Alejandra           DOB   :   2005-10-11 00:00:00
Name  :  Tara           DOB   :   2016-06-18 00:00:00
Name  :  Leah           DOB   :   2015-01-15 00:00:00
Name  :  Lorraine           DOB   :   2012-07-21 00:00:00
Name  :  Joanna           DOB   :   2018-09-20 00:00:00 
Name  :  Lonnie           DOB   :   2015-05-12 00:00:00
Name  :  Leonard           DOB   :   2012-08-25 00:00:00
Name  :  Arthur           DOB   :   2017-03-30 00:00:00
Name  :  Gina           DOB   :   2007-07-23 00:00:00
Name  :  Jenna           DOB   :   2022-03-05 00:00:00
Name  :  Darren           DOB   :   2012-09-14 00:00:00
Name  :  Mandy           DOB   :   2019-04-27 00:00:00
Name  :  Whitney           DOB   :   2020-11-02 00:00:00
Name  :  Julian           DOB   :   2006-10-16 00:00:00
Name  :  Mason           DOB   :   2010-12-28 00:00:00
Name  :  Kristen           DOB   :   2016-10-13 00:00:00
Name  :  Lawrence           DOB   :   2013-05-01 00:00:00
Name  :  Garrett           DOB   :   2008-10-08 00:00:00 
Name  :  Annette           DOB   :   2013-05-30 00:00:00
Name  :  Xavier           DOB   :   2009-06-05 00:00:00
Name  :  Eduardo           DOB   :   2014-03-29 00:00:00
Name  :  Caleb           DOB   :   2020-12-29 00:00:00
Name  :  Krista           DOB   :   2016-03-12 00:00:00
Name  :  Sonya           DOB   :   2016-09-13 00:00:00
Name  :  Toni           DOB   :   2012-05-02 00:00:00
Name  :  Fred           DOB   :   2010-01-29 00:00:00
Name  :  Laura           DOB   :   2013-01-17 00:00:00
Name  :  Jaclyn           DOB   :   2012-01-09 00:00:00
Name  :  Sonia           DOB   :   2006-04-03 00:00:00
Name  :  Rebecca           DOB   :   2015-06-26 00:00:00
Name  :  Cristina           DOB   :   2020-04-28 00:00:00
Name  :  Marco           DOB   :   2008-11-02 00:00:00
Name  :  Suzanne           DOB   :   2021-08-21 00:00:00
Name  :  Joshua           DOB   :   2017-04-23 00:00:00
Name  :  Marie           DOB   :   2010-09-18 00:00:00 
Name  :  Charles           DOB   :   2012-06-17 00:00:00
Name  :  Evelyn           DOB   :   2011-07-10 00:00:00
Name  :  Karla           DOB   :   2015-05-25 00:00:00
Name  :  Johnny           DOB   :   2009-01-09 00:00:00
Name  :  Emma           DOB   :   2018-10-05 00:00:00
Name  :  Daryl           DOB   :   2011-01-27 00:00:00
Name  :  Victor           DOB   :   2019-08-30 00:00:00
Name  :  Jon           DOB   :   2012-01-03 00:00:00
Name  :  Dorothy           DOB   :   2017-09-07 00:00:00
Name  :  Derrick           DOB   :   2005-01-23 00:00:00
Name  :  Greg           DOB   :   2006-02-26 00:00:00
Name  :  Ram           DOB   :   2013-11-23 00:00:00 
Name  :  Noelle           DOB   :   2007-06-15 00:00:00
Name  :  Ram           DOB   :   2013-11-23 00:00:00
Name  :  Noelle           DOB   :   2007-06-15 00:00:00
.........
'''