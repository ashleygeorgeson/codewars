#!/usr/bin/env python

# Docstring
"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

"""

# imports
import logging, os, sys
import argparse

# Module Constants
START_MESSAGE = "WeIrD StRiNg cAsE"

# Module "Global" Variables
location = os.path.abspath(__file__)

def to_weird_case(string):
    weird_string = ''
    for char in range(0, len(string), 2):
        weird_string += string[char].upper()
        weird_string += string[char+1].lower()
    return weird_string

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print("="*64,'\n', START_MESSAGE, "\nScript Location:", location, "\nArguments Passed: ", args, '\n',"="*64, sep='')
    logging.debug('Passed string: %s', args.string)
    weird_string = to_weird_case(args.string)
    #print(solution(args.number))
    #print(solution2(args.number))
    #print(wip(args.number))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    #_, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='WeIrD StRiNg cAsE')
    parser.add_argument('string', type=str, help="Sring to convert to WeIrD StRiNg cAsE")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    args = parser.parse_args()
    # Set logging level
    if args.debug == True: logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else: logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.debug('Arguments: %s', args)
    main(args)