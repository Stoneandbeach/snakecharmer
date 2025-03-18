"""The exercises consist of XYZ different tasks. For each task there is a script with a name
that starts with exN_ where N is the number of the exercise. These scripts contain a des-
cription of the task to be solved, and a working but slow solution.

Your task is to optimize these solutions, improving the time they require to run. Edit
the scripts, then test them by running

> python test_run.py exN_NAME.py

replacing 'exN_NAME.py' with the name of the script in question. This will evaluate your
solution using a simple sample input, checking that it runs and that it gives the correct
output. When you are ready to time the execution of your script, run

> python evaluate.py exN_NAME.py

Your results will be saved in the results/ folder. You will be able to upload your results
to a results board hosted on the site https://stenastrand.web.cern.ch/ where you can com-
pare your solutions to those of other participants.
"""

competition = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While you can compete in performance, this exercise is also about evaluating different
tools. You may solve exercises using only basic Python statements and expressions, use
built-in functions, import libraries from the Python standard library (like collections,
itertools), or use external libraries like NumPy. The evaluation will detect these imports
and add 'flair' to your submission, showing what tools you have used.

If you want to, you can also manually add flair by using the --flair argument:

> python evaluate.py exN_NAME.py --flair FLAIR_1 FLAIR_2

Use this if you want to highlight some specific design or idea of your solution. The more,
the merrier! Try to make your solutions as fast as possible, or challenge yourself by re-
stricting what you can use in order to test the many different tools that are available -
the choice is up to you!

If you have any questions, please ask the guy at the front of the room!

Cheers and happy timing,
Sten
"""

install_note = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To complete installation, please run the following commands. This will install all requi-
red Python libraries. First, activate the virtual environment:

On Linux/MacOS:
> source .venv/bin/activate

On Windows:
    using cmd.exe:
> .venv\\Scripts\\activate.bat

    using PowerShell:
> .venv\\Scripts\\Activate.ps1

Then, install the requirements:

> pip install -r requirements.txt
"""

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

def main():
    print(help_note)

if __name__ == "__main__":
    main()