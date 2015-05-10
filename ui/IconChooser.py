from PyQt4.QtGui import QLabel, QFileDialog
from PyQt4 import QtCore

class IconChooser(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.iconDialog = QFileDialog()
        self.setToolTip("Choose device icon")
        self.selectedIcon = None
        self.updateLabelIcon()

    def mousePressEvent(self, QMouseEvent):
        self.selectedIcon = self.iconDialog.getOpenFileName()
        print "Selected icon=" + str(self.selectedIcon)
        self.updateLabelIcon()

    def updateLabelIcon(self):
        htmlText = "<img src='"
        htmlText += str(self.selectedIcon)
        htmlText += "' with='40' height='40'/>"
        # print "Updating with " + htmlText
        self.setText(htmlText)
        self.emit(QtCore.SIGNAL("iconUpdated()"))

    def getSelectedIcon(self):
        return self.selectedIcon

    def setIcon(self, iconPath):
        self.selectedIcon = iconPath
        self.updateLabelIcon()