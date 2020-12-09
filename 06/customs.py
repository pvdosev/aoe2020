#!/usr/bin/env python3
"""
This one looks a bit easier than yesterday's
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="This is a huge hassle irl",
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
    """List of repeating characters, separated by 2 newlines
    get all unique characters per list and sum them together"""

    args = get_args()

    answers = [set(entry.replace('\n', '')) for entry in args.file.read().split("\n\n")]
    total = 0

    for entry in answers:
        total += len(entry)

    print(answers)


# --------------------------------------------------
if __name__ == "__main__":
    main()
