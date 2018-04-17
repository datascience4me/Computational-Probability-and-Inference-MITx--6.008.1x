# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:47:55 2017

@author: pia-hp
"""
def TwoFairDiceRoll():
    pmf={}
    for x in range(1,7):
        for y in range(1,7):
            if x+y in pmf:
                pmf[x+y] += 1/36
            else:
                pmf[x+y] = 1/36
            print(pmf[x+y])
    
TwoFairDiceRoll()