## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:4|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## n_largest_numbers:                                        ##
## Given an input list 'lst' and integer 'n', find the n     ##
## largest numbers in lst. Return a list with the those      ##
## number sorted from largest to smallest.                   ##
##                                                           ##
## Inputs:                                                   ##
## lst: list                                                 ##
## n: int                                                    ##
##                                                           ##
## Returns:                                                  ##
## largest: iterable, length n                               ##
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

def solution(lst, n):
    largest = []
    for i in (range(n)):
        this_largest = 0
        largest_index = 0
        for n, num in enumerate(lst):
            # Check if the current number is the largest so far, and store it and its index
            if num > this_largest:
                this_largest = num
                largest_index = n
        # Store the largest number found, and remove if from lst
        largest.append(this_largest)
        lst.pop(largest_index)
    return largest
                