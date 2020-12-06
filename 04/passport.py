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

    passports = args.file.read().split("\n\n")
    total = 0

    for passport in passports:
        # I'm still a bit confused about lookaheads
        if re.match(
            r"(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$",
            re.sub(r"\n", " ", passport),
        ):
            total += 1

    print(total)


# --------------------------------------------------
if __name__ == "__main__":
    main()
