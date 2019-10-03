import argparse
import sys


def parse_arguments():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def read_ciphertext():
    ciphertext = ""
    with sys.stdin as fd:
        ciphertext += fd.readline().rstrip()
    return ciphertext


def main(options):
    ciphertext = read_ciphertext()
    print(ciphertext)
    # Count letters
    # Sort by frequency
    # Print frequencies


if __name__ == "__main__":
    main(parse_arguments())
