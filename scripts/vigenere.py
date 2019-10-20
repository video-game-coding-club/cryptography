#!/usr/bin/python

import argparse
import sys
from textwrap import wrap


def shift_character(a, shift):
    """Shift the character by shift positions in the alphabet.

    The input letter a is shifted by shift positions in the alphabet.
    The letter is upper cased first. The alphabet wraps beyond 'z'
    back to 'a'. If the input letter is a digit, that digit is
    returned. If the input letter is a punctuation character in [',',
    '.', '(', ')', "'", '"', "?", ";", ":", "!", "-"] that character
    is returned. If the input letter is anything else an Exception is
    raised. The output is the shifted letter.

    """
    a = a.upper().strip()
    if len(a) == 0:
        return ""
    if len(a) > 1:
        raise Exception("Input too long, expected 1 character")
    if a.isdigit():
        return a
    if a.isalpha():
        return chr(ord("A") + (ord(a) - ord("A") + shift) % 26)
    if a in [",", ".", ";", ":", "!", "(", ")", "'", '"', "?", "-"]:
        return a
    raise Exception("Illegal input (received '%s')" % a)


def parse_arguments():
    # type: () -> argparse.Namespace
    parser = argparse.ArgumentParser(description="""This script
applies the Viegenere Cipher to a plaintext given on standard
input.""")
    parser.add_argument(
        "FILE",
        default="-",
        help="The input file (use '-' for standard input)")
    parser.add_argument(
        "--passphrase",
        default="A",
        help="The passphrase")
    parser.add_argument(
        "--encrypt",
        action="store_true",
        help="Encrypt the input (this is the default)")
    parser.add_argument(
        "--decrypt",
        action="store_true",
        help="Decrypt the input")
    options = parser.parse_args()
    if not (options.encrypt or options.decrypt):
        options.encrypt = True
    return options


def check_passphrase(passphrase):
    # type: (str) -> str
    """The passphrase can contain only letters and is uppercased, i.e. an
    'a' corresponds to the same shift as an 'A'.

    This function will check whether it contains illegal characters
    and return an upper case version of the passphrase.

    """
    for letter in passphrase:
        if not letter.isalpha():
            raise Exception("The passphrase contains a character " +
                            "not contained in the alphabet")
    return passphrase.upper()


def encrypt(cleartext, passphrase):
    # type: (str, str) -> str
    ciphertext = ""
    shift_index = 0
    for line in [line.strip() for line in cleartext]:
        for c in line:
            ciphertext += shift_character(
                c, ord(passphrase[shift_index % len(passphrase)]) - ord("A"))
            shift_index += 1
    return ciphertext


def decrypt(ciphertext, passphrase):
    # type: (str, str) -> str
    cleartext = ""
    shift_index = 0
    for line in [line.strip() for line in ciphertext]:
        for c in line:
            cleartext += shift_character(
                c, -(ord(passphrase[shift_index % len(passphrase)])
                     - ord("A")))
            shift_index += 1
    return cleartext


def main(options):
    # type: (argparse.Namespace) -> None
    passphrase = check_passphrase(options.passphrase)

    if options.FILE == "-":
        with sys.stdin as fd:
            cleartext = fd.readlines()
    else:
        with open(options.FILE) as fd:
            cleartext = fd.readlines()

    if options.encrypt:
        ciphertext = encrypt(" ".join(cleartext), passphrase)
    elif options.decrypt:
        ciphertext = decrypt(" ".join(cleartext), passphrase)

    for line in wrap(ciphertext, break_long_words=True,
                     break_on_hyphens=False):
        print(line)


if __name__ == "__main__":
    main(parse_arguments())
