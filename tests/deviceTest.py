#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Device import Device
from src.Icon import Icon
import src.svg as svg
from lxml import etree


class TestDevice(unittest.TestCase):
    def setUp(self):
        pass

    def testConfiguration(self):
        coord = (12,13.901)
        icon = Icon("test/path")
        device = Device("name", icon, coord)
        self.assertEqual(device.icon, icon)
        self.assertEqual(device.realCoordinates, coord)
        self.assertEqual(device.name, "name")

    def testSectionName(self):
        device = Device("I-TL/VAC/I-TL-CAB02-VAC-IPCU1", None, None)
        self.assertEqual(device.getSectionName(), "I-TL")

        device = Device("I-S00/MAG/I-S00-MAG-COBX2", None, None)
        self.assertEqual(device.getSectionName(), "I-S00")

        device = Device("I-K01/VAC/I-K01CAB05-VAC-IPCU1", None, None)
        self.assertEqual(device.getSectionName(), "I-K01")

        device = Device("R1-SGA/MAG/CAB1R1-SGA4-MAG-PS04", None, None)
        self.assertEqual(device.getSectionName(), "R1-SGA")

    def testSubsystemName(self):
        device = Device("I-TL/VAC/I-TL-CAB02-VAC-IPCU1", None, None)
        self.assertEqual(device.subsystem, "VAC")

        device = Device("I-S00/MAG/I-S00-MAG-COBX2", None, None)
        self.assertEqual(device.subsystem, "MAG")

        device = Device("I-K01/RF/I-K01CAB03-RF-LLRFL1", None, None)
        self.assertEqual(device.subsystem, "RF")

        device = Device("I-S00/DIA/I-S00-DIA-SCRN1", None, None)
        self.assertEqual(device.subsystem, "DIA")

    def testRingElement(self):
        device = Device("I-K01/VAC/I-K01CAB05-VAC-IPCU1", None, None)
        self.assertEqual(device.isRingElement(), False)

        device = Device("R1-SGA/MAG/R1-SGACAB14-MAG-PS04", None, None)
        self.assertEqual(device.isRingElement(), True)

    def testLinacElement(self):
        device = Device("I-K01/VAC/I-K01CAB05-VAC-IPCU1", None, None)
        self.assertEqual(device.isLinacElement(), True)

        device = Device("R1-SGA/MAG/R1-SGACAB14-MAG-PS04", None, None)
        self.assertEqual(device.isLinacElement(), False)


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()