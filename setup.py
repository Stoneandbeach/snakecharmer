import sys
import os
import subprocess
import json

welcome = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~Welcome to the Snakecharmer exercise session!~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The exercises consist of XYZ different tasks. For each task there is a script with a name
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
red Python libraries. First, create a virual environment. Be sure to use a version of
Python that is 3.11 or later.

> python3.11 -m venv .venv                 # Replace 3.11 with the version you want to use

Then, activate the virtual environment:

On Linux/MacOS:
> source .venv/bin/activate

On Windows:
    using cmd.exe:
> .venv\\Scripts\\activate.bat

    using PowerShell:
> .venv\\Scripts\\Activate.ps1

Finally, install the requirements:

> pip install -r requirements.txt
"""

def main():
    # Welcome
    print(welcome)

    input("Press ENTER to continue...\n")
    print(competition)
    
    input("Press ENTER to continue...\n")
    print(install_note)
    proceed = input("Do you want to proceed with the setup? (yes/NO) ")
    if not proceed.lower() == "yes":
        sys.exit("Setup aborted.")
    
    # Make a venv and install requirements
    try:
        import pip
    except ImportError as e:
        sys.exit(f"Failed to import pip. Please make sure pip is available in this Python install. Error {e}.")
    
    assert sys.version_info.major == 3, "Please use Python version >= 3.11."
    python_version = (sys.version_info.major, sys.version_info.minor)
    print(f"You are using Python version {'.'.join([str(i) for i in python_version])}")
    if python_version[1] < 11:
        print(f"Note that performance will be very different if you use a version of Python older than 3.11!")
        print(f"You can continue with this Python version, or abort the setup and relaunch it with a different version.")
        proceed = input(f"Do you wish to continue using Python {'.'.join([str(i) for i in python_version])}? (yes/NO)")
        if proceed.lower() != "yes":
            sys.exit("Setup aborted.")
    
    config_file = os.sep.join(["config", "config.json"])
    if os.path.exists(config_file):
        with open(config_file, "r") as fp:
            config = json.load(fp)
    else:
        config = {}
    if not "user" in config.keys():
        user = input("Please select a username: ")
        config["user"] = user
        print()
    
    with open(config_file, "w") as fp:
        json.dump(config, fp, indent=2)
    
    print("If you need a reminder on how to run the exercises, run 'python help.py'.")
    
    # Install requirements
        # Which means it needs to check for pip
        # And activate a venv
            # Which depends on os
                # Linux
                # MacOS
                # Windows
    
    # Dump manual
    

if __name__ == "__main__":
    main()