## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:1|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
"""
n_largest_numbers:
Given an input list 'lst' and integer 'n', find the n largest
numbers in lst. Return a list with the those number sorted from
largest to smallest.

Inputs:
lst: list
n: int
"""
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

def solution(lst, n):
    lst = sorted(lst, reverse=True)
    return lst[:n]

def solution_(lst, n):
    largest = [0 for _ in range(n)]
    for num in lst:
        if num > min(largest):
            largest.pop()
            largest.append(num)
        largest = sorted(largest, reverse=True)
    return largest