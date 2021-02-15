#!/usr/bin/env python

# imports
import os
import sys
from solution import sum_even_numbers

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

@test.describe("Simple integers input.")
def example_tests():
    test.assert_equals(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    test.assert_equals(sum_even_numbers([]), 0)