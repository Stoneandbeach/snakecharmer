## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:6|                                                     ##
## -------------------EXERCISE DESCRIPTION------------------ ##
## You believe that a new particle, called a bothon, is      ##
## being created at the LHC! If so, that could explain the   ##
## process of inflation in the early universe.               ##
##                                                           ##
## The hypothetical bothon is created with some energy E.    ##
## For each picosecond, its energy doubles! When it reaches  ##
## a high enough energy E_SPLIT, it will decay into two new  ##
## bothons.                                                  ##
##                                                           ##
## When this happens, the total energy is decreased by the   ##
## mass needed to create the new bothons, and then the rest  ##
## is divided among them. Since a bothon has mass E_MASS, if ##
## the total energy is E_OLD, each new bothon will get       ##
## (E_OLD - 2 * E_MASS) / 2.                                 ##
##                                                           ##
## The new bothons then also double in energy for each pico- ##
## second until they too split. However, this process only   ##
## continues until 60 picosecond have passed. After that,    ##
## the remaining bothons reach thermal equilibrium and stop  ##
## multiplying.                                              ##
##                                                           ##
## You are tasked with writing simulation software to de-    ##
## scribe this process. Given than a single bothon is crea-  ##
## ted with energy E = 8 GeV, and that E_SPLIT = 12 GeV and  ##
## E_MASS = 3 GeV, how many will there be when 60 pico-      ##
## seconds have passed?                                      ##
##                                                           ##
## Your input will be the initial state in the form of a     ##
## list with the energy of the first bothon. Calculate how   ##
## many bothons there will be after 60 picoseconds have      ##
## passed and return that number.                            ##
##                                                           ##
## Inputs:                                                   ##
## initial_state = [8]                                       ##
##                                                           ##
## Returns:                                                  ##
## final_state: int repr. the final number of bothons        ##
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


def step(bothons, E_split, E_mass):
    new_bothons = []
    for bothon in bothons:
        if bothon > E_split:
            # Bothon is above splitting energy. Split it into
            # two new bothons and store their energies.
            new_energy = (bothon - 2 * E_mass) / 2
            new_bothons.extend([new_energy, new_energy])
        else:
            # Double bothon energy
            new_bothons.append(bothon * 2)
    return new_bothons

def solution(initial_state, E_split, E_mass, stop_threshold):
    bothons = initial_state
    steps = 0
    
    while (steps := steps + 1)  <= stop_threshold:
        bothons = step(bothons, E_split, E_mass)
    
    number_of_bothons = len(bothons)
    return number_of_bothons
