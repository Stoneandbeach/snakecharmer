## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:3|                                                     ##
## --------------------------IMPORTS------------------------ ##
## Imports - put any imports you use here                    ##
from collections import defaultdict

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

def solution_(sonnets):
    words = sonnets.split()
    
    word_dict = defaultdict(list)
    
    [word_dict[(words[i], words[i+1])].append(words[i+2]) for i in range(len(words) - 2)]
        
    return word_dict

def solution(sonnets):
    word_dict = dict()
    
    w1, w2, w3 = "", "", ""
    found_space = False
    for char in sonnets:
        if char.isspace():
            found_space = True
            continue
        
        if found_space:
            if w1 and w2 and w3:
                if (w1, w2) not in word_dict.keys():
                    word_dict[(w1, w2)] = list()
                word_dict[(w1, w2)].append(w3)
            w1, w2, w3 = w2, w3, ""
            found_space = False
        
        w3 += char
    
    if (w1, w2) not in word_dict.keys():
        word_dict[(w1, w2)] = list()
    word_dict[(w1, w2)].append(w3)
        
    return word_dict