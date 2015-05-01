from PyQt4.QtGui import QLabel, QColorDialog

class ColorChooser(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.colorDialog = QColorDialog()
        self.setToolTip("Choose section color")
        self.selectedColor = "white"
        self.updateLabelColor()

    def mousePressEvent(self, QMouseEvent):
        self.colorDialog.exec_()
        self.selectedColor = self.colorDialog.selectedColor().name()
        self.updateLabelColor()

    def updateLabelColor(self):
        styleSheet = "background-color:" + self.selectedColor + ";"
        styleSheet += "border-radius:7px"
        self.setStyleSheet(styleSheet)

    def getSelectedColor(self):
        return self.selectedColor

    def setColor(self, color):
        self.selectedColor = color
        self.updateLabelColor()