from Feature_Selection import feature_selection
from sklearn.model_selection import train_test_split
def data_splitting():
    dataset = feature_selection()
    x = dataset.drop(['level'], axis = 1)
    y = dataset.drop(x.columns, axis = 1)
    print(x.shape)
    print(y.shape)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state = 0)
    return x_train, x_test, y_train, y_test
data_splitting()