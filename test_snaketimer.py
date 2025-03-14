import dis
import timeit
from lib import snaketimer

lst = list(range(100000))

def poppy(lst):
    lst = sorted(lst)

def main():
    
    from snakecharmer.ex999_dummy_exercise import solution
    
    number = 1000
    
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