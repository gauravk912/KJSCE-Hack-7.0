# -*- coding: utf-8 -*-
"""Cricket_RandomForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iLxWBf6X1Vjmnaseo8jWE_p1mke6LqZT
"""

import pandas as pd
# Importing the dataset
data = pd.read_csv('odi.csv')
data.head()

data = data.dropna()

X = data.iloc[:,[7,8,9,12,13]].values
y = data.iloc[:, 14].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the dataset
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=100,max_features=None)
reg.fit(X_train,y_train)

# Testing the dataset on trained model
y_pred = reg.predict(X_test)
score = reg.score(X_test,y_test)*100
print("R square value:" , score)
#print("Custom accuracy:" , custom_accuracy(y_test,y_pred,20))

# Testing with a custom input
import numpy as np
new_prediction = reg.predict(sc.transform(np.array([[100,0,13,50,50]])))
print("Prediction score:" , new_prediction)

from sklearn.model_selection import cross_val_score
#clf = svm.SVC(kernel='linear', C=1, random_state=42)
scores = cross_val_score(reg, X, y, cv=5)
scores

sdata = pd.read_csv('match_data.csv')

## Creating target variable
sdata = sdata.astype({'team_name':'string'})
sdata = sdata.astype({'team1_name':'string'})
sdata = sdata.astype({'team2_name':'string'})
sdata = sdata.astype({'match_name':'string'})
sdata = sdata.astype({'name':'string'})
## generating target variable
sdata['winner'] = np.where(
    sdata['team1_score'] > sdata['team2_score'], sdata['team1_name'], np.where(
    sdata['team2_score'] >  sdata['team1_score'], sdata['team2_name'], "Tie"))

import numpy as np
sdata['WinNum'] = np.where(
    sdata['team1_score'] > sdata['team2_score'], 1, np.where(
    sdata['team2_score'] >  sdata['team1_score'], 0, -1))

##Winner is the target variable
## selecting features to take into account
## training based on numerical data available
A = sdata.iloc[:,[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]].values
B = sdata.iloc[:, 24].values

sdata.columns

from sklearn.model_selection import train_test_split
A_train, A_test, B_train, B_test = train_test_split(A, B, test_size = 0.25, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
A_train = sc.fit_transform(A_train)
A_test = sc.transform(A_test)

# Training the dataset
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators=100,max_features=None)
reg.fit(A_train,B_train)

# Testing the dataset on trained model
B_pred = reg.predict(A_test)
score = reg.score(A_test,B_test)*100
print("R square value:" , score)
#print("Custom accuracy:" , custom_accuracy(y_test,y_pred,20))

# Testing with a custom input
import numpy as np
new_prediction = reg.predict(sc.transform(np.array([[26, 28, 5, 0, 68.65, 0, 0, 0, 0, 0, 0, 0]])))
print("Prediction score:" , new_prediction)

from sklearn.model_selection import cross_val_score
#clf = svm.SVC(kernel='linear', C=1, random_state=42)
scores = cross_val_score(reg, X, y, cv=5)
scores