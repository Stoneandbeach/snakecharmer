## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:999|                                                   ##
## --------------------------IMPORTS------------------------ ##
## Imports - put any imports you use here                    ##
import math


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

def results(lst, n):
    lst_sum = sum(lst)
    return [i/lst_sum for i in lst]

def solution(lst, n):
    res = results(lst, n)
    return res