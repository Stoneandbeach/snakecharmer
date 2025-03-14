import json
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args()

def main():
    args = parse_args()
    output = {}
    with open(args.file, "r") as fp:
        output["code"] = fp.read()
    with open("code.json", "w") as fp:
        json.dump(output, fp)

if __name__ == "__main__":
    main()