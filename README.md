# snakecharmer

### Welcome to the Snakecharmer Python exercise repo!

This repo is built around a set of exercises on the topic of optimizing Python code. Each exercise comes in a script (filename beginning with ex and a number) that contains a description of the task, and a fully working *but nonoptimal* solution. The goal is to explore different ways to approach writing faster Python code. You can try to make the solutions as fast as Pythonly possible, or you can set yourself a different challenge! See what you can do using only the Python standard library, or only built-in functions, or perhaps write your own, external C++ code that you call from within the exercise script...

### Installation

Simply clone the git repo (or download as a zip file) and run `python setup.py` to get further instructions. You may be asked to set up a virtual environment, into which a few external, required libraries need to be installed.\
`git clone https://github.com/Stoneandbeach/snakecharmer.git`\
`cd snakecharmer`\
`python setup.py`

Note that using Python 3.11 is recommended. This version of Python came with a large change to how Python code is interpreted and run, so using an older version will not yield the same timing results (though should very likely work, so there's no harm). Using a newer version than 3.11 should be fine, remembering that at some point, there will be new updates to Python. In essence, results are only truly comparable while using the same Python version.

### Usage

Each exercise is contained in a Python script. Read the task described inside, edit the script to your heart's content (obeying the rules written within...), then test your solution by running\
`python test_run.py SCRIPT_NAME.py`\
replacing SCRIPT_NAME with the exercise script in question.

When you are ready to time your solution, run\
`python evaluate.py SCRIPT_NAME.py`

This will store your results in the `results` folder. Explore, optimize and rerun!

There is also an additional tool that lets you view the [bytecode](https://opensource.com/article/18/4/introduction-python-bytecode) of the exercise scripts, perhaps useful as an inspiration to understanding performance:\
`python show_bytecode.py SCRIPT_NAME.py`

### Inverted CERN School of Computing 2025

This repo was built for an exercise session at the [Inverted CERN School of Computing 2025](https://indico.cern.ch/event/1468713/overview). I also had a talk at the school, covering how Python works internally and what consequences that has for performance: [Under the Hood of the Snake](https://indico.cern.ch/event/1468713/contributions/6275292/). The recording of this talk may be available at that link for those interested in delving deeper.