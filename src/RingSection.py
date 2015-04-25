from math import pi, cos, sin
from Section import Section
from ArcDrawingTools import ArcDrawingTools
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
        if self.isInUpperHalf():
            clockwiseFunction = ArcDrawingTools.describePathForTextAnticlockwise
        else:
            clockwiseFunction = ArcDrawingTools.describePathForTextClockwise
        self.drawSectionOnZoom1(clockwiseFunction)
        self.drawSectionOnZoom2(clockwiseFunction)

    def isInUpperHalf(self):
        numbersOfAngle = [x for x in range(self.startAngle, self.endAngle)]
        numbersOfUpperHalf = [x for x in range(-90, 90)]
        listsIntersection = set(numbersOfAngle).intersection(numbersOfUpperHalf)
        percentInUpperHalf = len(listsIntersection) / float(len(numbersOfAngle))
        if percentInUpperHalf > 0.5:
            return True
        else:
            return False

    def drawSectionOnZoom1(self, clockwiseFunction):
        self.drawBigColorfulCircle()
        self.drawBigText(clockwiseFunction)

    def drawBigColorfulCircle(self):
        zoomNode = self.svgFile.getZoom1Background()
        sectionElement = self.drawColourfulSection(zoomNode, 100, 0, "colourfulCircle")

        descElement = etree.SubElement(sectionElement, "desc")
        descElement.attrib["id"] = self.shortName + "desc"
        descElement.text = "section=" + self.longName

    def drawSectionOnZoom2(self, clockwiseFunction):
        zoomNode = self.svgFile.getZoom2Background()
        self.drawColourfulSection(zoomNode, -150, 20, "colorfulBorder")
        self.drawSmallText(clockwiseFunction)

    def drawColourfulSection(self, parentNode, radiusOffset, strokeWidth, idName):
        path = ArcDrawingTools.describeArcClockwise(self.centerX, self.centerY, self.radius+radiusOffset, self.startAngle, self.endAngle)

        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = self.shortName + idName
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = self.colour
        sectionElement.attrib["stroke"] =  self.colour
        sectionElement.attrib["stroke-width"] = str(strokeWidth)
        return sectionElement

    def drawBigText(self, clockwiseFunction):
        style = "font-size:200px;font-style:normal;"
        zoomElement = self.svgFile.getZoom1Background()
        if clockwiseFunction == ArcDrawingTools.describePathForTextAnticlockwise:
            radiusOffset = -100
        else:
            radiusOffset = 35
        self.drawText(zoomElement, radiusOffset, clockwiseFunction, style, "bigCaption")

    def drawSmallText(self, clockwiseFunction):
        style = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:" \
                "start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:" \
                "#000000;fill-opacity:1;stroke:none;display:inline;font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        zoomElement = self.svgFile.getZoom2Background()
        if clockwiseFunction == ArcDrawingTools.describePathForTextAnticlockwise:
            radiusOffset = -157
        else:
            radiusOffset = -143

        self.drawText(zoomElement, radiusOffset, clockwiseFunction, style, "smallCaption")

    def drawText(self, parentNode, radiusOffset, clockwiseFunction, style, idName):
        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName + idName + "Path"
        pathDef.attrib["d"] = clockwiseFunction(self.centerX, self.centerY, self.radius+radiusOffset, self.startAngle, self.endAngle)

        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + idName
        textElement.attrib["x"] = "0"
        textElement.attrib["y"] = "0"
        textElement.attrib["style"] = style
        textElement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textElement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName + idName + "Path"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.text = self.longName