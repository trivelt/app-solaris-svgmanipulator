#!/usr/bin/python

import src.svg as svg
from src.Linac import Linac
from lxml import etree
from src.TangoDeviceManager import TangoDeviceManager

blankSVGpath = './src/blank.svg'

svgTree = etree.parse(blankSVGpath)
svgRoot = svgTree.getroot()

svgFile = svg.SVG()
svgFile.setSvg(svgRoot)

print "SVG file loaded "

L = Linac()
L.addSection("AB-01")
L.addSection("BB02")
L.addSection("CC03")
L.addLastLongSection()
L.updateSvg()


svgRoot = svgFile.getSvg()
toWrite = etree.tostring(svgRoot, pretty_print=True)
fd = open("new.svg", 'w')
fd.write(toWrite)