## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:2|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
"""
clamp_values:
Given a matrix of integer values, constrain the range of those
values to [0, 255] inclusive. Any number originally in that
range is to remain unchanged, while a number < 0 should be set
to 0 and a number > 255 to 255.

Inputs:
matrix: list(n * list(m * int))

Returns:
matrix: iterable(n * iterable(m * int))
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

def solution(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 255:
                matrix[i][j] = 255
    return matrix