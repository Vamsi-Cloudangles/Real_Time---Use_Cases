import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

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

dataset = pd.read_csv("dimond.csv")


# In[3]:


dataset.head()


# In[4]:


dataset.columns


# In[5]:


dataset.duplicated().sum()


# In[6]:


dataset.isnull().sum()


# In[7]:


dataset.drop(columns = 'SI.NO', axis = 1, inplace = True)


# In[8]:


dataset.head()


# In[9]:


dataset.info()


# In[10]:


dataset.shape


# In[11]:


dataset['volume'] = dataset.x * dataset.y * dataset.z


# In[12]:


dataset.describe()


# In[13]:


dataset.dtypes


# In[14]:


cat_fea = []
num_fea = []

for feature in dataset.columns:
    if ((dataset[feature].dtypes=='O') & (feature not in 'price')):
        cat_fea.append(feature)
    elif(feature not in 'price'):
        num_fea.append(feature)

print(cat_fea)
print(num_fea)


# In[15]:


for col in dataset.select_dtypes(include="object").columns:
    dataset[col] = le.fit_transform(dataset[col])


# In[16]:


dataset.head()


# In[17]:


dataset.hist(cat_fea)


# In[18]:


dataset.hist(num_fea)


# In[19]:


sns.scatterplot(x=dataset.carat , y=dataset.price)


# In[20]:


sns.pairplot(dataset)


# In[21]:


corr = dataset.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, cmap='RdBu', annot = True, fmt=".2f")
plt.xticks(range(len(corr.columns)), corr.columns);
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()


# In[22]:


plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
sns.boxplot(dataset.price, color= 'skyblue')
plt.title('Box Plot of Price')

plt.subplot(1,2,2)
sns.distplot(a = dataset.price, color='darkred')
plt.title('Distribution Plot of Price')
plt.show()


# In[23]:


x = dataset.drop(['price'], axis = 1)
x.head()


# In[24]:


y = dataset['price']
y.head()


# In[25]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)


# In[26]:


print(x_train.shape)
print(y_train.shape)


# In[27]:


print(x_test.shape)
print(y_test.shape)


# In[28]:


lr.fit(x_train, y_train)
print("The Score of a Linear Regression model for the Training dataset is: ",lr.score(x_train, y_train))
print("The Score of a Linear Regression model for the Test dataset is: ",lr.score(x_test, y_test))


# In[29]:


y_predict = lr.predict(x_test)
sns.scatterplot(x=y_test, y=y_predict, color="orange")


# In[30]:


dtr.fit(x_train, y_train)
print("The Score of a Decision Tree Regressor model for the Training dataset is: ",dtr.score(x_train, y_train))
print("The Score of a Decision Tree Regerssor model for the Test dataset is: ",dtr.score(x_test, y_test))


# In[31]:


y_predict1 = dtr.predict(x_test)
sns.scatterplot(x=y_test , y=y_predict, color="blue")


# In[32]:


rfr.fit(x_train, y_train)
print("The Score of a Random Forest Regressor model for the Training dataset is: ",rfr.score(x_train, y_train))
print("The Score of a Random Forest Regerssor model for the Test dataset is: ",rfr.score(x_test, y_test))

y_predict2 = rfr.predict(x_test)
sns.scatterplot(x=y_test , y=y_predict2, color="green")

d = {'true': y_test, 'predicted': y_predict}
df_lr = pd.DataFrame(data=d)
df_lr['diff'] = df_lr['predicted']-df_lr['true']
df_lr
sns.displot(x = y_predict, y = y_test, color='blue')
mse = mt.mean_squared_error(y_test, y_predict)
print("Linear Regression")
print("Mean Absolute Error : ", mt.mean_absolute_error(y_test,y_predict))
print("Mean Squred Error : ", mse)
print("Root Mean Square Error : ", math.sqrt(mse))
plt.hist(y_predict[y_predict < 0 ])

d = {'true': y_test, 'predicted': y_predict1}
df_dtr = pd.DataFrame(data=d)
df_dtr['diff'] = df_dtr['predicted']-df_dtr['true']
df_dtr
sns.displot(x = y_predict1, y = y_test, color='orange')
mse1 = mt.mean_squared_error(y_test, y_predict1)
print("Decision Regression")
print("Mean Absolute Error : ", mt.mean_absolute_error(y_test,y_predict1))
print("Mean Squred Error : ", mse)
print("Root Mean Square Error : ", math.sqrt(mse1))

d = {'true': y_test, 'predicted': y_predict2}
df_rfr = pd.DataFrame(data=d)
df_rfr['diff'] = df_rfr['predicted']-df_rfr['true']
df_rfr
sns.displot(x = y_predict2, y = y_test, color='green')
mse2 = mt.mean_squared_error(y_test, y_predict2)
print("Random Forest Regression")
print("Mean Absolute Error : ", mt.mean_absolute_error(y_test,y_predict1))
print("Mean Squred Error : ", mse)
print("Root Mean Square Error : ", math.sqrt(mse1))

model = rfr
model

with open("dimond_pickle.pkl", 'wb') as p:
     pickle.dump(model,p)

pf = open('dimond_pickle.pkl', 'rb')
lp = pickle.load(pf)

dataset.head()

lp.predict([[0.21,3,1,2,59.8,61.0,3.89,3.84,2.31, 38.505856]])
