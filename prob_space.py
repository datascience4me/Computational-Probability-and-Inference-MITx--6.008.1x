# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:02:47 2017

@author: pia-hp
"""

def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total

prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
rainy_or_snowy_event = {'rainy', 'sunny'}
print(prob_of_event(rainy_or_snowy_event, prob_space))