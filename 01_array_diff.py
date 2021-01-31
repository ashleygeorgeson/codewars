#! /usr/bin/env python3

# """Program should remove all values from list a, which are present in list b."""

# Imports 
import os
import sys

def array_dif(a,b):
    c = [] # New array to store the differences between arrays [a] and [b]
    for i in a:
        for j in b:
            if i is j: # Tested value from [a] is present in [b] - do not append to the new array
                print("VALUE PRESENT! " , i , "=" , j)
            else:
                print("NO MATCH! " , i , "!=" , j) # Tested value from [a] is not present in [b] - append to the new array
                c.append(i) 
    return(c)

def main():
    # Test Case 1 Values
    #a = [1,2]
    #b = [1] 
    # Test Case 2 Values
    a = [1,2,2,2,3]
    b = [2]
    c = array_dif(a,b)
    print("FINAL ARRAY DIFFERENCE:" , c)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)