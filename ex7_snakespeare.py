## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:7|                                                     ##
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
## that follow that particular combination of word1, word2.  ##
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
## So the phrase 'This text' can be followed by either 'is'  ##
## or 'will', while 'text is' can only be followed by the    ##
## word 'an'.                                                ##
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
    # Note! This is definitely not the most reasonable algorithm to use!
    
    # Setup dictionary
    word_dict = dict()
    
    # Setup variables to store words
    w1, w2, w3 = "", "", ""
    
    # Setup boolean to track whitespace
    in_space = False
    
    # Loop over the text character by character
    for char in sonnets:
        if char.isspace():
            # Character is whitespace: we are in a space between words
            in_space = True
            # Keep going until we find the start of a new word
            continue
        
        else:
            # Character is not whitespace, i.e. part of a word
            if in_space:
                # The previous character was whitespace
                # We have found a new word
                in_space = False
                
                if w1 != "" and w2 != "" and w3 != "":
                    # All of w1, w2 and w3 are words
                    
                    if (w1, w2) not in word_dict.keys():
                        # The dictionary does not yet have the key (w1, w2)
                        word_dict[(w1, w2)] = list()
                        
                    # Add w3 to the list of words that can follow (w1, w2)
                    word_dict[(w1, w2)].append(w3)
                
                # Move w2->w1, w3->w2 and reset w3 so it can start
                # collecting characters from the next word when a
                # non-space character is found
                w1, w2, w3 = w2, w3, ""
            
            # Add this character to w3
            w3 += char
    
    # Add the last w3 to the dictionary. This is necessary since in the
    # loop, words are only added when the start of the next word is found.
    # Therefore, the last word will not be added while looping.
    if (w1, w2) not in word_dict.keys():
        word_dict[(w1, w2)] = list()
    word_dict[(w1, w2)].append(w3)
        
    return word_dict