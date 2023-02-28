import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
from sklearn.model_selection import train_test_split
import sklearn.linear_model as sl
lr = sl.LinearRegression()
import sklearn.tree as tree
dtr = tree.DecisionTreeRegressor()
import sklearn.ensemble as se
rfr = se.RandomForestRegressor(random_state = 42)
import sklearn.metrics as mt
import math
import pickle

# Peparing the data and loading the data
dataset = pd.read_csv("dataset.csv")

# Finding the duplicate values from the datset
duplicate = dataset[dataset.duplicated()] 

# Removing the unnecessary features from the dataset
dataset= dataset.drop(columns = 'SI.NO', axis = 1, inplace = True)

# Removing the duplicate rows from the dataset
for i in duplicate.index:
    print("index", i) 
    dataset.drop(index = [i], inplace = True)
    dataset.reset_index()

# Changing the catregorical values to numerical values
for col in dataset.select_dtypes(include="object").columns:
    dataset[col] = le.fit_transform(dataset[col])

# Setting the variables for dependent variables and independent variable
x = dataset.drop(['price'], axis = 1)
y = dataset['price']

# Splitting the data for training dataset and as well as testing dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state = 0)
s = []
model = [lr, dtr, rfr]

# Fitting the data to the different models Linear Regressor, Decission Tree Regressor and Random Forest Regressor and also finding the score
lr.fit(x_train,y_train)
lrs = lr.score(x_test, y_test)
s.append(lrs)
dtr.fit(x_train,y_train)
dtrs = dtr.score(x_test, y_test)
s.append(dtrs)
rfr.fit(x_train,y_train)
rfrs = rfr.score(x_test, y_test)
s.append(rfrs)

# Finding the best model for the 
max_score = max(s)
for i in range(len(s)):
    if s[i] == max_score :
        best_model = model[i] 
print(s)
print(best_model)
# Predict the value for best model and finding the MSE, RMSE, MAE
y_predict = best_model.predict(x_test)
MSE = mt.mean_squared_error(y_test, y_predict)
RMSE = math.sqrt(MSE)
MAE = mt.mean_absolute_error(y_test,y_predict)

# Creating the pickle file    
with open("model.pkl", 'wb') as p:
    pickle.dump(model,p)       
