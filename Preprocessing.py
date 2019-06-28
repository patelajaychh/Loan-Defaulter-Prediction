#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:15:19 2019

@author: ajay
"""

import Utils
import datetime
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler


def preproccesing(data_sampled, pca_components = 5):
    """
    Perform preprocessing of data and tranformationa and return the transformed data
    1. removing NaN values if any
    2. Converting categorical to continuous data variable
    3. Label encoding and then One Hot Encoding
    4. Performs PCA for dimenstions reduction
    """
    features = {  'UniqueID':0, 'disbursed_amount':1,'asset_cost':2,'ltv':3,'branch_id':4,'supplier_id':5,
                  'manufacturer_id':6,'Current_pincode_ID':7,'Date.of.Birth':8,'Employment.Type':9,'DisbursalDate':10,'State_ID':11,
                  'Employee_code_ID':12,'MobileNo_Avl_Flag':13, 'Aadhar_flag':14,'PAN_flag':15,'VoterID_flag':16,
                  'Driving_flag':17, 'Passport_flag':18,'PERFORM_CNS.SCORE':19, 'PERFORM_CNS.SCORE.DESCRIPTION':20,
                  'PRI.NO.OF.ACCTS':21,'PRI.ACTIVE.ACCTS':22,'PRI.OVERDUE.ACCTS':23,'PRI.CURRENT.BALANCE':24,
                  'PRI.SANCTIONED.AMOUNT':25,'PRI.DISBURSED.AMOUNT':26,'SEC.NO.OF.ACCTS':27,'SEC.ACTIVE.ACCTS':28,
                  'SEC.OVERDUE.ACCTS':29, 'SEC.CURRENT.BALANCE':30, 'SEC.SANCTIONED.AMOUNT':31,'SEC.DISBURSED.AMOUNT':32,
                  'PRIMARY.INSTAL.AMT':33, 'SEC.INSTAL.AMT':34, 'NEW.ACCTS.IN.LAST.SIX.MONTHS':35, 'DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS':36, 
                  'AVERAGE.ACCT.AGE':37,'CREDIT.HISTORY.LENGTH':38, 'NO.OF_INQUIRIES':39,'loan_default':40 }

    # Removing NaN values
    data_sampled = data_sampled.drop(['branch_id','supplier_id', 'manufacturer_id','Current_pincode_ID', 'State_ID', 'Employee_code_ID'], axis = 1)

    from sklearn_pandas import CategoricalImputer
    imputer = CategoricalImputer()
    data_sampled['Employment.Type'] = imputer.fit_transform(data_sampled['Employment.Type'])
    
    # Categorial to continuos

    import functools    # Used for mapping a function with more than one argument 
    data_sampled['Date.of.Birth'] = list(map(Utils.toDate, data_sampled['Date.of.Birth']))
    data_sampled['Date.of.Birth'] = list(map(functools.partial(Utils.date_diff, date2 = datetime.datetime.today().date()), data_sampled['Date.of.Birth']))
    
    data_sampled['DisbursalDate'] = list(map(Utils.toDate, data_sampled['DisbursalDate']))
    data_sampled['DisbursalDate'] = list(map(functools.partial(Utils.date_diff, date2 = datetime.datetime.today().date()), data_sampled['DisbursalDate']))
    
    data_sampled['AVERAGE.ACCT.AGE'] = list(map(Utils.total_span, data_sampled['AVERAGE.ACCT.AGE'] ))   #1yrs 10mon = 1*12 +10 = 22
    data_sampled['CREDIT.HISTORY.LENGTH'] = list(map(Utils.total_span, data_sampled['CREDIT.HISTORY.LENGTH'] ))   #1yrs 10mon = 1*12 +10 = 22

    x = data_sampled.iloc[:,0:34].values
    
    # Label encoding categorical values
    encoder = LabelEncoder()
    x[:,5] = encoder.fit_transform(x[:,5])
    x[:,14] = encoder.fit_transform(x[:,14])

    # Hot encoding new columns
    hot_encoder = OneHotEncoder(categorical_features=[5,14])
    x = hot_encoder.fit_transform(x).toarray()

    #normalizing data (scaling the data)
#    scale = StandardScaler()
#    x = scale.fit_transform(x)

    # feature selection using random forest
    # feature selection using PCA
#    from sklearn.decomposition import PCA
#    pca = PCA(n_components=pca_components)
#    x = pca.fit_transform(x)

    return (x)
