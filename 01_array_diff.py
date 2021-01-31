#! /usr/bin/env python3

# """Module docstring."""

# Imports 
import os
import sys

def array_dif(a,b):
    return(a,b)

def main():
    a = [1,2]
    b = [1]
    c = array_dif(a,b)
    print(c)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)