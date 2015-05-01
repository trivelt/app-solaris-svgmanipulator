import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.SettingsCloud import SettingsCloud
from PyQt4.QtGui import QPushButton, QVBoxLayout, QScrollArea, QWidget, QMessageBox
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWithSubsectionsWidget import BaseSectionWithSubsectionsWidget


class SectionWidget(QWidget):
    def __init__(self, parent=None, isLinacSectionWidget=True):
        QWidget.__init__(self, parent)
        self.sectionWidgets = list()
        self.setMinimumWidth(460)
        self.setMinimumHeight(600)
        self.isLinacSectionWidget = isLinacSectionWidget

        self.setupLayout()
        self.setupScrollArea()

        self.addSectionButton = QPushButton(self.containerWidget)
        self.addSectionButton.setText("Add new section")
        self.layout.addWidget(self.addSectionButton)

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
        newSection = BaseSectionWithSubsectionsWidget(self.containerWidget, self.isLinacSectionWidget)
        self.setDefaultValues(newSection)
        widgetPosition = len(self.sectionWidgets)
        self.layout.insertWidget(widgetPosition, newSection)
        self.sectionWidgets.append(newSection)

        self.widgetHeight += 80
        self.containerWidget.resize(450,self.widgetHeight)

        self.connect(newSection, QtCore.SIGNAL("remove()"), self.removeSection)

    def removeSection(self):
        messageBox = QMessageBox(self)
        userReply = messageBox.question(self, "Are you sure?", "Do you want to remove this section?",
                                        QMessageBox.Yes|QMessageBox.No)
        if userReply == QMessageBox.Yes:
            sender = self.sender()
            self.layout.removeWidget(sender)
            self.sectionWidgets.remove(sender)
            sender.setVisible(False)

            self.widgetHeight -= 80
            self.containerWidget.resize(460,self.widgetHeight)

    def getNumberOfSubsections(self):
        return len(self.sectionWidgets)

    def getSectionsData(self):
        sectionsData = list()
        for section in self.sectionWidgets:
            sectionsData.append(section.getSectionData())
        return sectionsData

    def setDefaultValues(self, section):
        section.setColor(SettingsCloud.getParameter("sectionColor"))
        print "Is linac section widget? " + str(self.isLinacSectionWidget)