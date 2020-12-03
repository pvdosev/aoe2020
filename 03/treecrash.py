#!/usr/bin/env python3
"""
Rushing through the snow, in a one horse open sleigh...
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="These branches hurt pretty bad",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file full of numbers",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="input",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get list of strings from input file
    If you start from the top left, going 1 down and 3 right,
    wrapping at the right edge, how many #'s do you pass?"""

    args = get_args()

    # strings are iterable, so no need for special processing
    snowyfield = args.file.read().splitlines()

    i = 0
    treecount = 0
    for line in snowyfield:
        if line[i % len(line)] == "#":
            treecount += 1
        i += 3
    print(treecount)

# --------------------------------------------------
if __name__ == "__main__":
    main()
