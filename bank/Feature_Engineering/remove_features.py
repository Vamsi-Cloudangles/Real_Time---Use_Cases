import pandas as pd



def removing_features(dataframe):
    print(dataframe.head())
    
    len = int(input("How many features you need to remove"))
    col = list(map(str,input("\n Enter the Unwanted Columns : ").strip().split()))[:len]
    print('\n')    
    dataframe.drop(col, axis = 1) 
    return dataframe

dataset = pd.read_csv('bank.csv')
dataset = removing_features(dataset)
print(dataset)