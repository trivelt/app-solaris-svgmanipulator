#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Section import Section
from src.Device import Device

class TestSection(unittest.TestCase):
    def setUp(self):
        pass

    def testSectionCreate(self):
        section = Section("I-K02", "red")
        self.assertEqual(section.longName, "I-K02")
        self.assertEqual(section.displayedName, "I-K02")
        self.assertEqual(section.colour, "red")
        self.assertEqual(len(section.devices), 0)

    def testAddDevice(self):
        device = Device("abcde", None, None)
        section = Section("test", "grey")
        self.assertEqual(section.numberOfDevices(), 0)
        section.addDevice(device)
        self.assertEqual(section.numberOfDevices(), 1)
        self.assertEqual(section.devices[0], device)
        self.assertEqual(device.numberInSection, 0)
        otherDevice = Device("other", None, None)
        section.addDevice(otherDevice)
        self.assertEqual(otherDevice.numberInSection, 1)

    def testGetDevice(self):
        dev1 = Device("foo", None, None)
        dev2 = Device("bar", None, None)
        section = Section("test", "grey")
        self.assertEqual(section.numberOfDevices(), 0)
        section.addDevice(dev1)
        section.addDevice(dev2)
        self.assertEqual(section.numberOfDevices(), 2)
        self.assertEqual(section.getDevice(0), dev1)
        self.assertNotEqual(section.getDevice(0), dev2)
        self.assertEqual(section.getDevice(1), dev2)
        self.assertEqual(section.getDevice(3), None)

    def testSortDevices(self):
        firstDevice = Device("First", None, [184, 99])
        secondDevice = Device("Second", None, [964, 80])
        section = Section("test", None)
        section.addDevice(secondDevice)
        section.addDevice(firstDevice)

        self.assertEqual(section.getDevice(0), secondDevice)
        section.sortDevices()
        self.assertEqual(section.getDevice(0), firstDevice)

    def testRepr(self):
        section = Section("AB-CD01", None)
        self.assertEqual(section.__repr__(), "AB-CD01")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()