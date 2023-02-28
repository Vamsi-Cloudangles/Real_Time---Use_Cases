import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from Data_Preprocessing import data_preprocessing

def data_visualization():
    dataset = data_preprocessing()
    for col in dataset.columns:
        if (len(dataset[col].unique()) > 5) and (col != 'Level'):
            fig,ax = plt.subplots(1,1, figsize=(5,4))
            sns.distplot(x=dataset[col][1:])
        elif col != 'Level':
            dataset[col] != 'Level'
            fig,ax = plt.subplots(1,1, figsize = (5,4))
            sns.countplot(x=dataset[col][1:])
    sns.pairplot(dataset)
    cor_mat = dataset.corr()
    fig = plt.figure(figsize=(15,7))
    sns.heatmap(cor_mat,annot=True)
    return dataset
