import svg
import os.path
from lxml import etree

class Icon:
    def __init__(self, path, coordinates=(0,0)):
        self.path = path
        self.coordinates = coordinates
        self.updateName()

    def __repr__(self):
        return "Icon(" + self.path + ")"

    def __eq__(self, other):
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)

    def updateName(self):
        pathElements = self.path.split("/")
        if len(pathElements):
            self.name = str(pathElements[-1])
        else:
            self.name = str(self.path)
        self.cutExtensionInName()

    def cutExtensionInName(self):
        try:
            dotIndex = self.name.rindex(".")
            self.name = self.name[:dotIndex]
        except ValueError:
            pass

    def updateSvg(self):
        if self.isCorrect() == False:
            print("Warning: icon's path is invalid!")

        svgFile = svg.SVG()
        self.svgRoot = svgFile.getSvg()
        symbolsNode = svgFile.getSymbolsNode()

        gElement = etree.SubElement(symbolsNode, "g")
        gElement.attrib["style"] = "display:inline"
        gElement.attrib["id"] = self.name

        imgElement = etree.SubElement(gElement, "image")
        imgElement.attrib["{http://www.w3.org/1999/xlink}href"] = self.path
        imgElement.attrib["id"] = self.name + "Group"
        imgElement.attrib["x"] = str(self.coordinates[0])
        imgElement.attrib["y"] = str(self.coordinates[1])
        imgElement.attrib["width"] = "30"
        imgElement.attrib["height"] = "30"

    def isCorrect(self):
        return os.path.isfile(self.path)
