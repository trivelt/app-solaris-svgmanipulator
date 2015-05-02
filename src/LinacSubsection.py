from lxml import etree
from LinacAbstractSection import LinacAbstractSection

class LinacSubsection(LinacAbstractSection):
    id = 1

    def __init__(self, name, colour, startCoordinate, width):
        LinacAbstractSection.__init__(self, name, colour, startCoordinate, width)
        self.id = LinacSubsection.id
        LinacSubsection.id += 1
        self.shortName = "linacSubsection" + str(self.id)

    def updateSvg(self):
        zoomNode = self.svgFile.getZoom2Background()
        self.createRectangle(zoomNode)
        self.createTextElement(zoomNode)

    def createRectangle(self, parentNode):
        rectElement = etree.SubElement(parentNode, "rect")
        rectElement.attrib["id"] = self.shortName + "Rect"
        rectElement.attrib["x"] = str(self.startCoordinate)
        rectElement.attrib["y"] = "3665"
        rectElement.attrib["width"] = str(self.width)
        rectElement.attrib["height"] = "19.999943"
        rectElement.attrib["style"] = "fill:" + self.colour + ";fill-opacity:0.49803922;stroke:none;display:inline"

    def createTextElement(self, parentNode):
        style = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;" \
                "font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        defs = self.svgFile.getElementById("defs8812", self.svgRoot)
        pathDef = etree.SubElement(defs, "path")
        pathDef.attrib["id"] = self.shortName + "SmallCaptionPath"
        pathDef.attrib["d"] = "M " + str(self.startCoordinate) + " 3682 l " + str(self.width) + " 0"

        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + "SmallCaption"
        textElement.attrib["style"] = style
        textElement.attrib["text-anchor"] = "middle"

        textPathElement = etree.SubElement(textElement, "textPath")
        textPathElement.attrib["{http://www.w3.org/1999/xlink}href"] = "#" + self.shortName + "SmallCaptionPath"
        textPathElement.attrib["startOffset"] = "50%"
        textPathElement.attrib["id"] = self.shortName + "SmallCaptionTextPath"
        textPathElement.text = self.displayedName