#!/usr/bin/env python

# Docstring
"""
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.

You don't need to validate the form of the Roman numeral.
"""

# imports
import logging, os, sys
import argparse

# Module Constants
START_MESSAGE = "Roman Numeral Decoder"

# Module "Global" Variables
location = os.path.abspath(__file__)

def solution(roman):
    # Convert Roman Numeral string to uppercase
    roman = roman.upper()
    # Count and strip each potential unique 'odd/ one less than' number
    cm,cd,xc,xl,ix,iv = roman.count('CM'), roman.count('CD'), roman.count('XC'), roman.count('XL'), roman.count('IX'), roman.count('IV')
    logging.debug('Count of odd numerals: CM:%s CD:%s XC:%s XL:%s IX:%s IV:%s', cm,cd,xc,xl,ix,iv)
    for i in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']:
        roman = roman.replace(i,'')
    # Count each Roman Numeral base and assign to a unique variable
    logging.debug('Remaining Roman numerals after stripping odd numerals: %s', roman)
    m,d,c,l,x,v,i = roman.count('M'), roman.count('D'), roman.count('C'), roman.count('L'), roman.count('X'), roman.count('V'), roman.count('I')
    logging.debug('Count of normal numerals: M:%s D:%s C:%s L:%s X:%s V:%s I:%s', m,d,c,l,x,v,i)
    # Calculate decimal value
    decimal = (int(cm)*900) + (int(cd)*400) + (int(xc)*90) + (int(xl)*40) + (int(ix)*9) + (int(iv)*4) + (int(m)*1000) + (int(d)*500) + (int(c)*100) + (int(l)*50) + (int(x)*10) + (int(v)*5) + (int(i)*1)
    logging.debug('Converted decimal: %s', decimal)
    return(decimal)

# Module Functions and Classes
def main(args):
    """Main script function.

    Displays the full path to this script, and a list of the arguments passed to the script.
    """
    print("="*64,'\n', START_MESSAGE, "\nScript Location:", location, "\nArguments Passed: ", args, '\n',"="*64, sep='')
    logging.debug('Passed sequence in main: %s', args.roman)
    solution(args.roman)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    #_, *script_args = sys.argv
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Decodes a Roman Numeral to Decimal integer')
    parser.add_argument('roman', type=str, help="Roman Numeral")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug logging")
    args = parser.parse_args()
    # Set logging level
    if args.debug == True: logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    else: logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.debug('Arguments: %s', args)
    main(args)