## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:2|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##

def solution(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 255:
                matrix[i][j] = 255
    return matrix