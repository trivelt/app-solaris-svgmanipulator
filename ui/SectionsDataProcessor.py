from src.SvgDrawer import SvgDrawer

class SectionsDataProcesssor:
    def __init__(self, svgDrawer):
        self.svgDrawer = svgDrawer


    def processLinacSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionsData(section)
            widthInPixels = sizeInPercent*7770.0
            self.svgDrawer.addSectionToLinac(name, color, widthInPixels)


    def processRingSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionsData(section)

            angleInDegrees = sizeInPercent*360.0
            self.svgDrawer.addSectionToRing(name, color, angleInDegrees)

    def processSectionsData(self, sectionsData):
            subsectionsData = None
            if len(sectionsData) > 5:
                subsectionsData = sectionsData[5]
            name = str(sectionsData[0])
            sizeInPercent = float(str(sectionsData[1]).replace(",","."))/100.0
            color = str(sectionsData[2])
            displayedNameFlag = bool(sectionsData[3])
            displayedName = str(sectionsData[4])

            return [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData]