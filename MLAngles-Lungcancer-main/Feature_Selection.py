from Feature_Engineering import feature_engineering
import pandas as pd
from dvc import dvc

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    dataset = dataset.drop(["patient_id", "index"], axis =1)    
    print(dataset.head())
    dataset.to_csv("cleaned.csv")
    
    dvc()

    return dataset

feature_selection()