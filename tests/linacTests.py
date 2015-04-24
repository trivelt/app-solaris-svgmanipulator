#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Linac import Linac
from src.Device import Device
import src.svg as svg
from lxml import etree


class TestLinac(unittest.TestCase):
    def setUp(self):
        blankSVGpath = './blank.svg'
        svgTree = etree.parse(blankSVGpath)
        svgRoot = svgTree.getroot()
        self.svgFile = svg.SVG()
        self.svgFile.setSvg(svgRoot)
        self.linac = Linac()

    def testSectionColour(self):
        firstColour = self.linac.getNextSectionColour()
        self.assertEqual(firstColour, "#55ffdd")
        self.linac.addSection("AB01")
        nextSectionColour = self.linac.getNextSectionColour()
        self.assertEqual(nextSectionColour, "#b3b3b3")
        self.linac.addSection("TEST")
        nextSectionColour = self.linac.getNextSectionColour()
        self.assertEqual(nextSectionColour, "grey")

    def testNumberOfSections(self):
        self.assertEqual(self.linac.numberOfSections(), 0)
        self.linac.addSection("A")
        self.assertEqual(self.linac.numberOfSections(), 1)
        self.linac.addSection("B")
        self.linac.addSection("C")
        self.assertEqual(self.linac.numberOfSections(), 3)

    def testGetSection(self):
        self.assertEqual(self.linac.getSection("A"), None)
        self.linac.addSection("A")
        self.assertNotEqual(self.linac.getSection("A"), None)
        sectionA = self.linac.sections[0]
        self.assertEqual(self.linac.getSection("A"), sectionA)

        self.linac.addSection("TEST-01")
        sectionTest = self.linac.sections[1]
        self.assertEqual(self.linac.getSection("TEST-01"), sectionTest)

    def testAddSection(self):
        self.assertEqual(self.linac.numberOfSections(), 0)
        addedSection = self.linac.addSection("test002")
        self.linac.updateSvg()
        newSection = self.linac.getSection("test002")
        self.assertEqual(newSection.longName, "test002")
        self.assertEqual(addedSection, newSection)

        zoomNode = self.svgFile.getZoom2Background()
        bottomRect = self.svgFile.getElementById("section1bottomRect", zoomNode)
        self.assertEqual(bottomRect.attrib["x"], "1885")
        self.assertEqual(bottomRect.attrib["y"], "3685")
        self.assertEqual(self.linac.numberOfSections(), 1)

    def testAddLastLongSection(self):
        self.assertEqual(self.linac.numberOfSections(), 0)
        self.linac.addSection("test001")
        self.linac.addLastLongSection()
        self.assertEqual(self.linac.numberOfSections(), 2)
        firstSection = self.linac.getSection("test001")
        lastSection = self.linac.getSection("")
        self.assertNotEqual(lastSection, None)
        self.assertEqual(firstSection.width, 630)
        self.assertEqual(lastSection.width, 6148.519)

        self.linac.updateSvg()
        zoomNode = self.svgFile.getZoom2Background()
        bottomRect = self.svgFile.getElementById("section2bottomRect", zoomNode)
        self.assertEqual(bottomRect.attrib["x"], "2515")

    def testAddDevice(self):
        device = Device("ABC/MAG/device123", None, None)
        anotherDevice = Device("ABC/VAC/dev7", None, None)
        self.linac.addSection("ABC")
        section = self.linac.getSection("ABC")
        self.assertEqual(section.numberOfDevices(), 0)
        self.assertEqual(section.getDevice(0), None)
        self.linac.addDevice(device)
        self.assertEqual(section.getDevice(0), device)
        self.assertEqual(section.getDevice(1), None)
        self.linac.addDevice(anotherDevice)
        self.assertEqual(section.getDevice(1), anotherDevice)
        self.assertEqual(section.numberOfDevices(), 2)

    def testAddDeviceToSubsection(self):
        section = self.linac.addSection("I-S01", None, 200)
        subsection = section.addSubsection("I-S01B", None, 50)
        device = Device("I-S01B/ab/cd", None, [0, 20])
        self.linac.addDevice(device)
        self.assertEqual(device.section, subsection)


    def testComputeCoordinate(self):
        self.assertEqual(self.linac.numberOfSections(), 0)
        self.assertEqual(self.linac.computeNewSectionCoordinate(), 1885)
        self.linac.addSection("FOO")
        self.assertEqual(self.linac.computeNewSectionCoordinate(), 2515)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()