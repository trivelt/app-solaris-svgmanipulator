import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SettingsCloud import SettingsCloud
from PyQt4.QtGui import QDialog
from BaseSectionWidget import BaseSectionWidget
from SectionsContainerWidget import SectionsContainerWidget

class subsectionContainerWidget(SectionsContainerWidget):
    lastSectionColor = None

    def __init__(self, parent=None, isLinacSectionWidget=True):
        SectionsContainerWidget.__init__(self, parent, isLinacSectionWidget, BaseSectionWidget)

    def setDefaultValues(self, section):
        #section.colorLabel.setColor(SettingsCloud.getParameter("subsectionColor"))
        self.setSectionColor(section)
        self.setSectionSize(section)

    def setSectionColor(self, section):
        firstColor = SettingsCloud.getParameter("subsectionFirstColor")
        secondColor = SettingsCloud.getParameter("subsectionSecondColor")
        if subsectionContainerWidget.lastSectionColor == secondColor:
            section.colorLabel.setColor(firstColor)
            subsectionContainerWidget.lastSectionColor = firstColor
        else:
            section.colorLabel.setColor(secondColor)
            subsectionContainerWidget.lastSectionColor = secondColor

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
