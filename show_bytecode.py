import dis
import types
from argparse import ArgumentParser

template = """import {file} as module
global module"""

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args()

def main():
    args = parse_args()
    file = args.file.replace(".py", "")
    exec(template.format(file=file))
    for key in dir(module):
        item = getattr(module, key)
        if isinstance(item, types.FunctionType):
            print(f"Bytecode of function {key}:")
            dis.dis(item)
            print()
    

if __name__ == "__main__":
    main()