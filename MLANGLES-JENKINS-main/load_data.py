import pandas as pd

def create_datafarme():
    dataframe = pd.read_csv("Covid_Data.csv")
    return dataframe