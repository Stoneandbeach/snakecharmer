import matplotlib.pyplot as plt
import numpy as np
import html
import time
import json
import requests
from lib import snaketimer
from lib.solutionhandler import SolutionHandler
from argparse import ArgumentParser
import os, sys
sys.path.append(os.getcwd())

template = """
from {module} import solution
global solution
"""

time_to_evaluate = 10
length = 10000
lst = list(range(length))
n = 100

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--skip-numpy", action="store_true", default=False)
    parser.add_argument("--flair", nargs="*")
    parser.add_argument("--dry-run", action="store_true", default=False)
    parser.add_argument("--plot-estimation", action="store_true", default=False)
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
        
    # Parse script to find exercise id, analyse imports and assign flair to setup evaluation
    id = None
    imported_modules = []
    use_numpy = False
    in_code = False
    for l, line in enumerate(script):
        if line[:6] == "## id:":
            id = line[6:].split("|")[0]
        elif "## ----------------------------CODE------------------------- ##" in line:
            in_code = True
        elif line[0] != "#" and (parts := line.split()):
            if parts[0] == "from" or parts[0] == "import":
                assert not in_code, f"Please put all imports under IMPORTS at the top of the script. Issue on line {l}:\n{line}"
                assert "," not in line, f"Failed to analyse imports on line {l}. Please only import one module per line. Line in question:\n{line}"
                module_name = parts[1]
                print(f"Identified module {module_name} on line {l}.")
                imported_modules.append(module_name)
                if not args.skip_numpy and module_name == "numpy":
                    use_numpy = True
                    print("Found numpy import. Assuming you want the input data as a numpy.ndarray. \
To prevent this, add '--skip-numpy' when you run this script.")
    assert id, f"Could not read exercise ID from {file}.\nDid you change the EXERCISE ID block at the top of the file?"
        
    flair = []
    if args.flair:
        flair.extend(args.flair)
    else:
        print(f"\nNote: you can manually add flair to your submission using '--flair FLAIR_1 FLAIR_2' if you want to indicate that you're using some specific design, function or library.\n")
    if imported_modules:
        flair.extend(imported_module for imported_module in imported_modules if imported_module not in flair)
    else:
        flair.append("no-imports")
    print(flair)
    
    # Get rough execution time in order to choose number of iterations to average over
    print(f"Estimating average execution time...")
    average_over_num = 50
    solution_handler = SolutionHandler(id, use_numpy=use_numpy)
    t_estimate = []
    for i in range(average_over_num):
        sol_args = solution_handler.get_args()
        t_estimate.append(
            snaketimer.timeit(
                stmt=solution,
                args=sol_args,
                number=1
            )
        )
    
    print(f"Average execution time during estimation: {1e6*sum(t_estimate)/average_over_num:.3f} µs.")
    
    iterations = max(5, int(time_to_evaluate / (sum(t_estimate) / average_over_num)))
    if iterations > 100000:
        iterations = 100000
        print(f"Running 100000 iterations.")
    else:
        print(f"Estimated number of iterations needed in order to run for >= {time_to_evaluate} s: {iterations}")
    
    if args.plot_estimation:
        plt.plot([t*1e6 for t in t_estimate], 'x', label="Prel. run")
        plt.xlabel("Run number")
        plt.ylabel("Execution time [µs]")
        plt.legend()
        plt.show()
    
    start = time.perf_counter()
    t = []
    for i in range(iterations):
        t.append(
            snaketimer.timeit(
                stmt=solution,
                args=solution_handler.get_args(),
                number=1
            )
        )
    end = time.perf_counter()
    print(f"Total evaluation time: {end - start:.3f} s")
    
    print(f"Total time in work function: {sum(t):.3f} s")
    execution_time = 1e6*sum(t)/iterations
    print(f"Average execution time: {execution_time:.3f} µs")
    
    # Post-processing
    print()
    result = solution(*solution_handler.get_args())
    print(solution_handler.post_process(result))
    
    # Clean up exercise script and write to local results file
    script = [line for line in script if not (line[:2]=="##" and line[-3:]=="##\n")]

    output = {
        "exercise" : id,
        "user" : "Sten",
        "time" : f"{execution_time:.3f} µs",
        "flair" : flair,
        "code" : "".join(script)
    }

    if not args.dry_run:
        run_nr = 0
        results_file_name = ".".join([module, str(run_nr), "json"])
        result_file_path = os.sep.join(["results", results_file_name])
        while os.path.exists(result_file_path):
            run_nr += 1
            result_file_path = os.sep.join(["results", ".".join([module, str(run_nr), "json"])])
        with open(result_file_path, "w") as fp:
            json.dump(output, fp, indent=2)
        print(f"Wrote results to file: {result_file_path}")
        upload = ""
        while upload not in ["yes", "no"]:
            upload = input("Would you like to upload this result to the Snakecharmer Results Board? (yes/NO) ").lower()
        if upload == "yes":
            r = requests.put("".join(["https://cernbox.cern.ch/remote.php/dav/public-files/lokc8ro60Xj1Wwr/", results_file_name]), headers={'content-type': 'application/json'}, data=output)
            if r.status_code == requests.codes.ok:
                print("Results uploaded.")
            else:
                r.raise_for_status()
        
        print("\nEvaluation complete.")
    
    
if __name__ == "__main__":
    main()