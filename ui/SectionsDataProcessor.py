from src.SvgDrawer import SvgDrawer

class SectionsDataProcesssor:
    def __init__(self, svgDrawer):
        self.svgDrawer = svgDrawer

    def processLinacSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            widthInPixels = sizeInPercent*7770.0
            newSection = self.svgDrawer.addSectionToLinac(name, color, widthInPixels)

    def processRingSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            angleInDegrees = sizeInPercent*360.0
            newSection = self.svgDrawer.addSectionToRing(name, color, angleInDegrees)

    def processSectionData(self, sectionData):
            [name, color, sizeInPercent, displayedNameFlag, displayedName] = self.processBaseSectionData(sectionData)
            subsectionsData = None
            if len(sectionData) > 5:
                subsectionsData = sectionData[5]
            return [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData]

    def processBaseSectionData(self, sectionData):
            name = str(sectionData[0])
            sizeInPercent = float(str(sectionData[1]).replace(",","."))/100.0
            color = str(sectionData[2])
            displayedNameFlag = bool(sectionData[3])
            displayedName = str(sectionData[4])
            return [name, color, sizeInPercent, displayedNameFlag, displayedName]