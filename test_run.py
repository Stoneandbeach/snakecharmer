import matplotlib.pyplot as plt
import time
import random
from lib import snaketimer
from lib.solutionhandler import SolutionHandler
from argparse import ArgumentParser
import os, sys
sys.path.append(os.getcwd())

template = """
from {module} import solution
global solution
"""

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args()

def main():
    args = parse_args()
    assert hasattr(args, "file"), "Please specify one file to evaluate, i.e. 'python evaluate.py FILENAME.py"
    file = args.file
    assert os.path.exists(file), f"No file named {file}."
    module = file.replace(".py", "")
    
    # Execute import to access solution function
    try:
        exec(template.format(module=module))
    except ImportError as e:
        sys.exit(f"Could not import function 'solution' from {file}. Error: {e}")
    
    with open(file, "r") as fp:
        script = fp.readlines()
        
    # Fetch exercise id to setup evaluation
    id = None
    for line in script:
        if line[:6] == "## id:":
            id = line[6:].split("|")[0]
            break
    assert id, f"Could not read exercise ID from {file}.\nDid you change the EXERCISE ID block at the top of the file?"
    
    argument_handler = SolutionHandler(id, test_mode=True)
    solution_args = argument_handler.get_args()
    result = solution(*solution_args)
    print(f"Testing exercise {id}. Test output below:")
    print()
    print(result)
    
    
     
if __name__ == "__main__":
    main()