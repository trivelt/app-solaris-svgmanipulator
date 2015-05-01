import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SettingsCloud import SettingsCloud
from PyQt4.QtGui import QDialog
from BaseSectionWidget import BaseSectionWidget
from SectionsContainerWidget import SectionsContainerWidget

class subsectionContainerWidget(SectionsContainerWidget):
    def __init__(self, parent=None, isLinacSectionWidget=True):
        SectionsContainerWidget.__init__(self, parent, isLinacSectionWidget, BaseSectionWidget)

    def setDefaultValues(self, section):
        section.colorLabel.setColor(SettingsCloud.getParameter("subsectionColor"))
        self.setSectionSize(section)

    def setSectionSize(self, section):
        if self.isLinacSection:
            defaultSize = SettingsCloud.getParameter("linacSubsectionSize")
        else:
            defaultSize = SettingsCloud.getParameter("ringSubsectionSize")
        section.sizeEdit.setValue(defaultSize)
        self.updateSumOfSize(section)


class SubsectionsDialog(QDialog):
    def __init__(self, parent=None, isLinacSection=True):
        QDialog.__init__(self, parent)
        self.containerWidget = subsectionContainerWidget(self, isLinacSection)

    def getNumberOfSubsections(self):
        return self.containerWidget.getNumberOfSections()

    def getSectionsData(self):
        return self.containerWidget.getSectionsData()
