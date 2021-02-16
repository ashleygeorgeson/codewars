#!/usr/bin/env python

# """Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number."""

# imports
import os
import sys

# Module Constants
START_MESSAGE = "Create Phone Number Script"

# Module "Global" Variables
location = os.path.abspath(__file__)
parser = argparse.ArgumentParser(description='Create Phone Number Script')
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', type=int,
    default=[1,2,3,4,5,6,7,8,9,0],required=False)

def create_phone_number(n):
    return("({}{}{}) {}{}{}-{}{}{}{}".format(*n))

# Module Functions and Classes
def main(*args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Running '{}'".format(__file__))
    print("Arguments Passed:", *args)
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    #phone_number = create_phone_number(*args, n=n)
    phone_number = create_phone_number(*args)
    print(phone_number)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    args = parser.parse_args()
    #_, *script_args = sys.argv
    main(args.list)