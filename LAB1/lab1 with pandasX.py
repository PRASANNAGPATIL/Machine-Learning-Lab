# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:43:21 2019

@author: ISHAAN
"""

import pandas as pd
dataset = pd.read_csv('lab1_with_pandas.csv')
X = dataset.iloc[:, :].values

print("\n The most general hypothesis : ['?','?','?','?','?','?'] \n")
print("\n The most specific hypothesis : ['0','0','0','0','0','0'] \n")
num_of_attributes=6
print("\n The initial value of hypothesis :")
hypothesis = ['0']*num_of_attributes;
print(hypothesis)

for j in range(0,num_of_attributes): # j varies from 0 to 5
    hypothesis[j] = X[0][j];

print("\n Find S: Finding a maximally specific hypothesis \n")

for i in range(0,len(X)): # i valies from 0 to 3, len(a) is 4, i.e, 4 instances in dataset
    if X[i][num_of_attributes]=='Yes':  # checking the label/target is "yes" or "no"
        for j in range(0,num_of_attributes): # j varies from 0 to 5
            if X[i][j]!=hypothesis[j]:  # check 1st instance's 1st attribute value  is same as hypothesis's 1st value or not
                hypothesis[j]='?'       # if no then replace the old hypothesis by "?"
            else:
                hypothesis[j]=X[i][j]   # if yes then copy the attibute value to respective hypothesis
    print("For Training Example No : {0} the hypothesis is".format(i),hypothesis)
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
