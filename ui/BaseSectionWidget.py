from PyQt4.QtGui import QWidget, QLineEdit, QPushButton, QCheckBox, QDoubleSpinBox, QPixmap, QIcon
from PyQt4.Qt import QRect, QSize
from PyQt4 import QtCore
from ColorChooser import ColorChooser

class BaseSectionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.resize(400,80)

        self.sectionNameEdit = QLineEdit(self)
        self.sectionNameEdit.setGeometry(QRect(0,5,110,30))
        self.sectionNameEdit.setPlaceholderText("Section name")
        self.sectionNameEdit.setToolTip("Name of new section")

        self.sizeEdit = QDoubleSpinBox(self)
        self.sizeEdit.setGeometry(QRect(115,5,65,30))
        self.sizeEdit.setToolTip("Size of section in percent")

        self.colorLabel = ColorChooser(self)
        self.colorLabel.setGeometry(QRect(185,8,25,25))

        self.displayedNameCheckBox = QCheckBox(self)
        self.displayedNameCheckBox.setGeometry(215, 5, 185, 30)
        self.displayedNameCheckBox.setText("Change displayed name")
        self.displayedNameCheckBox.setStyleSheet("font-size:11px;")

        self.displayedNameEdit = QLineEdit(self)
        self.displayedNameEdit.setGeometry(QRect(235,5,120,30))
        self.displayedNameEdit.setPlaceholderText("Displayed name")
        self.displayedNameEdit.setToolTip("Displayed name of new section")
        self.displayedNameEdit.setVisible(False)

        self.removeButton = QPushButton(self)
        self.removeButton.setGeometry(QRect(385,5,35,30))
        self.removeButton.setToolTip("Remove section")
        pixmap = QPixmap("./removeIcon.png")
        buttonIcon = QIcon(pixmap)
        self.removeButton.setIcon(buttonIcon)
        self.removeButton.setIconSize(QSize(25,25))

        self.connect(self.displayedNameCheckBox, QtCore.SIGNAL("clicked()"), self.changeDisplayedName)
        self.connect(self.removeButton, QtCore.SIGNAL("clicked()"), QtCore.SIGNAL("remove()"))

    def changeDisplayedName(self):
        if self.displayedNameCheckBox.isChecked():
            self.displayedNameEdit.setVisible(True)
            self.displayedNameCheckBox.setText("")
        else:
            self.displayedNameEdit.setVisible((False))
            self.displayedNameCheckBox.setText("Change displayed name")

    def getName(self):
        return self.sectionNameEdit.text()

    def getSectionData(self):
        name = self.sectionNameEdit.text()
        size = self.sizeEdit.text()
        color = self.colorLabel.getSelectedColor()
        displayedNameFlag = self.displayedNameCheckBox.isChecked()
        displayedName = self.displayedNameEdit.text()
        return (name, size, color, displayedNameFlag, displayedName)