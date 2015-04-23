from LinacAbstractSection import LinacAbstractSection

class LinacSubsection(LinacAbstractSection):
    def __init__(self, name, colour, startCoordinate, width):
        LinacAbstractSection.__init__(self, name, colour, startCoordinate, width)

    def updateSvg(self):
        pass