# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:12:30 2021

@author: IronMan
"""

import pandas as pd
data=pd.read_csv("https://raw.githubusercontent.com/edyoda/data-science-complete-tutorial/master/Data/house_rental_data.csv.txt")
del data["Unnamed: 0"]

X=data.iloc[:,:-1]
y=data.iloc[:,-1]


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=57)

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)

y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))

print(lr.score(X_test,y_test))
