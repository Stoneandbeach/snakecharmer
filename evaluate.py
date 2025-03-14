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
        
    # Find flair in script file
    flair = ""
        
    # Fetch exercise id to setup evaluation
    id = None
    for line in script:
        if line[:6] == "## id:":
            id = line[6:].split("|")[0]
            break
    assert id, f"Could not read exercise ID from {file}.\nDid you change the EXERCISE ID block at the top of the file?"
    
    # Get rough execution time in order to choose number of iterations to average over
    average_over_num = 50
    
    # Prime the snaketimer scope, i.e. run once to let the Python Virtual Machine do some initial optimizations,
    # avoiding counting those in the subsequent timing runs
    # solution_args = (lst, n)
    # snaketimer.timeit(
    #     stmt=solution,
    #     args=solution_args,
    #     number=1
    # )
    
    argument_handler = SolutionHandler(id)
    t_ordered = []
    solution_args = argument_handler.get_args()
    print(type(solution_args))
    print(len(solution_args))
    print(solution_args)
    
    for i in range(average_over_num):
    
        t_ordered.append(
            snaketimer.timeit(
                stmt=solution,
                args=argument_handler.get_args(),
                number=1
            )
        )
    
    argument_handler = SolutionHandler("1")
    t_shuffled = []
    for i in range(average_over_num):
        
        t_shuffled.append(
            snaketimer.timeit(
                stmt=solution,
                args=argument_handler.get_args(),
                number=1
            )
        )
    
    plt.plot([t*1e6 for t in t_ordered], 'x', label="Ordered")
    plt.plot([t*1e6 for t in t_shuffled], 'x', label="Shuffled")
    plt.xlabel("Run number")
    plt.ylabel("Execution time [µs]")
    plt.legend()
    plt.show()
    
    print(f"Average runtime of\n\tordered input:{1e6*sum(t_ordered)/average_over_num:.3f}\n\tshuffled input:{1e6*sum(t_shuffled)/average_over_num:.3f}")
    
    iterations = max(5, int(5 / (sum(t_ordered) / average_over_num)))
    print(f"Iterations: {iterations}")
    
    start = time.perf_counter()
    t = []
    for i in range(iterations):
        
        t.append(
            snaketimer.timeit(
                stmt=solution,
                args=argument_handler.get_args(),
                number=1
            )
        )
    end = time.perf_counter()
    print(f"Time to time: {end - start:.3f} s.")
    
    print(f"Total time in work function: {sum(t):.3f} s.")
    execution_time = 1e6*sum(t)/iterations
    print(f"{execution_time:.3f} µs")
    
    # Post-processing
    print()
    result = solution(*solution_args)
    argument_handler.post_process(result)
    print()
    
    # Clean up exercise script and write to local results file
    script = [line for line in script if not (line[:2]=="##" and line[-3:]=="##\n")]

    script = "".join([
        f"Exercise: {module}\n",
        f"Execution time: {execution_time:.3f} µs\n",
        f"Flair: {flair}\n",
        "Code:\n"
    ] + script + ["\n\n"])

    run_nr = 0
    result_file_path = os.sep.join(["results", ".".join([module, str(run_nr), "result"])])
    while os.path.exists(result_file_path):
        run_nr += 1
        result_file_path = os.sep.join(["results", ".".join([module, str(run_nr), "result"])])
    with open(result_file_path, "w") as fp:
        fp.write(script)
    print(f"Wrote to file: {result_file_path}")
    
    
if __name__ == "__main__":
    main()