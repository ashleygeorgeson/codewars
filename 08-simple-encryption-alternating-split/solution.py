#!/usr/bin/env python

# Docstring
""" For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!.
"""

# imports
import os
import sys
import argparse
#from typing import final

# Module Constants
START_MESSAGE = "Simple Encryption #1 - Alternating Split"

# Module "Global" Variables
location = os.path.abspath(__file__)

def decrypt(encrypted_text, n):
    """decrypt function

    """
    print("Decrypt:", args.decrypt, args.text, args.n)

def encrypt(text, n):
    """encrypt function
    For building the encrypted string:
    Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
    Do this n times!
    """
    #print("Encrypt:", args.encrypt, args.text, args.n)
    for i in range(n):
        text = text[1:len(text):2] + text[0:len(text):2]
    return(text)

# Module Functions and Classes
def main(args):
    """My main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)
    #print(solution(*args))
    if args.decrypt:
        decrypt(args.text, args.n)
    else:
        encrypt(args.text, args.n)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Simple encryption, alternating split program')
    parser.add_argument('text', type=str, help="String to de/encrypt")
    parser.add_argument('n', type=int, help="Number of times to alternate split in crypto algorithm")
    group = parser.add_mutually_exclusive_group(required=True) # Mututally exclusive group
    group.add_argument("-d", "--decrypt", action="store_true",
                        help="Encrypt text")
    group.add_argument("-e", "--encrypt", action="store_true",
                        help="Decrypt text")
    args = parser.parse_args()
    #print(args.text, args.n, args.decrypt, args.encrypt)
    #main(args.text, args.n)
    #print(type(args))
    #print(type(*args))
    main(args)