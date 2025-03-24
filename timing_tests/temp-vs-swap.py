import dis
import timeit

def temp(a, b):
    t = a
    a = b
    b = t
    return a, b

def swap(a, b):
    a, b = b, a
    return a, b

def main():
    print("Bytecode of function using temporary holder:")
    dis.dis(temp)
    
    print("\n======================\n")
    
    print("Bytecode of function using swap assignment.")
    dis.dis(swap)
    
    # Number of iterations to average execution time over
    number = 100000000
    print("Timing...")
    t = timeit.repeat(stmt="func(1, 2)", setup="from __main__ import swap as func", number=number)
    print(f"\nSwap: {1e6*sum(t)/5/number:.4f} µs")
    
    t = timeit.repeat(stmt="func(1, 2)", setup="from __main__ import temp as func", number=number)
    print(f"Temp: {1e6*sum(t)/5/number:.4f} µs")
    

if __name__ == "__main__":
    main()