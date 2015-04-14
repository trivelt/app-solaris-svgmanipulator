#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest

from src.Icon import Icon
import src.svg as svg
from lxml import etree


class TestIcon(unittest.TestCase):
    def setUp(self):
        pass

    def testInitialization(self):
        icon = Icon("path/to/file.png")
        self.assertEqual(icon.name, "file")
        self.assertEqual(icon.path, "path/to/file.png")
        self.assertEqual(icon.coordinates, (0,0))

    def testNameUpdate(self):
        icon = Icon("/path/to/file123.jpg")
        self.assertEqual(icon.name, "file123")
        icon.path = "/other/path/imageFoo"
        self.assertNotEqual(icon.name, "imageFoo")
        icon.updateName()
        self.assertEqual(icon.name, "imageFoo")
        icon.path = "/another/iMg.gif"
        icon.updateName()
        self.assertEqual(icon.name, "iMg")
        self.assertEqual(icon.path, "/another/iMg.gif")

    def testCutExtension(self):
        icon = Icon("/icon/name.jpg")
        self.assertEqual(icon.name, "name")
        icon.name = "foo.Bar"
        icon.cutExtensionInName()
        self.assertEqual(icon.name, "foo")
        icon.name = "TE5T"
        self.assertEqual(icon.name, "TE5T")

    def testIconCorrect(self):
        icon = Icon("path/to/file.png")
        self.assertFalse(icon.isCorrect())
        icon.path = "blank.svg"
        self.assertTrue(icon.isCorrect())

    def testDrawIcon(self):
        absPath = path.abspath("symbol-solenoid.svg")
        icon = Icon(absPath)
        self.assertTrue(icon.isCorrect())

        blankSVGpath = 'blank.svg'
        svgTree = etree.parse(blankSVGpath)
        svgRoot = svgTree.getroot()
        svgFile = svg.SVG()
        svgFile.setSvg(svgRoot)

        icon.updateSvg()
        symbolsNode = foundSymbolsNode(svgRoot)
        self.assertNotEqual(symbolsNode, None)
        iconNode = foundElement("symbol-solenoid", symbolsNode)
        self.assertNotEqual(iconNode, None)
        self.assertEqual(iconNode.attrib["style"], "display:inline")
        self.assertEqual(iconNode.tag, "g")

        imageNode = iconNode[0]
        self.assertEqual(imageNode.tag, "image")
        self.assertEqual(imageNode.attrib["{http://www.w3.org/1999/xlink}href"], absPath)
        self.assertEqual(imageNode.attrib["x"], "0")
        self.assertEqual(imageNode.attrib["y"], "0")
        self.assertEqual(imageNode.attrib["width"], "30")
        self.assertEqual(imageNode.attrib["height"], "30")

    def tearDown(self):
        pass

def foundSymbolsNode(svgRoot):
    symbols = None
    for group in svgRoot[3]:
        if group.attrib["id"] == "symbols":
            symbols = group
            break
    return symbols

def foundElement(elementName, parentNode):
    searchElement = None
    for element in parentNode:
        if element.attrib["id"] == elementName:
            searchElement = element
    return searchElement

if __name__ == '__main__':
    unittest.main()