from RingAbstractSection import RingAbstractSection
from ArcDrawingTools import ArcDrawingTools
from lxml import etree

class RingSubsection(RingAbstractSection):
    id = 1

    def __init__(self, name, colour, startAngle, angle):
        RingAbstractSection.__init__(self, name, colour, startAngle, angle)
        self.id = RingSubsection.id
        RingSubsection.id += 1
        self.shortName = "ringSubsection" + str(self.id)

    def updateSvg(self):
        zoomNode = self.svgFile.getZoom2Background()
        if self.isInUpperHalf():
            clockwiseFunction = ArcDrawingTools.describeArcAnticlockwise
            radiusOffset = -138
        else:
            clockwiseFunction = ArcDrawingTools.describeArcClockwise
            radiusOffset = -123

        self.drawColourfulSection(zoomNode)
        self.drawText(clockwiseFunction, radiusOffset, zoomNode)


    def drawColourfulSection(self, parentNode):
        path = ArcDrawingTools.describeArcClockwise(self.centerX, self.centerY, self.radius-130, self.startAngle, self.endAngle)

        sectionElement = etree.SubElement(parentNode, "path")
        sectionElement.attrib["id"] = self.shortName + "colourfulSection"
        sectionElement.attrib["d"] = path
        sectionElement.attrib["fill"] = "white"
        sectionElement.attrib["fill-opacity"] = "0.0"
        sectionElement.attrib["stroke"] =  self.colour
        sectionElement.attrib["stroke-width"] = "20"


    def drawText(self, clockwiseFunction, radiusOffset, parentNode):
        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName + "Path"
        pathDef.attrib["d"] = clockwiseFunction(self.centerX, self.centerY, self.radius+radiusOffset, self.startAngle, self.endAngle)

        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + "text"
        textElement.attrib["x"] = "0"
        textElement.attrib["y"] = "0"
        textElement.attrib["style"] = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:" \
                "start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:" \
                "#000000;fill-opacity:1;stroke:none;display:inline;font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        textElement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textElement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName + "Path"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.text = self.longName



