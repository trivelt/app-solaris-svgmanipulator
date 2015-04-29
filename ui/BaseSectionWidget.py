from PyQt4.QtGui import QWidget, QLineEdit, QPushButton, QCheckBox
from PyQt4.Qt import QRect
from PyQt4 import QtCore
from ColorChooser import ColorChooser

class BaseSectionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.resize(400,80)

        self.sectionNameEdit = QLineEdit(self)
        self.sectionNameEdit.setGeometry(QRect(5,5,120,30))
        self.sectionNameEdit.setPlaceholderText("Section name")
        self.sectionNameEdit.setToolTip("Name of new section")

        self.widthEdit = QLineEdit(self)
        self.widthEdit.setGeometry(QRect(130,5,50,30))
        self.widthEdit.setPlaceholderText("size")
        self.widthEdit.setToolTip("Size of section in percent")

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

        self.connect(self.displayedNameCheckBox, QtCore.SIGNAL("clicked()"), self.changeDisplayedName)

    def changeDisplayedName(self):
        if self.displayedNameCheckBox.isChecked():
            self.displayedNameEdit.setVisible(True)
            self.displayedNameCheckBox.setText("")
        else:
            self.displayedNameEdit.setVisible((False))
            self.displayedNameCheckBox.setText("Change displayed name")

    def getName(self):
        return self.sectionNameEdit.text()