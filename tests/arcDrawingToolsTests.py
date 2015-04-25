#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.ArcDrawingTools import ArcDrawingTools

class TestArcTools(unittest.TestCase):
    def setUp(self):
        pass

    def testPolarToCartesian(self):
        self.assertEqual(ArcDrawingTools.polarToCartesian(2005, 1500, 600, 95), [2602.716818855047, 1552.2934456485948])
        self.assertEqual(ArcDrawingTools.polarToCartesian(20, 30, 10, 180), [20.0, 40.0])

    def testDescribePathForTextClockwise(self):
        expectedPath = "M 3995.88860426 4842.99213127 A 3000 3000 0 0 0 1776.45713531 2102.22252113"
        self.assertEqual(ArcDrawingTools.describePathForTextClockwise(1000, 5000, 3000, 15, 87), expectedPath)

        expectedPath = "M 450.0 200.0 A 150 150 0 0 0 193.933982822 93.933982822"
        self.assertEqual(ArcDrawingTools.describePathForTextClockwise(300, 200, 150, -45, 90), expectedPath)

    def testDescribePathForTextAntiClockwise(self):
        expectedPath = "M 1776.45713531 2102.22252113 A 3000 3000 0 0 1 3995.88860426 4842.99213127"
        self.assertEqual(ArcDrawingTools.describePathForTextAnticlockwise(1000, 5000, 3000, 15, 87), expectedPath)

        expectedPath = "M 193.933982822 93.933982822 A 150 150 0 0 1 450.0 200.0"
        self.assertEqual(ArcDrawingTools.describePathForTextAnticlockwise(300, 200, 150, -45, 90), expectedPath)

    def testDescribeArcClockwise(self):
        expectedPath = "M 16000.0 5000.0 A 3000 3000 0 0 0 13000.0 2000.0L 13000 5000 L 16000.0 5000.0 Z"
        self.assertEqual(ArcDrawingTools.describeArcClockwise(13000, 5000, 3000, 0, 90), expectedPath)

    def testDescribeArcAntiClockwise(self):
        expectedPath = "M 13000.0 2000.0 A 3000 3000 0 0 1 16000.0 5000.0L 13000 5000 L 13000.0 2000.0 Z"
        self.assertEqual(ArcDrawingTools.describeArcAnticlockwise(13000, 5000, 3000, 0, 90), expectedPath)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()