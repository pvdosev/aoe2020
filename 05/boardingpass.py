#!/usr/bin/env python3
"""
The first one was easy, not this one D:
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Please hold for passport check",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="input",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get input file, process to remove newlines
    validate each passport:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) <- optional"""

    args = get_args()

    passes = args.file.read().split()
    for doc in passes:
        vertical = doc[0:7]
        horizontal = doc[7:10]
        highbound = 127
        lowbound = 0

        for count, char in enumerate(vertical):
            if char == "F":
                lowbound += len(range(lowbound, highbound))
            if char == "B": 
                highbound -= len(range(lowbound, highbound))

        print(lowbound, highbound)


            

    


# --------------------------------------------------
if __name__ == "__main__":
    main()
