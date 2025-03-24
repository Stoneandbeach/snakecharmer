import os

help_note = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, choose an exercise script and edit it to improve its execution time.

Test it by running:
> python test_run.py exN_NAME.py

When ready, time it and post results by running:
> python evaluate.py exN_NAME.py

You can always rerun the evaluation if you make further improvements.

Add custom flair:
> python evaluate.py exN_NAME.py --flair MY_FLAIR MY_OTHER_FLAIR

Inspect the bytecode of a script:
> python show_bytecode.py SCRIPT.py
"""

venv_note = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activate the virtual environment (necessary if you restart the terminal):

On Linux/MacOS:
> source .venv/bin/activate

On Windows:
    using cmd.exe:
> .venv\\Scripts\\activate.bat

    using PowerShell:
> .venv\\Scripts\\Activate.ps1

Then, you can install required libraries:
> pip install -r requirements.txt

...or install other libraries, using scipy as an example:
> pip install scipy
"""

swan_note = """
To see what Python libraries are available, use:
> pip list
"""

swan_tips_and_tricks = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Some tips and tricks~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

External libraries available on SWAN:
NumPy, Pandas, Scipy… check ‘pip list’ for complete list

Python standard library modules:
https://docs.python.org/3/library/index.html
collections - useful for managing sets of things
math - useful for… math
itertools - provides tools for iterators

Built-in functions and other usefuls:
https://docs.python.org/3/library/functions.html
sum(), len(), max(), [list comprehension], {dictionaries}...
"""

tips_and_tricks = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Some tips and tricks~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

External libraries:
NumPy, Pandas, Scipy…

Python standard library modules:
https://docs.python.org/3/library/index.html
collections - useful for managing sets of things
math - useful for… math
itertools - provides tools for iterators

Built-in functions and other usefuls:
https://docs.python.org/3/library/functions.html
sum(), len(), max(), [list comprehension], {dictionaries}...
"""

def main():
    print(help_note)
    input("\nPress ENTER to continue...")
    if os.getenv("SWAN_LIB_DIR"):
        print(swan_tips_and_tricks)
    else:
        print(venv_note)
        input("\nPress ENTER to continue...")
        print(tips_and_tricks)
        
    
    


if __name__ == "__main__":
    main()