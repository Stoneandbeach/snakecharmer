## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:6|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## You are analysing a file of data from a collider experi-  ##
## ment. This data has been run through a machine learning   ##
## classifier, and each data point is labelled as either     ##
## "signal" (if the classifier thinks it is interesting) or  ##
## "background" (if it does not).                            ##
##                                                           ##
## Each data point represents a detected particle. Your task ##
## is to find all the data points labelled "signal" and cal- ##
## culate the average and standard deviation of the mass of  ##
## those particles.                                          ##
##                                                           ##
## The data is stored as a .csv file, with ',' as the delimi-##
## ter between values and the following column headers:      ##
##                                                           ##
## event_nr,classification,pt,eta,phi,mass                   ##
##                                                           ##
## Inputs:                                                   ##
## file: str (name of the .csv file)                         ##
##                                                           ##
## Returns:                                                  ##
## (mass_average, mass_std): tuple(float, float)             ##
##                                                           ##
## --------------------------IMPORTS------------------------ ##
## Imports - put any imports you use here                    ##
import math
import csv
import numpy as np


## ----------------------------CODE------------------------- ##
## Write your code below.                                    ##
## The solution(...) function is entry point to your code.   ##
## Note that its name and arguments must remain unchanged.   ##
## You are free to define any additional functions, classes  ##
## etc., but please do not perform any work outside of a     ##
## function body.                                            ##
##                                                           ##
## var = 2                   <--- no                         ##
## lst = sorted(lst)         <--- also no                    ##
##                                                           ##
## def func(lst):                                            ##
##       var = 2             <--- yes                        ##
##       lst = sorted(lst)   <--- also yes                   ##


def solution(file):
    data_table = []
    with open(file, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data_table.append(row)
    
    headers = data_table[0]
    masses = []
    for row in data_table[1:]:
        if row[1] == "signal":
            masses.append(float(row[5]))
            
    mass_mean = sum(masses) / len(masses)
    mass_std = math.sqrt(sum([(mass - mass_mean)**2 for mass in masses]) / len(masses))
    return mass_mean, mass_std