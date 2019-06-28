#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:05:19 2019

@author: ajay
"""
import pandas as pd
#import matplotlib.pyplot as plt
import Preprocessing
data = pd.read_csv("/home/ajay/Documents/LTFS DATASET/train_aox2Jxw/train.csv")
data_index = data['UniqueID']
dependentVar = data['loan_default']
data = data.drop(['loan_default'], axis = 1)

testData = pd.read_csv('/home/ajay/Documents/LTFS DATASET/test_bqCt9Pv.csv')
testData_index = testData['UniqueID']

dataForPreprocessing = pd.concat([data, testData])
preprocessed_data = Preprocessing.preproccesing(dataForPreprocessing, pca_components=5)

# Temporary lines of code to seperate testData and data after transformation
data_processed = preprocessed_data[:233154,:]
testData_processed = preprocessed_data[233154:,:]

# Extracting dependent and independent columns
x = data_processed[:,:]
y = (dependentVar.values)[:]

#splitting data into test and train dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =  train_test_split(x,y, train_size = 0.6, random_state = 0)

# Prediction using XGBoost Boosting method
from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(x_train, y_train)
prediction = model.predict_proba(x_test)


# Model Performance measurement
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, prediction[:,1]))

predict_x = model.predict_proba(testData_processed)
df = pd.DataFrame({"UniqueID": testData_index, 'loan_default':predict_x[:,1]}) 
df.to_csv('/home/ajay/Documents/LTFS DATASET/prediction/Predicted_output_XGBoost.csv',header=True, index=False)




