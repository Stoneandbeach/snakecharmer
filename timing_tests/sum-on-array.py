import numpy as np
import timeit

# Length of list/array to sum
length = 100000

# Timing setup
setup_sum_list = """
from __main__ import length
array = list(range(length))
"""

setup_sum_array = """
import numpy as np
from __main__ import length
array = np.arange(length)
"""
            
setup_np =  """
import numpy as np
from __main__ import length
array = np.arange(length)
"""

setup_np_list = """
import numpy as np
from __main__ import length
array = list(range(length))
"""

def builtin_sum(data):
    return sum(data)

def numpy_sum(array):
    return array.sum()

def main():
    # Number of iterations to average execution time over.
    # Needs to be a decent number to get stable timings.
    number = 1000
    
    t = timeit.repeat(stmt="sum(array)", setup=setup_sum_list, number=number)
    print(f"Built-in sum() of list: {1e6*sum(t)/5/number:.3f} µs")
    
    t = timeit.repeat(stmt="sum(array)", setup=setup_sum_array, number=number)
    print(f"Built-in sum() of numpy array: {1e6*sum(t)/5/number:.3f} µs")
    
    t = timeit.repeat(stmt="array.sum()", setup=setup_np, number=number)
    print(f"Numpy array.sum(): {1e6*sum(t)/5/number:.3f} µs")
    
    t = timeit.repeat(stmt="np.sum(array)", setup=setup_np_list, number=number)
    print(f"Numpy.sum(list): {1e6*sum(t)/5/number:.3f} µs")
    
if __name__ == "__main__":
    main()