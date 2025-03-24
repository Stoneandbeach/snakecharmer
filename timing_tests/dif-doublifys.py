from doublify import doublify

def main():
    x = 2
    print(f"x = {x}")
    print(f"doublify(x) = {doublify(x)}")
    
    print()
    
    x = 2.1
    print(f"x = {x}")
    print(f"doublify(x) = {doublify(x)}")
    
    print()
    
    x = "Hello"
    print(f"x = {x}")
    print(f"doublify(x) = {doublify(x)}")
    
    print()
    
    x = ("Hello",)
    print(f"x = {x}")
    print(f"doublify(x) = {doublify(x)}")

if __name__ == "__main__":
    main()