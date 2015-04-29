from PyQt4.QtGui import QWidget, QPushButton
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWidget import BaseSectionWidget

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
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
        print "Adding"
        newSection = BaseSectionWidget(self)
        newSection.setGeometry(QRect(5,self.buttonPosition, 450, 80))
        self.buttonPosition += 70

        newSection.setVisible(True)


        self.addSectionButton.setGeometry(QRect(165,self.buttonPosition,120,40))
