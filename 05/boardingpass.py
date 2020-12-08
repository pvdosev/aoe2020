#!/usr/bin/env python3
"""
The first one was easy, not this one D:
"""

import argparse

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
    """Struggling to get anything done here,
    someone explain bsp to"""

    args = get_args()

    currentid = 0
    highestid = 0

    passes = args.file.read().split()
    for doc in passes:
        vertical = doc[0:7]
        horizontal = doc[7:10]
        highbound = 127
        lowbound = 0
        leftbound = 0
        rightbound = 7

        for count, char in enumerate(vertical):
            if char == "F":
                highbound -= pow(2, 6 - count)
            if char == "B":
                lowbound += pow(2, 6 - count)

        for count, char in enumerate(horizontal):
            if char == "L":
                rightbound -= pow(2, 2 - count)
            if char == "R":
                leftbound += pow(2, 2 - count)

        currentid = highbound * 8 + rightbound  # given by puzzle definition

        if currentid > highestid:
            highestid = currentid

    print(highestid)


# --------------------------------------------------
if __name__ == "__main__":
    main()
