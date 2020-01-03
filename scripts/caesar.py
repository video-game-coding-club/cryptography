#!/usr/bin/env python

import argparse
import sys
import textwrap


def shift_character(a, shift):
    # type: (str, int) -> str
    """Shift the character by shift positions in the alphabet.

    The input letter a is shifted by shift positions in the alphabet.
    The letter is upper cased first. The alphabet wraps beyond 'z'
    back to 'a'. If the input letter is a digit, that digit is
    returned. If the input letter is a punctuation character in [',',
    '.', '(', ')', "'", '"', "?", ";", ":", "!", "-", "/"] that
    character is returned. If the input letter is anything else an
    Exception is raised. The output is the shifted letter.

    """
    a = a.upper().strip()
    if len(a) == 0:
        return ""
    if len(a) > 1:
        raise Exception("Input too long (got '%s', expected 1 character" % a)
    if a.isdigit():
        return a
    if a.isalpha():
        return chr(ord("A") + (ord(a) - ord("A") + shift) % 26)
    if a in [",", ".", ";", ":", "!", "(", ")", "'", '"', "?", "-", "/"]:
        return a
    raise Exception("Illegal input (received '%s')" % a)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="""This script applies the Caesar Cipher to a
plaintext given on standard input. If the shift is negative, the
script can be used to decrypt a ciphertext.""")
    parser.add_argument(
        "FILE",
        default="-",
        help="The input file (use '-' for standard input)")
    parser.add_argument(
        "--shift",
        type=int,
        default=0,
        help="The shift of the alphabet")
    return parser.parse_args()


def main():
    options = parse_arguments()
    if options.FILE == "-":
        with sys.stdin as fd:
            cleartext = fd.readlines()
    else:
        with open(options.FILE) as fd:
            cleartext = fd.readlines()
    ciphertext = ""
    for line in [line.strip() for line in cleartext]:
        for c in line:
            ciphertext += shift_character(c, options.shift)

    for line in textwrap.wrap(
            ciphertext, break_long_words=True, break_on_hyphens=False):
        print(line)


if __name__ == "__main__":
    main()
