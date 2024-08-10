'''
Importing the necessary packages
'''
import pandas as pd
import matplotlib.pyplot as plt

class Data:

    def __init__(self):
        pass

    def load_dataset(self):
        '''
        This method is used to load the datas from the csv to pandas dataframe
        '''
        self.data=pd.read_csv('data.csv')
        return self.data
    
    def load_data_index(self):
        '''
        This method is used to display the elements with the specified index
        '''
        data=pd.read_csv('data.csv').head(3)
        df=pd.DataFrame(data,index=['Patient_1','Patient_2','Patient_3'])
        return data
    
    def get_rows(self,*args):
        '''
        This method displays the only the rows from the dataset that are passed as arguments
        '''
        row=[]
        for arg in args:
            row.append(arg)
        return self.data.loc[row]
    
    def quick_display(self,head=5):
        '''
        This method is used to display the first 5 rows
        '''
        return self.data.head(head)
    
    def quick_display_last(self):
        '''
        This method is used to display the last 5 rows
        '''
        return self.data.tail()
    
    def data_info(self):
        '''
        This method gives the info about the given dataset
        '''
        return self.data.info()
    
    def remove_empty(self):
        '''
        This method removes the empty datas from the dataset
        '''
        data=pd.read_csv('data.csv')
        new_df=data.dropna()
        return new_df
    
    def replace_empty(self):
        '''
        This method replaces the  empty data from the dataset with a particular value
        '''
        df=pd.read_csv('data.csv')
        df.fillna(490,inplace=True)
        return df
    
    def replace_empty_mean(self):
        '''
        THis method replaces the empty values with their mean value
        '''
        df=pd.read_csv('data.csv')
        mean=df['Calories'].mean()
        df['Calories']=df['Calories'].fillna(mean)
        return df
    
    def correct_date_fromat(self):
        '''
        This method is used to correct the worng dates int the dataset
        '''
        self.data['Date']=pd.to_datetime(self.data['Date'])
        self.data.dropna(subset=['Date'],inplace=True)
        return self.data
    
    def remove_wrong_data(self,choice):
        '''
        This method is used to remove or replace the wrong datas based on the condition
        '''
        match(choice):
            case 1:
                self.data.loc[7,'Duration']=45
            case 2:
                for num in self.data.index:
                    if self.data.loc[num,"Duration"]>120:
                        self.data.loc[num,'Duration']=120
            case 3:
                for num in self.data.index:
                    if self.data.loc[num,"Duration"]>120:
                        self.data.drop(num,inplace=True)
            case _:
                return f"Wrong choice"
        return self.data
            
    def identify_duplicates(self):
        '''
        This method is used to identify the duplicate elements
        '''
        df=pd.read_csv('Data.csv')
        return df.duplicated()
        
    def remove_duplicates(self):
        '''
        This method is used to remove the duplicate items
        '''
        self.data.drop_duplicates(inplace=True)

    def find_correlation(self):
        '''
        This method is used to find the correlation between the rows and return it as a dictionary
        '''
        df=pd.read_csv('data.csv')
        data=pd.DataFrame(df.corr(numeric_only=True))
        print(data)
        correlations={'Duration':{},'Pulse':{},'Maxpulse':{},'Calories':{}}
        col=list(data.columns)
        for row in data:
            for column in col:
                correlations[row][column]=data.loc[row,column]
        return correlations

    def plot(self):
        '''
        This method gives the diagrammatic or graphical view of the data set
        '''
        df=pd.read_csv('data.csv')
        df.plot()
        plt.show()
        

def main():
    '''
    Main function for the execution of the code
    '''
    data=Data()
    print(data.load_dataset())
    print(data.load_data_index())
    print(data.quick_display())
    print(data.quick_display_last())
    print(data.get_rows(3))
    print(data.data_info())
    print(data.remove_empty())
    print(data.replace_empty())
    print(data.replace_empty_mean())
    print(data.correct_date_fromat())
    print(data.remove_wrong_data(2))
    print(data.identify_duplicates())
    print(data.remove_duplicates())
    print(data.find_correlation())
    print(data.plot())

if __name__=='__main__':
    main()



    
    

        


