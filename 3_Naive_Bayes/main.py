# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:43:46 2021

@author: DyningAida
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

df = pd.read_csv("car.csv", sep=',',usecols=[0, 1, 2, 3, 4, 5,6],
                    names=['buyprc','maintprice','doors','persons','lug_boot','safety','recommend'])
# encode atribut
encode = LabelEncoder()
df['buyprc'] = encode.fit_transform(df['buyprc'])
df['maintprice'] = encode.fit_transform(df['maintprice'])
df['doors'] = encode.fit_transform(df['doors'])
df['persons'] = encode.fit_transform(df['persons'])
df['lug_boot'] = encode.fit_transform(df['lug_boot'])
df['safety'] = encode.fit_transform(df['safety'])
df['recommend'] = encode.fit_transform(df['recommend'])
# independent variable
x = df.drop(["recommend"], axis = 1)
x.head()
# dependent variable
y = df["recommend"]
y.head()

# split data train dan data test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 123)

# memanggil naive bayes classifier
nb = GaussianNB()

# menginputkan data training
nb_train = nb.fit(x_train, y_train)

# Menentukan hasil prediksi dari x_test
y_pred = nb_train.predict(x_test)
y_pred

np.array(y_test)

# Menentukan probabilitas hasil prediksi
nb_train.predict_proba(x_test)

#membuat confusion matrix
confusion_matrix(y_test, y_pred)
f1_score(y_test, y_pred, labels=np.unique(y_pred), average='weighted')
# print classification report
print(classification_report(y_test, y_pred))