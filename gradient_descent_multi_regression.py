# -*- coding: utf-8 -*-
"""Gradient_descent multi regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tPk9jTZKNv9a7lxt8_vaNgVxEm3eAXDG
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

startup = pd.read_excel('/content/50_StartUp.xlsx')
df = startup.copy()
df

df.info()

df.shape

df.isnull().sum()

df.describe().T

df['State'].unique()

sns.scatterplot(x='R&D Spend', y ='Profit', data =df ,color = 'red')

df.hist(figsize=(12,6))

df

dfDummies=pd.get_dummies(df['State'],prefix ='State',dtype = int)
dfDummies

df = pd.concat([df,dfDummies],axis=1)
df

df=df.drop('State',axis=1)

df=df.drop('State_New York',axis= 1)
df

x=df.drop('Profit',axis=1)
y = df['Profit']

y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 35)

X_test

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

model = lm.fit(X_train, y_train)

y_predict = model.predict(X_test)

df= pd.DataFrame({'y_test':y_test,'y_predict':y_predict, 'diff':abs(y_predect-y_test)})
df

from sklearn.metrics import mean_absolute_error
mae= mean_absolute_error(y_test,y_predict)
mae

rmae= np.sqrt(mae)
rmae

df1 =startup.head(10)
df1.plot(kind='bar',figsize=(12,6))
plt.grid(which="major",linestyle="-", linewidth="0.5",color="green")
plt.show()

print('Intercept of the model:\n',lm.intercept_)
print("="*50)
print('Coefficient of the line:\n',lm.coef_)

print('intercept:\n',lm.intercept_)

import statsmodels.api as sm
stmodel = sm.OLS(y,x).fit()
stmodel.summary()

x=sm.add_constant(x)
##to add y-intercept(b)    y = wx+b
model=sm.OLS(y,x).fit()
model.summary()

x=x.drop(['State_California'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

x=x.drop(['State_Florida'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

model=sm.OLS(y,x).fit()
model.summary()

x=x.drop(['Marketing Spend'],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

x=x.drop(["Administration"],axis=1)
model=sm.OLS(y,x).fit()
model.summary()

from sklearn.preprocessing import StandardScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = StandardScaler()
s.fit_transform(data)

from sklearn.preprocessing import MinMaxScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = MinMaxScaler()
s.fit_transform(data)

from sklearn.preprocessing import RobustScaler
data = [[0,61],[0,62],[1,63],[1,64]]
s = RobustScaler()
s.fit_transform(data)

from sklearn.preprocessing import normalizer
data = [[0,61],[0,62],[1,63],[1,64]]
s = normalizer()
s.fit_transform(data)



x=x.drop([''])