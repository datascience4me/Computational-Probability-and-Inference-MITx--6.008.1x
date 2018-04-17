# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:31:24 2018

@author: pia-hp
"""

import numpy as np




def mutualInformation():
    joint_prob_XY = np.array([[0.10, 0.09, 0.11], [0.08, 0.07, 0.07], [0.18, 0.13, 0.17]])
    prob_X = joint_prob_XY.sum(axis=1)
    prob_Y = joint_prob_XY.sum(axis=0)
    joint_prob_XY_indep = np.outer(prob_X, prob_Y)
    
    print(prob_X)
    print(prob_Y)
    print(joint_prob_XY_indep)
    total = 0
    
    for i in range(len(prob_X)):
        for j in range(len(prob_Y)):
            value = joint_prob_XY[i][j] * np.log2(joint_prob_XY[i][j] / joint_prob_XY_indep[i][j])
            total +=  value
    return total
    
    
print(mutualInformation())