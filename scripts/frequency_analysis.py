import argparse
import sys

try:
    from typing import Dict
except ImportError:
    pass

reference_frequency = {
    "E": 12.02,
    "T": 9.10,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.30,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.10,
    "Z": 0.07,
}


def parse_arguments():
    # type: () -> argparse.Namespace

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "FILE",
        help="The input file with the ciphertext (use '-' for standard input)",
        default="-")
    return parser.parse_args()


def read_ciphertext(options):
    # type: (argparse.Namespace) -> str

    if options.FILE == "-":
        with sys.stdin as fd:
            text = fd.readlines()
    else:
        with open(options.FILE) as fd:
            text = fd.readlines()
    ciphertext = ""
    for line in text:
        ciphertext += line.lower().rstrip()
    return ciphertext


def count_letters(text):
    # type: (str) -> Dict[str, Dict[ str, float]]
    """Count the letter frequencies in 'text'

    Count the letter frequency in 'text'. The output is a dictionary
    {'LETTER': { "count": COUNT, "frequency": FREQUENCY(in %) }.

    """

    result = {}  # type: Dict[str, Dict[str, float]]
    total = 0  # type: int
    for l in text:
        total += 1
        if l in result:
            result[l]["count"] += 1
        else:
            result[l] = {"count": 1}
    for l in result:
        result[l]["frequency"] = result[l]["count"] / total * 100
    return result


def main(options):
    # type: (argparse.Namespace) -> None

    ciphertext = read_ciphertext(options)
    letter_frequencies = count_letters(ciphertext)
    letters = sorted(letter_frequencies,
                     key=lambda l: letter_frequencies[l]["count"],
                     reverse=True)
    reference = sorted(reference_frequency,
                       key=reference_frequency.get, reverse=True)
    print("ciphertext    | reference")
    print("--------------------------")
    for l in letters:
        reference_string = "-"
        if len(reference) > 0:
            reference_string = "%6.3f (%s)" % (
                reference_frequency[reference[0]], reference[0].lower())
            del reference[0]
        print("%s %4d %6.3f | %s" % (
            l, letter_frequencies[l]["count"],
            letter_frequencies[l]["frequency"], reference_string))


if __name__ == "__main__":
    main(parse_arguments())
