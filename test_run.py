from lib.solutionhandler import TestRunHandler
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
    parser.add_argument("--skip-numpy", action="store_true", default=False)
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
    use_numpy = False
    for line in script:
        if line[:6] == "## id:":
            id = line[6:].split("|")[0]
        if not args.skip_numpy and "import" in line and "numpy" in line and not line[0] == "#":
            use_numpy = True
            print("Found numpy import. Assuming you want the input data as a numpy.ndarray. \
To prevent this, add '--skip-numpy' when you run this script.")
    assert id, f"Could not read exercise ID from {file}.\nDid you change the EXERCISE ID block at the top of the file?"
    
    solution_handler = TestRunHandler(id, use_numpy=use_numpy)
    solution_args = solution_handler.get_args()
    print(f"Testing exercise {id}.")
    print()
    print(f"Sample input: {solution_args}")
    print()
    result = solution(*solution_args)
    print("Result:")
    print(solution_handler.post_process(result))
    
    
     
if __name__ == "__main__":
    main()