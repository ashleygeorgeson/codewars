#!/usr/bin/env python

# """Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number."""

# imports
import os
import sys

# Module Constants
START_MESSAGE = "Create Phone Number Script"

# Module "Global" Variables
location = os.path.abspath(__file__)

def create_phone_number(n):
    num = ''
    for i in n: num += str(i)
    return('(' + num[0:3] + ') ' + num[3:6] + '-' + num[6:11])

# Module Functions and Classes
def main(*args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", *args)
    #print(type(*args))
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    phone_number = create_phone_number(*args, n=n)
    print(phone_number)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    #print(sys.argv)
    #print(sys.argv[1])
    main(*script_args)