import timeit
import dis

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

def naive_sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def builtin_sum(lst):
    return sum(lst)

def main():
    # Number of iterations to average execution time over
    number = 1000
    
    t_naive = timeit.timeit(stmt="func(lst)", setup=setup_naive, number=number)
    
    t_sum = timeit.timeit(stmt="func(lst)", setup=setup_sum, number=number)
    
    print("Bytecode of naive sum function:")
    dis.dis(naive_sum)
    
    print("\n==========================================\n")
    
    print("Bytecode of function using built-in sum:")
    dis.dis(builtin_sum)
    
    print("\n==========================================\n")
    
    print(f"Testing; these numbers should be the same. Naive: {naive_sum(list(range(1000)))}, vs. built-in: {builtin_sum(list(range(1000)))}")
    
    print(f"Naive: {1e6*t_naive/number:.3f} µs\nBuilt-in: {1e6*t_sum/number:.3f} µs")
    

if __name__ == "__main__":
    main()