# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 21:43:21 2019

@author: ISHAAN
"""
import csv
attributes = [['Sunny','Rainy'],['Warm','Cold'],['Normal','High'],['Strong','Weak'],['Warm','Cool'],['Same','Change']]
#type of attributes is list
num_attributes = len(attributes)
#num_attributes=6
print("\n The most general hypothesis : ['?','?','?','?','?','?'] \n")
print("\n The most specific hypothesis : ['0','0','0','0','0','0'] \n")
a=[]
#a is empty list
print("\n The given training data set \n")
csvFile= open(r"lab1.csv")
reader = csv.reader(csvFile)
a=list(reader)
print(a)
#      another way to read csv file is
#with open(r"lab1.csv",'r')as csvFile:
#    reader = csv.reader(csvFile)
#    for row in reader :
#        #reading each line in the csv file object "reader"
#        a.append(row)
#        print(row)
# now list "a" contains all the 4 rows of csv file
# a=[['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
#    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
#    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
#    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']]

print("\n The initial value of hypothesis :")
hypothesis = ['0']*num_attributes
print(hypothesis)
#hypothesis has null hypothesis in the beginning, i.e, 
# hypothesis= ['0', '0', '0', '0', '0', '0']

#comparing with first training example
for j in range(0,num_attributes): # j varies from 0 to 5
    hypothesis[j] = a[0][j];
    # now hypotheses becomes ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
    
#comparing with remaining training examples of given data set
print("\n Find S: Finding a maximally specific hypothesis \n")

for i in range(0,len(a)): # i valies from 0 to 3, len(a) is 4, i.e, 4 instances in dataset
    if a[i][num_attributes]=='Yes':  # checking the label/target is "yes" or "no"
        for j in range(0,num_attributes): # j varies from 0 to 5
            if a[i][j]!=hypothesis[j]:  # check 1st instance's 1st attribute value  is same as hypothesis's 1st value or not
                hypothesis[j]='?'       # if no then replace the old hypothesis by "?"
            else:
                hypothesis[j]=a[i][j]   # if yes then copy the attibute value to respective hypothesis
    print("For Training Example No : {0} the hypothesis is".format(i),hypothesis)
print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
