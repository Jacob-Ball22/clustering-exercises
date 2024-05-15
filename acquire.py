#Imports
import pandas as pd
import os

#Function that gets the mall_customers data from the csv file and returns it as a dataframe
def get_mall_data():
    filename = 'Mall_Customers.csv'
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename, index_col=0)
        #renames genre column to gender
        df = df.rename(columns={"Genre": "Gender"})
        return df