#!/usr/bin/env python

# imports
import os
import sys
from solution import create_phone_number

# Module "Global" Variables
location = os.path.abspath(__file__)
here = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path for the directory where this file is located "here"
project_root = os.path.abspath(os.path.join(here, "..")) # Get the absolute path for the project / repository root
sys.path.insert(0, project_root)# Extend the system path to include the project root and import the test module

# relative imports
import codewars_test as test

@test.describe("Basic tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
