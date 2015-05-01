from PyQt4.QtGui import QWidget, QPushButton, QLabel
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWidget import BaseSectionWidget
from SubsectionsDialog import SubsectionsDialog

class BaseSectionWithSubsectionsWidget(QWidget):
    def __init__(self, parent=None, isLinacSectionWidget=True):
        QWidget.__init__(self, parent)
        self.subsectionsDialog = SubsectionsDialog(self, isLinacSectionWidget)

        self.resize(450,80)

        self.section = BaseSectionWidget(self)
        self.section.setGeometry(QRect(5,5, 450, 80))

        self.subsectionsLabel = QLabel(self)
        self.subsectionsLabel.setText("Subsections: 0")
        self.subsectionsLabel.setGeometry(QRect(15,40,120,30))

        self.subsectionsEditButton = QPushButton(self)
        self.subsectionsEditButton.setText("+")
        self.subsectionsEditButton.setGeometry(QRect(125,40,20,30))

        self.connect(self.subsectionsEditButton, QtCore.SIGNAL("clicked()"), self.editSubsections)
        self.connect(self.section, QtCore.SIGNAL("remove()"), QtCore.SIGNAL("remove()"))
        self.connect(self.section, QtCore.SIGNAL("sizeValueChanged(QWidget*)"), QtCore.SIGNAL("sizeValueChanged(QWidget*)"))

    def editSubsections(self):
        self.subsectionsDialog.exec_()
        numberOfSubsections = self.subsectionsDialog.getNumberOfSubsections()
        self.subsectionsLabel.setText("Subsections: " + str(numberOfSubsections))

    def getSectionData(self):
        subsectionsData = self.subsectionsDialog.getSectionsData()
        allData = self.section.getSectionData()
        allData.extend(subsectionsData)
        return allData

    def setColor(self, color):
        self.section.colorLabel.setColor(color)

    def setSize(self, size):
        self.section.sizeEdit.setValue(size)

    def getSize(self):
        return self.section.getSize()