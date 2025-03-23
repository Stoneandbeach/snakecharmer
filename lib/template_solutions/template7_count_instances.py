## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:7|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##

def solution(lst, number):
    count = 0
    for element in lst:
        if element == number:
            count += 1
    return count