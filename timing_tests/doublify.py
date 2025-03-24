import dis

def doublify(x):
    return x * 2

def main():
    dis.dis(doublify)
    
    print()
    print([b for b in doublify.__code__.co_code])
    print()
    
if __name__ == "__main__":
    main()