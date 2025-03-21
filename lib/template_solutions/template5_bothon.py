## ------------------------EXERCISE ID---------------------- ##
## Exercise id number - don't change this!                   ##
## id:5|                                                     ##
## ------------------------DESCRIPTION---------------------- ##
## This is a template used to provide a correct result for   ##
## checking exercise submissions. Please don't change this!  ##
from collections import defaultdict
import numpy as np

def solution(initial_state, E_split, E_mass, stop_threshold):
    if isinstance(initial_state, np.ndarray):
        initial_state = initial_state.tolist()
    
    bothon_dict = defaultdict(int)
    for energy in initial_state:
        bothon_dict[energy] = bothon_dict[energy] + 1
    
    steps = 0
    while (steps := steps + 1)  <= stop_threshold:
        temp_dict = defaultdict(int)
        for bothon_energy, bothon_count in bothon_dict.items():
            if bothon_energy > E_split:
                temp_dict[(bothon_energy - 2 * E_mass) / 2] += 2 * bothon_count
            else:
                temp_dict[bothon_energy * 2] += bothon_count
        bothon_dict = temp_dict
    
    number_of_bothons = sum([value for value in bothon_dict.values()])
    return number_of_bothons