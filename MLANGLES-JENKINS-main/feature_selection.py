from feature_engineering import feature_engineering
from dvc import dvc

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    print(dataset.head())
    dataset.drop(["SEX","PREGNANT","COPD","ASTHMA","INMSUPR","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO"], axis=1, inplace=True)
    print(dataset)
    return dataset




