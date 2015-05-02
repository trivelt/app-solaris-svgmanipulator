from src.SvgDrawer import SvgDrawer
from src.LinacSection import LinacSection
from src.Ring import RingSection

class SectionsDataProcesssor:
    def __init__(self, svgDrawer):
        self.svgDrawer = svgDrawer

    def processLinacSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            widthInPixels = sizeInPercent * 7770.0
            newSection = self.svgDrawer.addSectionToLinac(name, color, widthInPixels)
            self.processSubsectionsData(newSection, subsectionsData)

    def processRingSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            angleInDegrees = sizeInPercent * 360.0
            newSection = self.svgDrawer.addSectionToRing(name, color, angleInDegrees)
            self.processSubsectionsData(newSection, subsectionsData)

    def processSectionData(self, sectionData):
            [name, color, sizeInPercent, displayedNameFlag, displayedName] = self.processBaseSectionData(sectionData)
            subsectionsData = sectionData[5]
            return [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData]

    def processSubsectionsData(self, parentSection, subsectionsData):
        for subsection in subsectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName] = self.processBaseSectionData(subsection)
            if isinstance(parentSection, LinacSection):
                size = sizeInPercent * parentSection.width
            elif isinstance(parentSection, RingSection):
                size = sizeInPercent * parentSection.angle
            parentSection.addSubsection(name, color, size)

    def processBaseSectionData(self, sectionData):
            name = str(sectionData[0])
            sizeInPercent = float(str(sectionData[1]).replace(",","."))/100.0
            color = str(sectionData[2])
            displayedNameFlag = bool(sectionData[3])
            displayedName = str(sectionData[4])
            return [name, color, sizeInPercent, displayedNameFlag, displayedName]