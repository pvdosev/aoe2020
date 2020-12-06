#!/usr/bin/env python3
"""
This one sounds kinda easy tbh
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
    byr (Birth Year): 1920 - 2002
    iyr (Issue Year): 2010 - 2020
    eyr (Expiration Year): 2020 - 2030
    hgt (Height): 150cm - 193cm, or 59in - 73in
    hcl (Hair Color): valid hex color code
    ecl (Eye Color): amb blu brn gry grn hzl oth
    pid (Passport ID): 9 digits
    cid (Country ID) <- optional"""

    args = get_args()

    passports = args.file.read().split("\n\n")
    total = 0
    
    data = [re.sub(r"\n", " ", passport).rstrip() for passport in passports]

    for entry in data:
        birth = re.search(r"(?<=byr:)\d{4}", entry)
        # assign each 


# --------------------------------------------------
if __name__ == "__main__":
    main()
