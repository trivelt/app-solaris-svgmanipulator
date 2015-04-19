#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Device import Device
from src.Icon import Icon
from src.Linac import Linac
from src.LinacSection import LinacSection
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
        self.assertEqual(device.subsystemName, "VAC")

        device = Device("I-S00/MAG/I-S00-MAG-COBX2", None, None)
        self.assertEqual(device.subsystemName, "MAG")

        device = Device("I-K01/RF/I-K01CAB03-RF-LLRFL1", None, None)
        self.assertEqual(device.subsystemName, "RF")

        device = Device("I-S00/DIA/I-S00-DIA-SCRN1", None, None)
        self.assertEqual(device.subsystemName, "DIA")

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

    def testCheckingConditions(self):
        deviceWithoutIcon = Device("A/B/C", None, None)
        deviceWithoutIcon.section = True
        with self.assertRaises(Exception):
            deviceWithoutIcon.checkNecessaryConditions()

        deviceWithoutSection = Device("D/E/F", Icon("test"), None)
        with self.assertRaises(Exception):
            deviceWithoutSection.checkNecessaryConditions()

        deviceWithWrongSubsystem = Device("GHI", Icon("test"), None)
        deviceWithWrongSubsystem.section = True
        with self.assertRaises(Exception):
            deviceWithWrongSubsystem.checkNecessaryConditions()

    def testAssigningSvgCoordinate(self):
        device = Device("abc/testDevice", None, None)
        self.assertEqual(device.svgCoordinate, None)

        linac = Linac()
        linac.addSection("abc")
        linac.addDevice(device)
        device.assignSvgCoordinate()
        testSection = linac.getSection("abc")
        sectionStartCoordinate = testSection.startCoordinate
        distanceBetweenDevices = testSection.getDistanceBetweenDevices()

        self.assertEqual(device.svgCoordinate, sectionStartCoordinate+distanceBetweenDevices)

    def testGenerateSimpleName(self):
        device = Device("I-K01/VAC/I-K01CAB05-VAC-IPCU1", None, None)
        self.assertEqual(device.generateSimpleName(), "ik01vacik01cab05vacipcu1")

    def testDrawDevice(self):
        icon = Icon("symbol-quadrupole.svg")
        device = Device("I-K01/VAC/I-K01CAB05-VAC-IPCU1", icon, (113,122))
        linac = Linac()
        linac.addSection("I-K01")
        linac.addDevice(device)

        blankSVGpath = 'blank.svg'
        svgTree = etree.parse(blankSVGpath)
        svgRoot = svgTree.getroot()
        svgFile = svg.SVG()
        svgFile.setSvg(svgRoot)

        device.updateSvg()
        vacNode = svgFile.getSubsystemZoomNode("VAC")
        deviceNode = svgFile.getElementById("ik01vacik01cab05vacipcu1", vacNode)
        self.assertEqual(deviceNode.attrib["{http://www.w3.org/1999/xlink}href"], "#symbol-quadrupole")
        descriptionNode = svgFile.getElementById("ik01vacik01cab05vacipcu1Desc", deviceNode)
        self.assertEqual(descriptionNode.text, "device=I-K01/VAC/I-K01CAB05-VAC-IPCU1")

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()