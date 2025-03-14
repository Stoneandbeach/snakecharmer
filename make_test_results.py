from lib.solutionhandler import SolutionHandler
from argparse import ArgumentParser
import os, sys

template = """
from {module} import solution
global solution
"""

test_input = {
    "1" : (list(range(1000)), 10),
    "3" : ('Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2. Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.',)
}

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
    
    solution_handler = SolutionHandler(id)
    solution_args = test_input[id]
    result = solution(*solution_args)
    post = solution_handler.post_process(result)
    print(f"Testing exercise {id}. Test output below:")
    print()
    for r in result.items():
        print(r)
    print()
    print(post)

if __name__ == "__main__":
    main()