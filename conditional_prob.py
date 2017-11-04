# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:10:14 2017

@author: pia-hp
"""

p_s = 0.001
p_t_s = 0.99
p_nt_ns = 0.99
p_n_s =0.999
p_t_ns = 0.01

p_n_s = (p_t_s*p_s)/(p_s*p_t_s + p_n_s*p_t_ns)
print(p_n_s)