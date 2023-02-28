from data_analysis import data_analysis
def data_cleaning():
    dataset = data_analysis()
    dataset = dataset[(dataset.PNEUMONIA == 1) | (dataset.PNEUMONIA == 2)]
    dataset = dataset[(dataset.DIABETES == 1) | (dataset.DIABETES == 2)]
    dataset = dataset[(dataset.COPD == 1) | (dataset.COPD == 2)]
    dataset = dataset[(dataset.ASTHMA == 1) | (dataset.ASTHMA == 2)]
    dataset = dataset[(dataset.INMSUPR == 1) | (dataset.INMSUPR == 2)]
    dataset = dataset[(dataset.HIPERTENSION == 1) | (dataset.HIPERTENSION == 2)]
    dataset = dataset[(dataset.OTHER_DISEASE == 1) | (dataset.OTHER_DISEASE == 2)]
    dataset = dataset[(dataset.CARDIOVASCULAR == 1) | (dataset.CARDIOVASCULAR == 2)]
    dataset = dataset[(dataset.OBESITY == 1) | (dataset.OBESITY == 2)]
    dataset = dataset[(dataset.RENAL_CHRONIC == 1) | (dataset.RENAL_CHRONIC == 2)]
    dataset = dataset[(dataset.TOBACCO == 1) | (dataset.TOBACCO == 2)]
    return dataset

