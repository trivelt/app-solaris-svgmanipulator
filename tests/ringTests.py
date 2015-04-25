#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Ring import Ring
from src.Device import Device
import src.svg as svg
from lxml import etree


class TestRing(unittest.TestCase):
    def setUp(self):
        self.ring = Ring()

    def testRingInit(self):
        newRing = Ring()
        self.assertEqual(len(newRing.sections), 0)
        self.assertEqual(newRing.radius, 2645.4143)

    def testAddSection(self):
        firstSection = self.ring.addSection("R1-01", None, 90)
        self.assertEqual(firstSection.longName, "R1-01")
        self.assertEqual(firstSection.startAngle, -90)
        self.assertEqual(firstSection.angle, 90)

        secondSection = self.ring.addSection("R1-02", None, 30)
        self.assertEqual(secondSection.startAngle, 0)
        self.assertEqual(secondSection.angle, 30)

    def testGetSection(self):
        section = self.ring.addSection("R1-03", None, 10)
        self.assertEqual(self.ring.getSection("R1-01"), None)
        self.assertEqual(self.ring.getSection("R1-03"), section)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()