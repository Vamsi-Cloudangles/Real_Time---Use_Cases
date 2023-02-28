import pandas as pd

data = pd.read_csv('bank.csv')
def groupby(dataset):
    cate = []
    nume = []
    for col in dataset.columns:
        if dataset[col].dtype == object:
            cate.append(col) 
        else :
            nume.append(col)
    print("Categorical columns are\n")
    print(cate)
    n = int(input("Enter Howmany columns you need to groupby in 'Categorical Columns' "))
    cate_col = list(map(str,input("Enter the names of groupby Columns from 'Categorical Columns'").strip().split()))[:n]

    print("____________________ Describe the mean _______________________")
    groupby_values = dataset.groupby(cate_col, as_index=False).mean()
    print("____________________ Describe the standard deviation _______________________")
    groupby_values = dataset.groupby(cate_col, as_index=False).std()
    print("____________________ Describe the sum of the values _______________________")
    groupby_values = dataset.groupby(cate_col, as_index=False).sum()
    print("____________________ Describe the maximum value _______________________")
    groupby_values = dataset.groupby(cate_col, as_index=False).max()
    print("____________________ Describe the minmum value _______________________")
    groupby_values = dataset.groupby(cate_col, as_index=False).min()
  
    return groupby_values
    


print(groupby(data))
