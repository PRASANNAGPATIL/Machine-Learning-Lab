"""
Created on Fri Aug 16 23:02:26 2019

@author: ISHAAN
"""
import csv
print("\n The given training data set \n")
csvFile= open(r"lab2.csv")
reader = csv.reader(csvFile)
a=list(reader)
print(a)
concepts=[]
target=[]
num_attributes=len(a[0][:-1])
for i in range(0,len(a)):# i varies from 0 to 3
    concepts.append(a[i][0:6])
    target.append(a[i][6])

def learn(concepts, target):

   #learn() function implements the learning method of the Candidate elimination algorithm
   # Arguments:
       # concepts - a data frame with all the features
       # target - a data frame with corresponding output values

   # Initialise S0 with the first instance from concepts
   # .copy() makes sure a new list is created instead of just pointing to the same memory location ’’’
    specific_h = concepts[0].copy()
    #specific_h=['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']

    # Initialises G0 using list comprehension
    # Creates as many lists inside as there are arguments,
    # that which later will be replaced with actual parameters

    general_h = [['?' for i in range(len(specific_h))] for i in  range(len(specific_h))]  # len(specific_h)=6
    # general_h = [[’?’, ’?’, ’?’, ’?’, ’?’, ’?’],
    #              [’?’, ’?’, ’?’, ’?’, ’?’, ’?’],
    #              [’?’, ’?’, ’?’, ’?’, ’?’, ’?’],
    #              [’?’, ’?’, ’?’, ’?’, ’?’, ’?’],
    #              [’?’, ’?’, ’?’, ’?’, ’?’, ’?’],
    #              [’?’, ’?’, ’?’, ’?’, ’?’, ’?’]]  
    
    # The learning iterations
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
