#!/usr/bin/env python

# """Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of the even values of this sequence.
# Only numbers without decimals like 4 or 4.0 can be even.
# The input is a sequence of numbers: integers and/or floats. """

# imports
import os
import sys
import argparse

# Module Constants
START_MESSAGE = "Sum even numbers"

# Module "Global" Variables
location = os.path.abspath(__file__)
parser = argparse.ArgumentParser(description='Sum even numbers script')
parser.add_argument('-l', '--list', help='Provide a list of integers to sum. Defaults to [1,2,3,4,5,6,7,8,9,10]', nargs='+', 
    type=int, default=[1,2,3,4,5,6,7,8,9,10],required=False)

def sum_even_numbers(seq): # Init a running total, iterate through the list, check whether element is even, increment total if even
    sum = 0
    for i in seq:
        if i % 2 == 0: sum += i
    return sum

# Module Functions and Classes
def main(*args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Running: {}".format(__file__))
    print("Arguments Passed:", *args)
    sum = sum_even_numbers(*args)
    print(sum)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.list)