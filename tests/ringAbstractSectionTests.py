#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.RingAbstractSection import RingAbstractSection
from src.Device import Device

class TestRingAbstractSection(unittest.TestCase):
    def setUp(self):
        pass

    def testNewSection(self):
        section = RingAbstractSection("R1-01", "green", 15, 35)
        self.assertEqual(section.longName, "R1-01")
        self.assertEqual(section.startAngle, 15)
        self.assertEqual(section.endAngle, 50)

    def testIsInUpperHalf(self):
        upperSection = RingAbstractSection("InUpper", None, -30, 180)
        lowerSection = RingAbstractSection("InLower", None, 100, 120)
        self.assertEqual(upperSection.isInUpperHalf(), True)
        self.assertEqual(lowerSection.isInUpperHalf(), False)

    def testGetAngleBetweenDevices(self):
        ringASection = RingAbstractSection("RAS", None, 20, 90)
        self.assertEqual(ringASection.getAngleBetweenDevices(), 90)

        ringASection.addDevice(Device("a", None, None))
        self.assertEqual(ringASection.getAngleBetweenDevices(), 45)
        ringASection.addDevice(Device("b", None, None))
        self.assertEqual(ringASection.getAngleBetweenDevices(), 30)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()