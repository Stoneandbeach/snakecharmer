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
"""

venv_note = """
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

def main():
    print(help_note)
    print()
    if os.getenv("SWAN_LIB_DIR"):
        print(swan_note)
    else:
        print(venv_note)

if __name__ == "__main__":
    main()