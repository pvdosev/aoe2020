#!/usr/bin/env python3
"""
Keep on keeping on! This is fun
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Plaintext passwords bad",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file with passwords",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="input",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get passwords and requirements from file,
    evaluate passwords based on reqs,
    return number of wrong passwords"""

    args = get_args()

    inputlist = args.file.read().splitlines()

    passwords = [string.split(": ")[1] for string in inputlist]

    letters = [string.split(": ")[0].split()[1] for string in inputlist]

    passmax = [
        int(string.split(": ")[0].split()[0].split("-")[1]) for string in inputlist
    ]
    passmin = [
        int(string.split(": ")[0].split()[0].split("-")[0]) for string in inputlist
    ]

    i = 0
    finalcount = 0

    for password in passwords:
        if (
            password.count(letters[i]) <= passmax[i]
            and password.count(letters[i]) >= passmin[i]
        ):
            print(
                f"Word: {password} Letter: {letters[i]} Min/max: {passmin[i]}, {passmax[i]} \n {inputlist[i]}"
            )
            finalcount += 1

        i += 1

    print(finalcount)


# --------------------------------------------------
if __name__ == "__main__":
    main()
