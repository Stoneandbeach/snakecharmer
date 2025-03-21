## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:4|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##

def solution(lst):
    max_value = max(lst)
    new_lst = []
    for value in lst:
        new_value = value / max_value
        new_lst.append(new_value)
    return new_lst