#!/usr/bin/env python3
"""
Let's do this, day 1 of advent of code
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bureaucracy always gets me going",
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
    """Get array of numbers from file,
    figure out which pair adds up to 2020,
    and add them together.

    (Bonus points: Find a triplet that satisfies ^)"""

    args = get_args()

    numbers = list(map(int, args.file.read().split()))

    i = 0
    final = 0

    """There has to be a better way to do this than a 
    triple nested for loop... Gotta learn recursion"""
    for number in numbers:

        for number2 in numbers[i:]:
            for number3 in numbers[i:]:

                if number + number2 + number3 == 2020:
                    final = [number, number2, number3]
                    break

            if final:
                break

        if final:
            break
        i += 1

    print(final[0] * final[1] * final[2])


# --------------------------------------------------
if __name__ == "__main__":
    main()
