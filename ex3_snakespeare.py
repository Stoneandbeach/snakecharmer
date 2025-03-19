## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:3|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## Snakespeare:                                              ##
## Provide the input for a Markov chain-based text generator.##
## Given an input of a string (incidentally containing the   ##
## collected sonnets of William Shakespeare), build a        ##
## dictionary(or dictionary-like structure) with             ##
##     key: tuple(word1, word2)                              ##
##     value: list(words...]                                 ##
## where the keys should be all occurences of two consecutive##
## words, and the value for that key is a list of all words  ##
## thatfollow that particular combination of word1, word2.   ##
## Example:                                                  ##
##                                                           ##
## 'This text is an example text. This text will hopefully   ##
## help. For an example is an aid.'                          ##
##                                                           ##
## becomes                                                   ##
##                                                           ##
## {                                                         ##
##     ('This', 'text') ['is', 'will']                       ##
##     ('text', 'is') ['an']                                 ##
##     ('is', 'an') ['example', 'aid.']                      ##
##     ('an', 'example') ['text.', 'is']                     ##
##     ('example', 'text.') ['This']                         ##
##     ('text.', 'This') ['text']                            ##
##     ('text', 'will') ['hopefully']                        ##
##     ('will', 'hopefully') ['help.']                       ##
##     ('hopefully', 'help.') ['For']                        ##
##     ('help.', 'For') ['an']                               ##
##     ('For', 'an') ['example']                             ##
##     ('example', 'is') ['an']                              ##
## }                                                         ##
##                                                           ##
## You may need to take care to remove whitespace characters,##
## like \n and \t.                                           ##
##                                                           ##
## Inputs:                                                   ##
## sonnets: str                                              ##
##                                                           ##
## Returns:                                                  ##
## word_dict: dict or dict-like                              ##
##                                                           ##
## --------------------------IMPORTS------------------------ ##
## Imports - put any imports you use here                    ##
import numpy as np


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