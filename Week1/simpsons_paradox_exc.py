# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:30:41 2017

@author: pia-hp
"""

from simpsons_paradox import *

print("Joint probability table:\n" + str(joint_prob_table))
print(joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']])
joint_prob_gender_admission = joint_prob_table.sum(axis=1)
print(joint_prob_gender_admission)
print(joint_prob_gender_admission[gender_mapping['female'], admission_mapping['admitted']])

# What is P(A=admitted|G=female)
female_only = joint_prob_gender_admission[gender_mapping['female']]
prob_admission_given_female = female_only / np.sum(female_only)
prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print('P(A|G=female) = ' + str(prob_admission_given_female_dict))

# What is P(A=admitted|G=male)
male_only = joint_prob_gender_admission[gender_mapping['male']]
prob_admission_given_male = male_only / np.sum(male_only)
prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))
print('P(A|G=male) = ' + str(prob_admission_given_male_dict))

# Let's investigate by looking at how things differ by each department.
admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print(prob_gender_given_admitted_dict)


def cond_prob_admission(g,d):
       return str(joint_prob_table[
                   gender_mapping[g], department_mapping[d], admission_mapping['admitted']] / np.sum(
        joint_prob_table[gender_mapping[g], department_mapping[d]]))




def solution(gender,department):
    for d in department:
        for g in gender:
            print('For Gender = '+ g + ' and dept = '+ d +  ' The Prob is:  ' + cond_prob_admission(g,d))
            
            
solution(['female','male'],['A','B','C','D','E','F'])
            
            
            
