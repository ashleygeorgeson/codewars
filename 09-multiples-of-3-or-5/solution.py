#!/usr/bin/env python

# Docstring
"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net

"""

# imports
import logging, os, sys
import argparse
#from typing import final

# Module Constants
START_MESSAGE = "Euler Project - Multiples of 3 or 5"

# Module "Global" Variables
location = os.path.abspath(__file__)

def solution(number):
    return sum([num for num in range(number) if not num % 3 or not num % 5]) # returns a list of only multiples of 3 and 5

def solution2(number):
    '''
    Returns the sum of all the multiples of 3 or 5 below the number passed in. 
    '''
    sum = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0): sum += i
    return sum

def wip(number):
    '''
    Returns the sum of all the multiples of 3 or 5 below the number passed in. 
    '''
    #return [num for num in range(number) if not num % 3 or not num % 5] # returns a list of only multiples of 3 and 5
    return sum([num for num in range(number) if not num % 3 or not num % 5]) # returns a list of only multiples of 3 and 5

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print("="*64,'\n', START_MESSAGE, "\nScript Location:", location, "\nArguments Passed: ", args, '\n',"="*64, sep='')
    logging.debug('Passed number: %s', args.number)
    print(solution(args.number))
    print(solution2(args.number))
    print(wip(args.number))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    #_, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Euler project, multiples of 3 and 5')
    parser.add_argument('number', type=int, help="Number below which to calculate sum of multiples of 3 and 5")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    args = parser.parse_args()
    # Set logging level
    if args.debug == True: logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else: logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.debug('Arguments: %s', args)
    main(args)


'''
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Simple bubble sort program')
    parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', type=int, required=True)
    # Use like: python arg.py -l 1234 2345 3456 4567
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    #parser.add_argument("-v", "--verbosity", type=int, choices=[1,2],
    #               help="increase debug logging verbosity")
    args = parser.parse_args()
    # Set logging level
    if args.debug == True: logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else: logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.debug('Arguments: %s', args)
    main(args)
'''