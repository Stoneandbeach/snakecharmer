## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:7|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## Count the number of times a given number appears in a list##
## of integers and return the result.                        ##
##                                                           ##
## Inputs:                                                   ##
## lst: list                                                 ##
## number: int                                               ##
##                                                           ##
## Returns:                                                  ##
## count: int                                                ##
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


def solution(lst, number):
    count = 0
    for element in lst:
        if element == number:
            count += 1
    return count

def solution(lst, number):
    return lst.count(number)