from feature_engineering import feature_engineering
import pandas as pd

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    dataset = dataset.drop(["SEX","PREGNANT","COPD","ASTHMA","INMSUPR","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO"],axis = 1, inplace=True)
    print(dataset.head())
    return dataset

feature_selection()