from src.SvgDrawer import SvgDrawer
from src.LinacSection import LinacSection
from src.Ring import RingSection

class SectionsDataProcesssor:
    def __init__(self, svgDrawer):
        self.svgDrawer = svgDrawer
        self.sumOfLinacSectionsWidth = 0
        self.sumOfRingSectionWidth = 0

    def processLinacSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            widthInPixels = sizeInPercent * 7770.0
            self.sumOfLinacSectionsWidth += sizeInPercent
            newSection = self.svgDrawer.addSectionToLinac(name, color, widthInPixels)
            self.setDisplayedNameIfNecessary(newSection, displayedNameFlag, displayedName)
            self.processSubsectionsData(newSection, subsectionsData)

    def processRingSections(self, sectionsData):
        for section in sectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData] = self.processSectionData(section)
            angleInDegrees = sizeInPercent * 360.0
            self.sumOfRingSectionWidth += sizeInPercent
            newSection = self.svgDrawer.addSectionToRing(name, color, angleInDegrees)
            self.setDisplayedNameIfNecessary(newSection, displayedNameFlag, displayedName)
            self.processSubsectionsData(newSection, subsectionsData)

    def processSectionData(self, sectionData):
            [name, color, sizeInPercent, displayedNameFlag, displayedName] = self.processBaseSectionData(sectionData)
            subsectionsData = sectionData[5]
            return [name, color, sizeInPercent, displayedNameFlag, displayedName, subsectionsData]

    def processSubsectionsData(self, parentSection, subsectionsData):
        for subsection in subsectionsData:
            [name, color, sizeInPercent, displayedNameFlag, displayedName] = self.processBaseSectionData(subsection)
            size = 0
            if isinstance(parentSection, LinacSection):
                size = sizeInPercent * parentSection.width
            elif isinstance(parentSection, RingSection):
                size = sizeInPercent * parentSection.angle
            newSubsection = parentSection.addSubsection(name, color, size)
            self.setDisplayedNameIfNecessary(newSubsection, displayedNameFlag, displayedName)

    def processBaseSectionData(self, sectionData):
            name = str(sectionData[0])
            sizeInPercent = float(str(sectionData[1]).replace(",","."))/100.0
            color = str(sectionData[2])
            displayedNameFlag = bool(sectionData[3])
            displayedName = str(sectionData[4])
            return [name, color, sizeInPercent, displayedNameFlag, displayedName]

    def setDisplayedNameIfNecessary(self, section, displayedNameFlag, displayedName):
        if displayedNameFlag == True:
            section.setDisplayedName(displayedName)

    def drawLastSectionIfNecessary(self):
        if self.sumOfLinacSectionsWidth < 1.0:
            widthInPixels = (1.0 - self.sumOfLinacSectionsWidth) * 7770.0
            self.svgDrawer.addSectionToLinac("", "#b3b3b3", widthInPixels)
        if self.sumOfRingSectionWidth < 1.0:
            angle = (1.0 - self.sumOfRingSectionWidth) * 360.0
            if angle == 360.0:
                angle = 359.9999
            self.svgDrawer.addSectionToRing("", "#b3b3b3", angle)