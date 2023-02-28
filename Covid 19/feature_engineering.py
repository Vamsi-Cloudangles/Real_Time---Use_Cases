from data_cleaning import data_cleaning
def feature_engineering():
    dataset = data_cleaning()
    for col in dataset.columns:
        print(col, len(dataset[col].unique()))
    # Rename the "DATE_DIED" column to "DEATH" and make "9999-99-99" as alive(1) and others as dead(2)
    dataset['DEATH'] = [2 if val == '9999-99-99' else 1 for val in dataset['DATE_DIED']]
    dataset.drop(['DATE_DIED'], axis = 1, inplace = True)
    print(dataset.head())
    return dataset
