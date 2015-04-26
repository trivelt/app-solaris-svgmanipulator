from Accelerator import Accelerator
from LinacSection import LinacSection

class Linac(Accelerator):
    def __init__(self):
        Accelerator.__init__(self)
        self.sections = list()
        self.width = 7770.0
        LinacSection.id = 1

    def addSection(self, name, colour=None, width=630):
        print("Adding new section " + str(name) + " to the linac")
        if colour is None:
            colour = self.getNextSectionColour()
        coordinate = self.computeNewSectionCoordinate()
        newSection = LinacSection(name, colour, coordinate, width)
        self.sections.append(newSection)
        return newSection

    def addLastLongSection(self):
        colour = self.getNextSectionColour()
        coordinate = self.computeNewSectionCoordinate()
        newSection = LinacSection("", colour, coordinate, 1885+self.width-coordinate)
        self.sections.append(newSection)

    def computeNewSectionCoordinate(self):
        if len(self.sections) == 0:
            return 1885
        else:
            lastSection = self.sections[-1]
            startOfLastSection = lastSection.startCoordinate
            widthOfLastSection = lastSection.width
            startOfNextSection = startOfLastSection+widthOfLastSection
            return startOfNextSection

    def updateSvg(self):
        for section in self.sections:
            section.updateSvg()
