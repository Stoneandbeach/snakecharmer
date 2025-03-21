## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:4|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## normalization:                                            ##
## Given an input list 'lst' of numbers, normalize all the   ##
## values by the largest value and return a list or list-    ##
## like containing the results. The values in the output     ##
## should hence be between 0 and 1.                          ##
##                                                           ##
## Inputs:                                                   ##
## lst: list of values                                       ##
##                                                           ##
## Returns:                                                  ##
## lst: iterable of normalized values                        ##
##                                                           ##
## --------------------------IMPORTS------------------------ ##
## Imports - put any imports you use here                    ##



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
 

def normalize(value, normalize_by):
    return value / normalize_by

def solution(lst):
    new_lst = []
    for value in lst:
        new_value = normalize(value, max(lst))
        new_lst.append(new_value)
    return new_lst