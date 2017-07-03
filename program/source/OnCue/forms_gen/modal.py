# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modal.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_modal_ynoc(object):
    def setupUi(self, modal_ynoc):
        modal_ynoc.setObjectName("modal_ynoc")
        modal_ynoc.setWindowModality(QtCore.Qt.ApplicationModal)
        modal_ynoc.resize(508, 309)
        font = QtGui.QFont()
        font.setPointSize(12)
        modal_ynoc.setFont(font)
        modal_ynoc.setStyleSheet("QWidget {\n"
"text-align: center;\n"
"color: black;\n"
"border: none;\n"
"text-decoration: none;\n"
"}")
        modal_ynoc.setModal(True)
        self.theming = QtWidgets.QFrame(modal_ynoc)
        self.theming.setGeometry(QtCore.QRect(0, 0, 508, 309))
        self.theming.setStyleSheet("QPushButton {\n"
"background-color: #BAB9BA;\n"
"color: white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #8CC5FF;\n"
"}")
        self.theming.setObjectName("theming")
        self.response = QtWidgets.QDialogButtonBox(self.theming)
        self.response.setGeometry(QtCore.QRect(20, 250, 471, 41))
        self.response.setStyleSheet("width: 157px; height: 100%;")
        self.response.setOrientation(QtCore.Qt.Horizontal)
        self.response.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Yes)
        self.response.setCenterButtons(True)
        self.response.setObjectName("response")
        self.message = QtWidgets.QLabel(self.theming)
        self.message.setGeometry(QtCore.QRect(20, 20, 471, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.message.setFont(font)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.message.raise_()
        self.response.raise_()

        self.retranslateUi(modal_ynoc)
        self.response.accepted.connect(modal_ynoc.accept)
        self.response.rejected.connect(modal_ynoc.reject)
        QtCore.QMetaObject.connectSlotsByName(modal_ynoc)

    def retranslateUi(self, modal_ynoc):
        _translate = QtCore.QCoreApplication.translate
        modal_ynoc.setWindowTitle(_translate("modal_ynoc", "OnCue"))

