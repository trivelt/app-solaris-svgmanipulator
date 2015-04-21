from Section import Section

class LinacAbstractSection(Section):
    def __init__(self, name, colour, startCoordinate, width):
        Section.__init__(self, name, colour)
        self.startCoordinate = startCoordinate
        self.width = width

    def getDistanceBetweenDevices(self):
        return self.width/float(self.numberOfDevices()+1)