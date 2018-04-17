# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:01:11 2018

@author: pia-hp
"""

import math

#Calculation of Expectation 

def calculateExpectation(X , P_X ):
    expectation_1 = 0
    for i in range(2):
        value = (X[i] * P_X[i])
        expectation_1 += value
    return expectation_1
    
#Calculation of Variance

def calculateVariance(X , P_X):
    excpectation = calculateExpectation(X,P_X)
    variance = 0
    for i in range(len(X)):
        new_X = X[i] - excpectation
        value = pow(new_X,2) * P_X[i]
        variance += value
    return variance
   
#Calculation of Standard Deviation
   
def calculateStd(X,P_X):
    return math.sqrt(calculateVariance(X,P_X))
   
#L1
print("The answer of L1: ")
print()
print(calculateVariance([ -1 , -1+1000],[(999999 / 1000000) , (1/1000000) ]))
print(calculateStd([ -1 , 999],[(999999 / 1000000) , (1/1000000) ]))
print()
print()
#L2
print("The answer of L2: ")
print()
print(calculateVariance([ -1 , -1+1000000],[(999999 / 1000000) , (1/1000000) ]))
print(calculateStd([ -1 , -1+1000000],[(999999 / 1000000) , (1/1000000) ]))
print()
print()
#L3
print("The answer of L3: ")
print()
print(calculateVariance([ -1 , -1+10],[(9/ 10) , (1/10) ]))
print(calculateStd([ -1 , -1+10],[(9/ 10) , (1/10) ]))