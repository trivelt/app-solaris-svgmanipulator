from RingSection import RingSection

class Ring:
    def __init__(self):
        self.sections = list()
        self.radius = 2645.4143

    def addSection(self, name, colour=None, angleInDegrees=45):
        startAngle = self.computeNewSectionStartAngle()
        newSection = RingSection(name, colour, startAngle, angleInDegrees)
        self.sections.append(newSection)
        return newSection

    def computeNewSectionStartAngle(self):
        if len(self.sections) == 0:
            return -90
        else:
            lastSection = self.sections[-1]
            return lastSection.endAngle

    def getSection(self, name):
        searchedSection = None
        for section in self.sections:
            if section.longName == name:
                searchedSection = section
            for subsection in section.subsections:
                if subsection.longName == name:
                    searchedSection = subsection
        return searchedSection

    def updateSvg(self):
        for section in self.sections:
            section.updateSvg()