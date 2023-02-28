import pandas as pd 
read_file = pd.read_excel("Adidas US Sales Datasets.xlsx")
read_file.to_csv('Adidassales.csv', index = False, header = True)