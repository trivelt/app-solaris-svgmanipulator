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
        textElement = etree.SubElement(parentNode, "text")
        textElement.attrib["id"] = self.shortName + "smallText"
        textElement.attrib["x"] = str(self.startCoordinate)
        textElement.attrib["y"] = "3682.2803"
        textElement.attrib["style"] = "font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;display:inline;font-family:Sans;-inkscape-font-specification:'Sans, Normal'"
        textElement.text = self.displayedName

