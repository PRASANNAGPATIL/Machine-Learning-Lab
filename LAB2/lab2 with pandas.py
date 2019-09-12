# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:06:04 2019

@author: ISHAAN
"""

import pandas as pd

dataset = pd.read_csv("lab2_with_pandas.csv")

concepts = dataset.iloc[:,0:-1].values
target = dataset.iloc[:,-1].values

def learn(concepts, target):

    specific_h = concepts[0].copy()
    
    general_h = [['?' for i in range(len(specific_h))] for i in  range(len(specific_h))]  # len(specific_h)=6
    for i, h in enumerate(concepts):  # enumerate returns number of instances in i from 0 to 3, and each instances in h in each iteration, i.e, in 1st iteration, h=['Sunny' 'Warm' 'Normal' 'Strong' 'Warm' 'Same']
        # Checking if the hypothesis has a positive target
        if target[i] == "Yes":               # if its a +ve instance
            for x in range(len(specific_h)): # x varies from 0 to 5 & len(specific_h)=6

                # Change values in S & G only if values change
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
                   

        # Checking if the hypothesis has a positive target
        if target[i] == "No":               # if its a -ve instance
            for x in range(len(specific_h)):

                # For negative hyposthesis change values only in G
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

    # find indices where we have empty rows, meaning those that are unchanged
    indices = [i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
    for i in indices:
        # remove those rows from general_h
        general_h.remove(['?','?','?','?','?','?'])

    # Return final values
    return specific_h, general_h

s_final, g_final = learn(concepts, target)
print("Final S:", s_final, sep="\n")
print("Final G:", g_final, sep="\n")
dataset.head()