from PyQt4.QtGui import QDialog, QPushButton, QVBoxLayout, QScrollArea, QWidget
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from BaseSectionWidget import BaseSectionWidget


class SubsectionsDialog(QDialog):
    def __init__(self, strt, parent=None):
        QDialog.__init__(self, parent)
        self.subsectionWidgets = list()
        self.setMinimumWidth(450)
        self.setMinimumHeight(600)

        self.setupLayout()
        self.setupScrollArea()
        self.addSectionButton = QPushButton(self.containerWidget)
        self.addSectionButton.setText("Add new section")
        self.layout.addWidget(self.addSectionButton)

        self.connect(self.addSectionButton, QtCore.SIGNAL("clicked()"), self.addNewSection)

    def setupLayout(self):
        self.containerWidget = QWidget(self)
        self.widgetHeight = 120
        self.containerWidget.setGeometry(QRect(0,0,450,self.widgetHeight))

        self.layout = QVBoxLayout()
        self.containerWidget.setLayout(self.layout)

    def setupScrollArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setMaximumWidth(440)
        self.scrollArea.setMinimumHeight(600)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setWidget(self.containerWidget)


    def addNewSection(self):
        newSection = BaseSectionWidget(self.containerWidget)
        widgetPosition = len(self.subsectionWidgets)
        self.layout.insertWidget(widgetPosition, newSection)
        self.subsectionWidgets.append(newSection)

        self.widgetHeight += 80
        self.containerWidget.resize(450,self.widgetHeight)

        self.connect(newSection, QtCore.SIGNAL("remove()"), self.removeSection)


    def removeSection(self):
        sender = self.sender()
        self.subsectionWidgets.remove(sender)
        sender.setVisible(False)

        self.widgetHeight -= 80
        self.containerWidget.resize(450,self.widgetHeight)

    def getNumberOfSubsections(self):
        return len(self.subsectionWidgets)

    def getSubsections(self):
        return self.subsectionWidgets