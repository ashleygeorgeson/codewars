#!/usr/bin/env python

# Docstring
"""
Your task is to make a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0
"""

# imports
import logging, os, sys
import argparse
#from typing import final

# Module Constants
START_MESSAGE = "Sum of a Sequence"

# Module "Global" Variables
location = os.path.abspath(__file__)

def sequence_sum_old(begin_number, end_number, step):
    # debug display the passed sequence information
    logging.debug('Passed sequence in solution: %s %s %s', begin_number, end_number, step)
    # Sum sequence
    j = 0
    for i in range(begin_number, end_number+1, step):
        j += i
        logging.debug('Iteration: %s Sum: %s', i, j)
    return(j)

def sequence_sum_iterate(begin_number, end_number, step):
    # Iteration
    # debug display the passed sequence information
    logging.debug('Passed sequence in solution: %s %s %s', begin_number, end_number, step)
    # Sum sequence
    return sum([i for i in range(begin_number, end_number+1, step)])

def sequence_sum_recursion(begin_number, end_number, step):
    # Recursion
    if begin_number > end_number: return 0
    # return call sequence_sum with begin_number + step
    return begin_number + sequence_sum(begin_number + step, end_number, step)

def sequence_sum(b, e, s):
    # Recursion, simplified
    return b + sequence_sum(b + s , e, s) if b <= e else 0

def solution(roman):
    pass

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print("="*64,'\n', START_MESSAGE, "\nScript Location:", location, "\nArguments Passed: ", args, '\n',"="*64, sep='')
    logging.debug('Passed sequence in main: %s %s %s', args.begin, args.end, args.step)
    #sequence_sum(args.begin, args.end, args.step)
    sum = sequence_sum(args.begin, args.end, args.step)
    print(sum)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    #_, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Returns the sum of a sequence of integers')
    parser.add_argument('begin', type=int, help="Sequence begin")
    parser.add_argument('end', type=int, help="Sequence end")
    parser.add_argument('step', type=int, help="Sequence step")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    args = parser.parse_args()
    # Set logging level
    if args.debug == True: logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else: logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.debug('Arguments: %s', args)
    main(args)
