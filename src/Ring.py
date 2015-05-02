from RingSection import RingSection
from Accelerator import Accelerator

class Ring(Accelerator):
    def __init__(self):
        Accelerator.__init__(self)
        self.radius = 2645.4143

    def addSection(self, name, colour=None, angleInDegrees=45):
        startAngle = self.computeNewSectionStartAngle()
        newSection = RingSection(name, colour, startAngle, angleInDegrees)
        self.sections.append(newSection)
        print("Adding new section " + name + " to the ring")
        return newSection

    def computeNewSectionStartAngle(self):
        if len(self.sections) == 0:
            return -90
        else:
            lastSection = self.sections[-1]
            return lastSection.endAngle

    def updateSvg(self):
        for section in self.sections:
            section.updateSvg()