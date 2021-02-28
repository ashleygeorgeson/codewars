#!/usr/bin/env python

# """Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_')."""

# imports
import os
import sys
import argparse
from typing import final

# Module Constants
START_MESSAGE = "Split Strings Script"

# Module "Global" Variables
location = os.path.abspath(__file__)

def solution(s):
    list = []
    if len(s) %2 == 1: s = s + '_'
    for i in range(0, len(s), 2):
        list.append(s[i:i+2])
        i+=2
    return(list)

# Module Functions and Classes
def main(*args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", *args)
    print(solution(*args))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument('s')
    args = parser.parse_args()
    print(args.s)
    main(args.s)