# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:51:53 2021

@author: IronMan
"""
import pandas as pd
data=pd.read_csv("https://raw.githubusercontent.com/edyoda/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt")

s_dict={'low':0,'medium':1,'high':2}
data['salary'].replace(s_dict,inplace=True)
data=pd.get_dummies(data,drop_first=True)

corr=data.corr()

y=data['left']
del data['left']
X=data

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=1)

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_train, y_train)

y_pred=lr.predict(X_test)
print(lr.score(X_test,y_test))
