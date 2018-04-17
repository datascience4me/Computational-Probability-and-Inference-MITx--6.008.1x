# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:10:26 2017

@author: pia-hp
"""

#Approach 1
import comp_prob_inference

def approach1():
    
    prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
    W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
    I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}
    random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
    W = W_mapping[random_outcome]
    I = I_mapping[random_outcome]
    print("Approach 1: ", W,I)

#Approach 2

def approach2():
    
    W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
    I_table = {0: 1/2, 1: 1/2}
    W = comp_prob_inference.sample_from_finite_probability_space(W_table)
    I = comp_prob_inference.sample_from_finite_probability_space(I_table)
    print("Approach 2: ",W,I)

approach1()
approach2()