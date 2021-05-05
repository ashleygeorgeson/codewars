#!/usr/bin/env python

# imports
import os
import sys
from solution import sequence_sum

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sequence_sum(2, 6, 2), 12)
        test.assert_equals(sequence_sum(1, 5, 1), 15)
        test.assert_equals(sequence_sum(1, 5, 3), 5)
        test.assert_equals(sequence_sum(0, 15, 3), 45)
        test.assert_equals(sequence_sum(16, 15, 3), 0)
        test.assert_equals(sequence_sum(2, 24, 22), 26)
        test.assert_equals(sequence_sum(2, 2, 2), 2)
        test.assert_equals(sequence_sum(2, 2, 1), 2)
        test.assert_equals(sequence_sum(1, 15, 3), 35)
        test.assert_equals(sequence_sum(15, 1, 3), 0)
