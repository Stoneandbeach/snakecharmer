import dis
import timeit

# Choose the length of the list to be created
# Suggestion: see how this changes for (much) longer and shorter lists!
length = 10000

# "Naive" version using a for loop
def for_func(length):
    my_list = []
    for i in range(length):
        my_list.append(i)
    return my_list

# List comprehension
def comp_func(length):
    return [i for i in range(length)]

# Timing setup
for_setup = """
from __main__ import for_func, length
"""

comp_setup = """
from __main__ import comp_func, length
"""

def main():
    print("Bytecode of for loop version:")
    dis.dis(for_func)
    
    print("\n=======================================\n")
    
    print("Bytecode of list comprehension version:")
    dis.dis(comp_func)
    
    print(f"\nTesting the functions. These values should be the same: {sum(for_func(length))}, {sum(comp_func(length))}.")
    print("Timing...")
    
    # Number of executions to average time over. Needs to be a decent
    # number to get stable timings. For longer lists, I suggest you
    # reduce number so you don't have to wait until tomorrow morning.
    number = 10000

    t = timeit.repeat(stmt="for_func(length)", setup=for_setup, number=number)
    print(f"For loop version: {1e6*sum(t)/5/number:.3f} µs")

    t = timeit.repeat(stmt="comp_func(length)", setup=comp_setup, number=number)
    print(f"List comprehension version: {1e6*sum(t)/5/number:.3f} µs")

if __name__ == "__main__":
    main()