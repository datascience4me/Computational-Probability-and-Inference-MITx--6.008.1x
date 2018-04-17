# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:48:58 2018

@author: pia-hp
"""
import numpy as np
import matplotlib.pyplot as plt
def entropy(P_X):
    return np.sum(P_X * np.log2(1 / P_X ))
    
    
    
entropy1 = entropy(np.array([(999999/1000000) , (1/1000000)]))
print(entropy1)
entropy2 = entropy(np.array([(999999/1000000) , (1/1000000)]))
print(entropy2)
entropy3 = entropy(np.array([(9/10) , (1/10)]))
print(entropy3)

def plot_Entropy():
    p_list = np.linspace(0,1,50)
    plt.figure()
    plt.plot(p_list, 
             [ entropy(np.array([p, 1-p])) for p in p_list])
    plt.xlabel('p')
    plt.ylabel('H(Ber(p))')
    plt.show()
    
plot_Entropy()