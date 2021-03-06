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
    """List of lists of repeating chars, separated by 2 newlines
    get all non repeating characters per list of lists, sum number"""

    args = get_args()

    answers = [entry.rstrip().split("\n") for entry in args.file.read().split("\n\n")]

    for answerlist in answers:
        for count, string in enumerate(answerlist):
            answerlist[count] = set(answerlist[count])

    # Find set intersection using list expansion
    final = [set.intersection(*setlist) for setlist in answers]

    sum = 0
    for each in final:
        sum += len(each)

    print(sum)


# --------------------------------------------------
if __name__ == "__main__":
    main()
