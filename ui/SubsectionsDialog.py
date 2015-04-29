from PyQt4.QtGui import QDialog, QPushButton, QLabel, QScrollArea
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWidget import BaseSectionWidget


class SubsectionsDialog(QDialog):
    def __init__(self, strt, parent=None):
        QDialog.__init__(self, parent)
        self.subsectionWidgets = list()

        self.resize(450,800)
        self.buttonPosition = 60

        section = BaseSectionWidget(self)
        section.setGeometry(QRect(5,5, 450, 80))

        self.addSectionButton = QPushButton(self)
        self.addSectionButton.setText("Add new section")
        self.addSectionButton.setGeometry(QRect(165,self.buttonPosition,120,40))

        self.connect(self.addSectionButton, QtCore.SIGNAL("clicked()"), self.addNewSection)





    def addNewSection(self):
        newSection = BaseSectionWidget(self)
        newSection.setGeometry(QRect(5,self.buttonPosition, 450, 80))
        newSection.setVisible(True)
        self.subsectionWidgets.append(newSection)

        self.buttonPosition += 70
        self.addSectionButton.setGeometry(QRect(165,self.buttonPosition,120,40))


    def getNumberOfSubsections(self):
        return len(self.subsectionWidgets)