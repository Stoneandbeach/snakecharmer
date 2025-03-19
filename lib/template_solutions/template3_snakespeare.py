## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:3|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##

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