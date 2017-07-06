# -*- coding: utf-8 -*-
"""
OnCue Projector
Copyright 2017 Andrew Wong <featherbear@navhaxs.au.eu.org>

The following code is licensed under the GNU Public License Version v3.0

File: oncue/forms/colorPicker.py
"""


from PyQt5 import QtCore, QtWidgets

class customQColorDialog(QtWidgets.QColorDialog):
    """
    Color picker override
    """
    def __init__(self):
        QtWidgets.QColorDialog.__init__(self)
        self.setOption(QtWidgets.QColorDialog.NoButtons)
        """
        QColorDialog
            [0] PyQt5.QtWidgets.QVBoxLayout
            [1] PyQt5.QtWidgets.QWidget             | Basic Color Grid
            [2] PyQt5.QtWidgets.QLabel              | Basic Color Label
            [3] PyQt5.QtWidgets.QPushButton         | Pick Screen Color Button
            [4] PyQt5.QtWidgets.QLabel              | Background for the colour preview
            [5] PyQt5.QtWidgets.QWidget             | Custom Color Grid
            [6] PyQt5.QtWidgets.QLabel              | Custom Color Label
            [7] PyQt5.QtWidgets.QPushButton         | Add to Custom Colors Button
            [8] PyQt5.QtWidgets.QFrame              | Hue Saturation Picker
            [9] PyQt5.QtWidgets.QWidget             | Intensity Slider
            [10] PyQt5.QtWidgets.QWidget            | Value and Preview
            [11] PyQt5.QtWidgets.QDialogButtonBox   | Dialog Buttons
            [12] PyQt5.QtCore.QTimer                | ???
        """
        self.children()[10].children()[16].setText("&Hex:")
        [self.children()[1].setParent(None) for elem in range(7)]  # Remove elements 1-7
        self.updateColor()
        # Elements 0, 8, 9, 10, 11 are important

    def updateColor(self, colorHex="FFFFFF"):
        foc = self.children()[3].children()[17]
        foc.clear()
        foc.insert("#" + colorHex)

    def getColor(self):
        return self.children()[3].children()[17].text()[1:]


class colorPicker(QtWidgets.QDialog):
    def __init__(self, colorDict, theme=("d8d8d8", "808080", "bcbcbc")):
        QtWidgets.QDialog.__init__(self)
        self.colorDict = colorDict
        self.theme = theme
        self.colordialog = customQColorDialog()
        self.setupUi(self)
        self.setWindowTitle("Colour Picker")

    def setupUi(self, colorPicker):
        """
        Interface setup
        """
        class entryButton(QtWidgets.QPushButton):
            def __init__(self, text, parent):
                """
                Create category button 
                """
                self.parent = parent
                self.identifier = text
                QtWidgets.QPushButton.__init__(self)
                self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum))
                self.setCheckable(True)
                self.setAutoExclusive(True)
                self.setText(text)
                self.hexValue = self.parent.colorDict[text]
                self.toggled.connect(self.handleChange)

            def handleChange(self, state):
                if state:
                    self.parent.activeButton = self
                    self.parent.colordialog.updateColor(self.parent.colorDict[self.identifier])
                else:
                    self.parent.colorDict[self.identifier] = self.parent.colordialog.getColor()

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("colorPicker")
        self.resize(900, 480)
        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())
        self.setStyleSheet("QWidget {\n"
                           "text-align: center;\n"
                           "color: black;\n"
                           "border: none;\n"
                           "text-decoration: none;\n"
                           "}")
        self.theming = QtWidgets.QFrame(self)
        self.theming.setGeometry(QtCore.QRect(0, 0, 900, 480))
        self.theming.setStyleSheet("QPushButton {background-color: #%s; color: white;}"
                                   "QPushButton:hover {background-color: #%s;}"
                                   "QPushButton:checked {background-color: #%s}" % self.theme)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.theming)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 840, 480))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        if not isinstance(self.colorDict, str) and len(self.colorDict) != 0:
            self.verticalLayout = QtWidgets.QVBoxLayout()
            [self.verticalLayout.addWidget(entryButton(label, self)) for label in self.colorDict]
            self.verticalLayout.itemAt(0).widget().click()
            self.horizontalLayout.addLayout(self.verticalLayout)
            self.horizontalLayout.setStretch(1, 1)
        else:
            self.colordialog.updateColor(self.colorDict)
        self.horizontalLayout.addWidget(self.colordialog)
        self.response = QtWidgets.QDialogButtonBox(self.theming)
        self.response.setGeometry(QtCore.QRect(755, 455, 81, 20))
        self.response.setOrientation(QtCore.Qt.Horizontal)
        self.response.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.response.accepted.connect(self.OK)
        self.response.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(self)

    def OK(self):
        if isinstance(self.colorDict, str):
            self.colorDict = self.colordialog.getColor()
        else:
            self.activeButton.handleChange(False)
        self.accept()

    def exec_(self):
        return self.colorDict if super().exec_() else False
