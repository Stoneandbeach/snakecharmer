## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:5|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##
import csv
import math

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