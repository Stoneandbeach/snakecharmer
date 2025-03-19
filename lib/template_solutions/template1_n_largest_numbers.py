## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:1|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##

def solution(lst, n):
    largest = []
    for i in (range(n)):
        this_largest = 0
        largest_index = 0
        for n, num in enumerate(lst):
            if num > this_largest:
                this_largest = num
                largest_index = n
        largest.append(this_largest)
        lst.pop(largest_index)
    return largest
                