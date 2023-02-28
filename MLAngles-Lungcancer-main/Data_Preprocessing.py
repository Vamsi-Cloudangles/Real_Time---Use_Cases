from Data_Analysis import data_analysis
def data_preprocessing():
    dataset = data_analysis()
    dataset =  dataset.rename(columns=str.lower)
    for col in dataset.columns:
        dataset = dataset.rename(columns = {col: col.replace(" ", "_")})
    print(dataset.columns)
    return dataset
data_preprocessing()
