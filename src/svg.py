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
        return self.getElement("background", self.svg[3])

    def getZoom1Background(self):
        backgroundNode = self.getBackgroundNode()
        return self.getElement("layer2", backgroundNode)

    def getZoom2Background(self):
        backgroundNode = self.getBackgroundNode()
        return self.getElement("layer1", backgroundNode)

    def getSymbolsNode(self):
        return self.getSubsystemNode("symbols")

    def getSubsystemNode(self, name):
        searchedNode = None
        for group in self.svg[3]:
            if group.attrib["{http://www.inkscape.org/namespaces/inkscape}label"] == name:
                searchedNode = group
        return searchedNode

    def getElement(self, elementName, parentNode):
        searchElement = None
        for element in parentNode:
            if element.attrib["id"] == elementName:
                searchElement = element
        return searchElement