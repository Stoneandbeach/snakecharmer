import timeit
import time
import dis
import numpy as np
import sys

setup = """
from __main__ import create_ordered_list, create_disordered_list, f
length = 50000
ordered_list = create_ordered_list(length=length)
disordered_list = create_disordered_list(length=length, stride=100)
"""

statement_ordered = """
f(ordered_list)
"""

statement_disordered = """
f(disordered_list)
"""

def create_ordered_list(length):
    return list(range(length))

def create_disordered_list(length, stride):
    ordered_list = create_ordered_list(length)
    disordered_list = []
    for position in range(stride):
        disordered_list.extend(ordered_list[position::stride])
    return disordered_list

def create_alternating_list(length):
    my_list = [length for _ in range(length)]
    my_list[::2] = [1 for _ in range(length//2)]
    return my_list

def create_half_n_half(length):
    my_list = [1 for _ in range(length//2)]
    my_list[len(my_list):] = [length for _ in range(length//2)]
    return my_list

def f(my_list):
    temp = 0
    for value in my_list:
        temp += value
    return temp

def builtin_sum(my_list):
    return sum(my_list)

def np_sum(my_array):
    return my_array.sum()

def measure_time(func, inp, iterations=1000000):
    start = time.perf_counter()
    for _ in range(iterations):
        func(inp)
    end = time.perf_counter()
    print(f"Time: {end - start} s")

def main():
    
    """
    timer_ordered = timeit.Timer(stmt=statement_ordered, setup=setup)
    time_ordered = timer_ordered.repeat(repeat = 5, number=5000)
    print(f"Ordered {time_ordered}")
    
    timer_disordered = timeit.Timer(stmt=statement_disordered, setup=setup)
    time_disordered = timer_disordered.repeat(repeat = 5, number=5000)
    print(f"Disordered {time_disordered}")
    
    print(f"Ordered sum: {f(create_ordered_list(length=50000))}")
    print(f"Disrdered sum: {f(create_disordered_list(length=50000, stride=100))}")
    """
    
    a = create_ordered_list(40000)
    print(a[:15])
    print(f"Length: {len(a)}, sum: {f(a)}")
    b = create_disordered_list(40000, 100)
    print(b[:15])
    print(f"Length: {len(b)}, sum: {f(b)}")
    c = create_alternating_list(40000)
    print(c[:15])
    print(f"Length: {len(c)}, sum: {f(c)}")
    d = create_half_n_half(40000)
    print(d[:15])
    print(f"Length: {len(d)}, sum: {f(d)}")
    
    #for x, y in zip(a[:1000], b[:1000]):
    #    print(x, y)
        
    #sys.exit()
    
    measure_time(builtin_sum, a)
    measure_time(builtin_sum, b)
    measure_time(builtin_sum, c)
    measure_time(builtin_sum, d)
    
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    measure_time(np_sum, a)
    measure_time(np_sum, b)
    measure_time(np_sum, c)
    

if __name__ == "__main__":
    main()