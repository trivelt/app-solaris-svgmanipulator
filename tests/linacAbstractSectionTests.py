#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.LinacAbstractSection import LinacAbstractSection
from src.Device import Device

class TestLinacAbstractSection(unittest.TestCase):
    def setUp(self):
        pass

    def testGetDistanceBetweenDevices(self):
        section = LinacAbstractSection("test", None, None, 600)
        self.assertEqual(section.numberOfDevices(), 0)
        self.assertEqual(section.getDistanceBetweenDevices(), 600)
        dev1 = Device("dev1", None, None)
        section.addDevice(dev1)
        self.assertEqual(section.getDistanceBetweenDevices(), 300)
        dev2 = Device("dev2", None, None)
        section.addDevice(dev2)
        self.assertEqual(section.getDistanceBetweenDevices(), 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()