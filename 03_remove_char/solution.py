#! /usr/bin/env python3

"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""

# Imports 
import os
import sys

def remove_char(s):
    ''' Function removes first and last characters from string.'''
    return(s[1:len(s)-1]) # could also [1:-1]

def main():
    print("FINAL STRING:" , remove_char('123456789'))

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)    