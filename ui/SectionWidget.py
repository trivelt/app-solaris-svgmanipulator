import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SettingsCloud import SettingsCloud
from BaseSectionWithSubsectionsWidget import BaseSectionWithSubsectionsWidget
from SectionsContainerWidget import SectionsContainerWidget

class SectionWidget(SectionsContainerWidget):
    def __init__(self, parent=None, isLinacSectionWidget=True):
        SectionsContainerWidget.__init__(self, parent, isLinacSectionWidget, BaseSectionWithSubsectionsWidget)

    def setDefaultValues(self, section):
        section.setColor(SettingsCloud.getParameter("sectionColor"))
        self.setSectionSize(section)

    def setSectionSize(self, section):
        if self.isLinacSection:
            defaultSize = SettingsCloud.getParameter("linacSectionSize")
        else:
            defaultSize = SettingsCloud.getParameter("ringSectionSize")
        section.setSize(defaultSize)
        self.updateSumOfSize(section)
