#!/usr/bin/env python

# '''Docstring'''
'''
Module docstring:
Write a function, persistence, that takes in a positive parameter num and returns its 
multiplicative persistence, which is the number of times you must multiply the digits 
in num until you reach a single digit.
'''

# Imports
import os
import sys
import argparse

# Module Constants
START_MESSAGE = "Persistence"

# Module "Global" Variables
location = os.path.abspath(__file__)
#parser = argparse.ArgumentParser(description='Return multiplicative persistence')
#parser.add_argument('-n', '--num', help='Provide a positive integer to calculate. Defaults to 2', 
#    type=int, default=2, required=False)

# argparser init
def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def persistence(n):
    '''
    Method docstring:
    Takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach 
    a single digit.

    LOGIC:
        while more than 1 digit
            split the digits
            multiply the digits
            increment iteration counter
        return counter

    '''
    print('Parameter in {} = {}'.format(__name__,n))
    
    #
    # Using math.prod:
    #
    #from math import prod
    #i = 0
    #while len(str(n)) > 1:
    #    i+=1
    #    n = prod([int(item) for item in list(str(n))])
    #    print('Iteration {}, n value: {}'.format(i,n))
    #return i

    #
    # Not using math.prod:
    #
    i = 0
    while len(str(n)) > 1:
        i+=1
        k = 1 # k = running product
        # j,k = 1,1 # i = iteration, k = running value ==> DEBUG
        for item in list(str(n)):
            k *= int(item)
            #print('Product Iteration: {} Sum: {}'.format(j,k)) ==> DEBUG
            #j += 1 ==> DEBUG
        n = k # set running product back to n for while loop num digits test
        #print('Iteration {}, n value: {}'.format(i,n)) ==> DEBUG
    return i
    
def main(*args):
    '''
    Method docstring:
    Main script function
    Displays the full path to this script, and a list of the arguments passed to the script.
    '''
    per = persistence(*args)
    print('Persistence: {}'.format(per))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return multiplicative persistence')
    parser.add_argument('-n', '--num', help='Provide a positive integer to calculate. Defaults to 2', 
        type=check_positive, default=2, required=False)
    args = parser.parse_args()
    main(args.num)