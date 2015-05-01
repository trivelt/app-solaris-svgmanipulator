import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SettingsCloud import SettingsCloud
from PyQt4.QtGui import QDialog, QPushButton, QVBoxLayout, QScrollArea, QWidget, QMessageBox
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWidget import BaseSectionWidget


class SubsectionsDialog(QDialog):
    def __init__(self, parent=None, isLinacSection=True):
        QDialog.__init__(self, parent)
        self.isLinacSection = isLinacSection
        self.subsectionWidgets = list()
        self.setMinimumWidth(460)
        self.setMinimumHeight(600)
        self.sumSize = 0

        self.setupLayout()
        self.setupScrollArea()
        self.addSectionButton = QPushButton(self.containerWidget)
        self.addSectionButton.setText("Add new section")
        self.layout.addWidget(self.addSectionButton)

        self.setWindowTitle("Subsections editing")

        self.connect(self.addSectionButton, QtCore.SIGNAL("clicked()"), self.addNewSection)

    def setupLayout(self):
        self.containerWidget = QWidget(self)
        self.widgetHeight = 120
        self.containerWidget.setGeometry(QRect(0,0,460,self.widgetHeight))

        self.layout = QVBoxLayout()
        self.containerWidget.setLayout(self.layout)

    def setupScrollArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setMaximumWidth(460)
        self.scrollArea.setMinimumHeight(600)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setWidget(self.containerWidget)

    def addNewSection(self):
        newSection = BaseSectionWidget(self.containerWidget)
        widgetPosition = len(self.subsectionWidgets)
        self.layout.insertWidget(widgetPosition, newSection)
        self.subsectionWidgets.append(newSection)
        self.setDefaultValues(newSection)

        self.widgetHeight += 80
        self.containerWidget.resize(460,self.widgetHeight)

        self.connect(newSection, QtCore.SIGNAL("remove()"), self.removeSection)
        self.connect(newSection, QtCore.SIGNAL("sizeValueChanged(QWidget*)"), self.updateSumOfSize)

    def setDefaultValues(self, section):
        section.colorLabel.setColor(SettingsCloud.getParameter("subsectionColor"))
        self.setSubsectionSize(section)

    def setSubsectionSize(self, section):
        if self.isLinacSection:
            defaultSize = SettingsCloud.getParameter("linacSubsectionSize")
        else:
            defaultSize = SettingsCloud.getParameter("ringSubsectionSize")
        section.sizeEdit.setValue(defaultSize)
        self.updateSumOfSize(section)

    def updateSumOfSize(self, sectionWidget):
        self.sumSize = 0
        for subsection in self.subsectionWidgets:
            self.sumSize += subsection.sizeEdit.value()
        if self.sumSize > 100:
            diff = self.sumSize - 100.0
            actualSize = sectionWidget.sizeEdit.value()
            sectionWidget.sizeEdit.setValue(actualSize - diff)

    def removeSection(self):
        messageBox = QMessageBox(self)
        userReply = messageBox.question(self, "Are you sure?", "Do you want to remove this section?",
                                        QMessageBox.Yes|QMessageBox.No)
        if userReply == QMessageBox.Yes:
            sender = self.sender()
            self.layout.removeWidget(sender)
            self.subsectionWidgets.remove(sender)
            sender.setVisible(False)

            self.widgetHeight -= 80
            self.containerWidget.resize(460,self.widgetHeight)

    def getNumberOfSubsections(self):
        return len(self.subsectionWidgets)

    def getSubsections(self):
        return self.subsectionWidgets

    def getSubsectionsData(self):
        subsectionsData = list()
        for subsection in self.subsectionWidgets:
            subsectionsData.append(subsection.getSectionData())
        return subsectionsData