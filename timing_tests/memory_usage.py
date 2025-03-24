import sys
import numpy as np

def main():    
    # Note: sys.getsizeof returns the size in byte of an object, but does
    # not take nested structures into account. See example below:
    list_a = ["a", "b", "c"]
    list_b = ["abcdefgh", "ikjlmnop", "qrstuvwx"]
    
    print("Demonstration - just getting the size of a list does not account for size of contents.")
    print(f"List a: {list_a}. sys.getsizeof returns: {sys.getsizeof(list_a)} bytes.")
    print(f"List b: {list_b}. sys.getsizeof returns: {sys.getsizeof(list_b)} bytes.")
    print("Actual sizes:")
    print(f"List a: {sys.getsizeof(list_a) + sum([sys.getsizeof(x) for x in list_a])} bytes.")
    print(f"List b: {sys.getsizeof(list_b) + sum([sys.getsizeof(x) for x in list_b])} bytes.")
    
    length = 100000
    lst = list(range(length))
    array = np.array(lst)
    
    print()
    print(f"Considering a list or array of {length} integers:")
    print(f"Size of Python list: {(sys.getsizeof(lst) + sum([sys.getsizeof(x) for x in lst]))//1024} kilobytes.")
    
    # The NumPy array is interely contained in a C struct, so Python doesn't know that
    # it has numbers inside. Therefore we don't need to consider the individual numbers.
    print(f"Size of NumPy array: {sys.getsizeof(array)//1024} kilobytes.")

if __name__ == "__main__":
    main()