import dis
import timeit
from lib import snaketimer

lst = [[-400 for _ in range(3)] for _ in range(3)]
# lst = list(range(1000))

def poppy(matrix):
    #print(f"Length of incoming list: {len(lst)}")
    #lst.extend(list(range(10000)))
    print(matrix)
    print(sum(matrix[0]), end=", ")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 255:
                matrix[i][j] = 255
    print(sum(matrix[0]))
    return matrix

def main():
    
    from ex999_dummy_exercise import solution
    
    print(lst)
    
    number = 1
    
    print("Run 1...")
    t = snaketimer.repeat(
        stmt = poppy,
        args = (lst,),
        number = number,
        repeat = 5
    )
    print(f"Run 1 complete. Time: {1e6*sum(t)/5/number:.3f} µs")
    
    print("Run 2...")
    t = snaketimer.repeat(
        stmt = poppy,
        args = (lst,),
        number = number,
        repeat = 5
    )
    print(f"Run 2 complete. Time: {1e6*sum(t)/5/number:.3f} µs")
    
    print("Run 1...")
    t = timeit.repeat(
        stmt = "poppy(lst)",
        setup = "from __main__ import poppy, lst",
        number = number,
        repeat = 5
    )
    print(f"Run 1 complete. Time: {1e6*sum(t)/5/number:.3f} µs")
    
    print("Run 2...")
    t = timeit.repeat(
        stmt = "poppy(lst)",
        setup = "from __main__ import poppy, lst",
        number = number,
        repeat = 5
    )
    print(f"Run 2 complete. Time: {1e6*sum(t)/5/number:.3f} µs")
    
    

if __name__ == "__main__":
    main()