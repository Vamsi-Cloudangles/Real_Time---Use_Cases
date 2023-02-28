from feature_engineering import feature_engineering
from sklearn.model_selection import train_test_split
from imblearn import over_sampling as ovrs
def data_preprocessing():
    dataset = feature_engineering()
    x = dataset.drop(['DEATH'], axis = 1)
    y = dataset.drop(x.columns, axis = 1)
    print(x.shape)
    print(y.shape)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state = 0)
    distnict = dataset["DEATH"].value_counts()
    print(distnict)
    ros = ovrs.RandomOverSampler(sampling_strategy=1)
    x_train, y_train = ros.fit_resample(x_train, y_train)
    print(y_train["DEATH"].value_counts())
    print(x_train.shape)
    print(y_train.shape)
    return x_train, x_test, y_train, y_test