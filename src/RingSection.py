from math import pi, cos, sin
from Section import Section
from lxml import etree
import svg


class RingSection(Section):
    id = 1

    def __init__(self, name, colour, startAngle, angle):
        Section.__init__(self, name, colour)
        self.angle = angle
        self.startAngle = startAngle
        self.endAngle = (startAngle+angle)
        self.subsections = list()
        self.centerX = 11989.075
        self.centerY = 4827.0225
        self.radius = 2705.4143
        self.shortName = "ringSection" + str(self.id)

        self.id = RingSection.id
        RingSection.id += 1

    def updateSvg(self):
        self.drawSectionOnZoom1()
        self.drawSectionOnZoom2()
        self.drawBigText()

    def drawSectionOnZoom1(self):
        zoomNode = self.svgFile.getZoom1Background()
        self.drawColorfulCircle(zoomNode)

    def drawColorfulCircle(self, parentNode):
        path = self.describeArc(self.centerX, self.centerY, self.radius+100, self.startAngle, self.endAngle)
        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = self.shortName + "colorfulCircle"
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = self.colour
        sectionElement.attrib["stroke"] = "white"
        sectionElement.attrib["stroke-width"] = "0"
        #sectionElement.attrib["style"] = "opacity:0.5;"

        descElement = etree.SubElement(sectionElement, "desc")
        descElement.attrib["id"] = self.shortName + "desc"
        descElement.text = "section=" + self.longName

    def drawSectionOnZoom2(self):
        zoomNode = self.svgFile.getZoom2Background()
        path = self.describeArc(self.centerX, self.centerY, self.radius-150, self.startAngle, self.endAngle)
        sectionElement = etree.SubElement(zoomNode, "path")
        sectionElement.attrib["id"] = self.shortName + "colorfulBorder"
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["stroke"] =  self.colour
        sectionElement.attrib["stroke-width"] = "20"

    def drawBigText(self):
        start = self.polarToCartesian(self.centerX, self.centerY, self.radius, self.startAngle)
        end = self.polarToCartesian(self.centerX, self.centerY, self.radius, self.endAngle)

        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName+"pathdef"
        print self.longName + ": Start.x=" + str(start[0]) + ",start.y=" + str(start[1]) + ", end.x=" + str(end[0]) + ", end.y=" + str(end[1])
        pathDef.attrib["d"] = "M " + str(start[0]) + " " + str(start[1]) + " S " + str(end[0]-200) + \
            " " + str(end[1] - 500) + " " + str(end[0]) + " " + str(end[1])

        zoomElement = self.svgFile.getZoom1Background()
        textEleement = etree.SubElement(zoomElement, "text")
        textEleement.attrib["x"] = "0"
        textEleement.attrib["y"] = "0"
        textEleement.attrib["font-size"] = "200"
        textEleement.attrib["style"] = "stroke:#000000;"
        textEleement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textEleement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName+"pathdef"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.text = self.longName


    def polarToCartesian(self, centerX, centerY, radius, angleInDegrees):
        angleInRadians = (angleInDegrees-90.0) * pi / 180.0
        #print "Angle in radians=" + str(angleInRadians)
        x = centerX + (radius * cos(angleInRadians))
        y = centerY + (radius * sin(angleInRadians))
        return [x, y]


    def describeArc(self, x, y, radius, startAngle, endAngle):
        start = self.polarToCartesian(x, y, radius, endAngle)
        #print("startX=" + str(start[0]) + ", startY=" + str(start[1]))
        end = self.polarToCartesian(x, y, radius, startAngle)
        #print("endX=" + str(end[0]) + ", endY=" + str(end[1]))

        arcSweep = "0" if endAngle - startAngle <= 180 else "1"

        d = "M " + str(start[0]) + " " + str(start[1]) + \
             " A " + str(radius) + " " + str(radius) + " 0 " + arcSweep + " 0 "  +str(end[0]) + " " + str(end[1]) + \
            " L " + str(x) + " " + str(y) + \
            " L " + str(start[0]) + " " + str(start[1]) + " Z"

        return d