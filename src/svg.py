#!/usr/bin/python

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class SVG:
    def __init__(self):
        self.svg = None

    def getSvg(self):
        return self.svg

    def setSvg(self, svg):
        self.svg = svg

    def getBackgroundNode(self):
        return self.getElementById("background", self.svg[3])

    def getZoom1Background(self):
        backgroundNode = self.getBackgroundNode()
        return self.getElementById("layer2", backgroundNode)

    def getZoom2Background(self):
        backgroundNode = self.getBackgroundNode()
        return self.getElementById("layer1", backgroundNode)

    def getSymbolsNode(self):
        return self.getSubsystemNode("symbols")

    def getSubsystemNode(self, name):
        return self.getElementByLabel(name, self.svg[3])

    def getSubsystemZoomNode(self, name):
        subsystemNode = self.getSubsystemNode(name)
        return self.getElementByLabel("zoom2", subsystemNode)

    def getElementById(self, elementName, parentNode):
        searchElement = None
        if parentNode == None:
            return searchElement
        for element in parentNode:
            if "id" in element.attrib and element.attrib["id"] == elementName:
                searchElement = element
        return searchElement

    def getElementByLabel(self, elementName, parentNode):
        searchedNode = None
        if parentNode == None:
            return searchedNode
        label = "{http://www.inkscape.org/namespaces/inkscape}label"
        for group in parentNode:
            if label in group.attrib and group.attrib[label] == elementName:
                searchedNode = group
        return searchedNode