#!/usr/bin/env python

import argparse


def shift_character(a, shift):
    """Shift the character by shift positions in the alphabet.

    The input letter a is shifted by shift positions in the alphabet.
    The letter is lowercased first. The alphabet wraps beyond 'z' back
    to 'a'. If the input letter is a digit, that digit is returned. If
    the input letter is a punctuation character in [',', '.', '(',
    ')'] that character is returned. If the input letter is anything
    else an Exception is raised. The output is the shifted letter.

    """
    a = a.lower().strip()
    if len(a) == 0:
        return ""
    if len(a) > 1:
        raise Exception("Input too long, expected 1 character")
    if a.isdigit():
        return a
    if a.isalpha():
        return chr(ord("a") + (ord(a) - ord("a") + shift) % 26)
    if a in [',', '.', '(', ')']:
        return a
    raise Exception("Illegal input (received '%s')" % a)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="""This script applies the Caesar Cipher to a
plaintext given on standard input. If the shift is negative, the
script can be used to decrypt a ciphertext.""")
    parser.add_argument(
        "--shift",
        type=int,
        default=0,
        help="The shift of the alphabet")
    return parser.parse_args()


def main():
    options = parse_arguments()


if __name__ == "__main__":
    main()
