import sys
import subprocess
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()

def main():
    args = parse_args()
    r = subprocess.run(['./uploader', args.filename])
    print(r)

if __name__ == "__main__":
    main()