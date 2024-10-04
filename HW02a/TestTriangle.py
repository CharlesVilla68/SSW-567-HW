# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(5,5,3), 'Isosceles', '5,5,3 should be Isosceles')
        self.assertEqual(classifyTriangle(5,3,5), 'Isosceles', '5,3,5 should be Isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,6,7), 'Scalene', '5,6,7 should be Scalene')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput', '-1,2,3 should be Invalid')
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 should be Invalid')
        self.assertEqual(classifyTriangle(234,452,343), 'InvalidInput', '234,452,343 should be Invalid')
        
    def testNonIntegerInputs(self):
        self.assertEqual(classifyTriangle(3.5,4,5), 'InvalidInput', '3.5,4,5 should be Invalid')
        
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,10,12),'NotATriangle', '1,10,12 should be NotATriangle')
        self.assertEqual(classifyTriangle(5,1,1), 'NotATriangle', '5,1,1 should be NotATriangle')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

