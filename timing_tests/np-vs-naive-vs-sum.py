import timeit
import dis
import numpy as np

# Length of list to sum
length = 100000

# Timing setup
setup_naive = """
from __main__ import length
from __main__ import naive_sum as func
lst = list(range(length))
"""

setup_sum = """
from __main__ import length
from __main__ import builtin_sum as func
lst = list(range(length))
"""

setup_np = """
from __main__ import length
from __main__ import numpy_sum as func
import numpy as np
numpy_array = np.arange(length)
"""

setup_np_w_creation = """
from __main__ import length
from __main__ import sum_w_array_creation as func
import numpy as np
lst = list(range(length))
"""

def naive_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def builtin_sum(lst):
    return sum(lst)

def numpy_sum(numpy_array):
    return numpy_array.sum()

def sum_w_array_creation(lst):
    return np.array(lst).sum()

def main():
    # Number of iterations to average execution time over. Needs to
    # be a decent number in order to get stable timings.
    number = 10000
    
    print("Timing naive_sum...")
    t_naive = timeit.timeit(stmt="func(lst)", setup=setup_naive, number=number)
    
    print("Timing built-in sum...")
    t_sum = timeit.timeit(stmt="func(lst)", setup=setup_sum, number=number)
    
    print("Timing NumPy.sum...")
    t_np = timeit.timeit(stmt="func(numpy_array)", setup=setup_np, number=number)
    
    print("Timing NumPy.sum with array creation...")
    t_np_incl = timeit.timeit(stmt="func(lst)", setup=setup_np_w_creation, number=number)
    
    print("\nBytecode of naive sum function:")
    dis.dis(naive_sum)
    
    print("\n==========================================\n")
    
    print("Bytecode of function using built-in sum:")
    dis.dis(builtin_sum)
    
    print("\n==========================================\n")
    
    print("Bytecode of function using NumPy sum:")
    dis.dis(numpy_sum)
    
    print("\n==========================================\n")
    
    print("Bytecode of function which creates an array, then uses NumPy sum:")
    dis.dis(sum_w_array_creation)
    
    print(f"\nTesting; naive: {naive_sum(list(range(1000)))}, vs. built-in: {builtin_sum(list(range(1000)))}, vs. NumPy: {numpy_sum(np.arange(1000))}")
    
    print(f"Naive: {1e6*t_naive/number:.3f} µs\nBuilt-in: {1e6*t_sum/number:.3f} µs\nNumPy: {1e6*t_np/number:.3f} µs\nNumPy including array creating: {1e6*t_np_incl/number:.3f} µs")
    

if __name__ == "__main__":
    main()