# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(900, 900)
        Settings.setMinimumSize(QtCore.QSize(900, 900))
        Settings.setMaximumSize(QtCore.QSize(900, 900))
        Settings.setStyleSheet("QWidget {\n"
"text-align: center;\n"
"color: white;\n"
"border: none;\n"
"text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #727272;\n"
"color: #A7A7A7;\n"
"}")
        self.theming = QtWidgets.QFrame(Settings)
        self.theming.setGeometry(QtCore.QRect(0, 0, 900, 900))
        self.theming.setStyleSheet("QLabel[objectName=\"Header\"] {background: #509DF3;}\n"
"QPushButton {background-color: #BAB9BA;}\n"
"QPushButton:checked {background-color: #509DF3;}\n"
"QPushButton:hover:!checked {background-color: #8CC5FF;}")
        self.theming.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.theming.setFrameShadow(QtWidgets.QFrame.Raised)
        self.theming.setObjectName("theming")
        self.btnBack = QtWidgets.QPushButton(self.theming)
        self.btnBack.setGeometry(QtCore.QRect(0, 0, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBack.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnBack.setStyleSheet("QPushButton {\n"
"background-color: #BAB9BA;\n"
"border: none;\n"
"color: white;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #A0A0A0;\n"
"}\n"
"")
        self.btnBack.setObjectName("btnBack")
        self.viewTabs = QtWidgets.QStackedWidget(self.theming)
        self.viewTabs.setGeometry(QtCore.QRect(10, 160, 881, 671))
        self.viewTabs.setStyleSheet("QLabel, QComboBox QAbstractItemView {\n"
"color: black;\n"
"}\n"
"QLabel:disabled {\n"
"color: grey;\n"
"}")
        self.viewTabs.setObjectName("viewTabs")
        self.viewGeneral = QtWidgets.QWidget()
        self.viewGeneral.setObjectName("viewGeneral")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.viewGeneral)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(-10, 0, 901, 671))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formGeneral = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formGeneral.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formGeneral.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formGeneral.setContentsMargins(20, 30, 80, 0)
        self.formGeneral.setSpacing(10)
        self.formGeneral.setObjectName("formGeneral")
        self.prefTheme_LABEL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.prefTheme_LABEL.setMinimumSize(QtCore.QSize(0, 55))
        self.prefTheme_LABEL.setObjectName("prefTheme_LABEL")
        self.formGeneral.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.prefTheme_LABEL)
        self.prefStageBackground_LABEL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.prefStageBackground_LABEL.setEnabled(False)
        self.prefStageBackground_LABEL.setMinimumSize(QtCore.QSize(0, 55))
        self.prefStageBackground_LABEL.setObjectName("prefStageBackground_LABEL")
        self.formGeneral.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prefStageBackground_LABEL)
        self.prefOutputBackground_LABEL = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.prefOutputBackground_LABEL.setMinimumSize(QtCore.QSize(0, 55))
        self.prefOutputBackground_LABEL.setObjectName("prefOutputBackground_LABEL")
        self.formGeneral.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.prefOutputBackground_LABEL)
        self.prefTheme_widget = QtWidgets.QWidget(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_widget.sizePolicy().hasHeightForWidth())
        self.prefTheme_widget.setSizePolicy(sizePolicy)
        self.prefTheme_widget.setObjectName("prefTheme_widget")
        self.layoutWidget = QtWidgets.QWidget(self.prefTheme_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 55))
        self.layoutWidget.setObjectName("layoutWidget")
        self.prefTheme = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.prefTheme.setContentsMargins(0, 0, 0, 0)
        self.prefTheme.setSpacing(0)
        self.prefTheme.setObjectName("prefTheme")
        self.prefTheme_BLUE = QtWidgets.QPushButton(self.layoutWidget)
        self.prefTheme_BLUE.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_BLUE.sizePolicy().hasHeightForWidth())
        self.prefTheme_BLUE.setSizePolicy(sizePolicy)
        self.prefTheme_BLUE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefTheme_BLUE.setFont(font)
        self.prefTheme_BLUE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefTheme_BLUE.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #509DF3;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #8CC5FF;\n"
"}\n"
"")
        self.prefTheme_BLUE.setCheckable(True)
        self.prefTheme_BLUE.setChecked(True)
        self.prefTheme_BLUE.setAutoExclusive(True)
        self.prefTheme_BLUE.setObjectName("prefTheme_BLUE")
        self.prefTheme.addWidget(self.prefTheme_BLUE)
        self.prefTheme_RED = QtWidgets.QPushButton(self.layoutWidget)
        self.prefTheme_RED.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_RED.sizePolicy().hasHeightForWidth())
        self.prefTheme_RED.setSizePolicy(sizePolicy)
        self.prefTheme_RED.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefTheme_RED.setFont(font)
        self.prefTheme_RED.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefTheme_RED.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #FF6666;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #FFADAD;\n"
"}")
        self.prefTheme_RED.setCheckable(True)
        self.prefTheme_RED.setChecked(False)
        self.prefTheme_RED.setAutoExclusive(True)
        self.prefTheme_RED.setObjectName("prefTheme_RED")
        self.prefTheme.addWidget(self.prefTheme_RED)
        self.prefTheme_GREY = QtWidgets.QPushButton(self.layoutWidget)
        self.prefTheme_GREY.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_GREY.sizePolicy().hasHeightForWidth())
        self.prefTheme_GREY.setSizePolicy(sizePolicy)
        self.prefTheme_GREY.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefTheme_GREY.setFont(font)
        self.prefTheme_GREY.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefTheme_GREY.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #808080;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #BCBCBC;\n"
"}\n"
"")
        self.prefTheme_GREY.setCheckable(True)
        self.prefTheme_GREY.setChecked(False)
        self.prefTheme_GREY.setAutoExclusive(True)
        self.prefTheme_GREY.setObjectName("prefTheme_GREY")
        self.prefTheme.addWidget(self.prefTheme_GREY)
        self.prefTheme_DARK = QtWidgets.QPushButton(self.layoutWidget)
        self.prefTheme_DARK.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_DARK.sizePolicy().hasHeightForWidth())
        self.prefTheme_DARK.setSizePolicy(sizePolicy)
        self.prefTheme_DARK.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefTheme_DARK.setFont(font)
        self.prefTheme_DARK.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefTheme_DARK.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #000;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #494949;\n"
"}\n"
"")
        self.prefTheme_DARK.setCheckable(True)
        self.prefTheme_DARK.setChecked(False)
        self.prefTheme_DARK.setAutoExclusive(True)
        self.prefTheme_DARK.setObjectName("prefTheme_DARK")
        self.prefTheme.addWidget(self.prefTheme_DARK)
        self.prefTheme_CUSTOM = QtWidgets.QPushButton(self.layoutWidget)
        self.prefTheme_CUSTOM.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefTheme_CUSTOM.sizePolicy().hasHeightForWidth())
        self.prefTheme_CUSTOM.setSizePolicy(sizePolicy)
        self.prefTheme_CUSTOM.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefTheme_CUSTOM.setFont(font)
        self.prefTheme_CUSTOM.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefTheme_CUSTOM.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:checked {\n"
"background-color: #BAB9BA;\n"
"}")
        self.prefTheme_CUSTOM.setCheckable(True)
        self.prefTheme_CUSTOM.setChecked(False)
        self.prefTheme_CUSTOM.setAutoExclusive(True)
        self.prefTheme_CUSTOM.setObjectName("prefTheme_CUSTOM")
        self.prefTheme.addWidget(self.prefTheme_CUSTOM)
        self.prefTheme.setStretch(0, 2)
        self.prefTheme.setStretch(1, 2)
        self.prefTheme.setStretch(2, 2)
        self.prefTheme.setStretch(3, 2)
        self.prefTheme.setStretch(4, 1)
        self.formGeneral.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.prefTheme_widget)
        self.prefOutputBackground_widget = QtWidgets.QWidget(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefOutputBackground_widget.sizePolicy().hasHeightForWidth())
        self.prefOutputBackground_widget.setSizePolicy(sizePolicy)
        self.prefOutputBackground_widget.setObjectName("prefOutputBackground_widget")
        self.layoutWidget1 = QtWidgets.QWidget(self.prefOutputBackground_widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 661, 55))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.prefOutputBackground = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.prefOutputBackground.setContentsMargins(0, 0, 0, 0)
        self.prefOutputBackground.setSpacing(0)
        self.prefOutputBackground.setObjectName("prefOutputBackground")
        self.prefOutputBackground_BLACK = QtWidgets.QPushButton(self.layoutWidget1)
        self.prefOutputBackground_BLACK.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefOutputBackground_BLACK.sizePolicy().hasHeightForWidth())
        self.prefOutputBackground_BLACK.setSizePolicy(sizePolicy)
        self.prefOutputBackground_BLACK.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefOutputBackground_BLACK.setFont(font)
        self.prefOutputBackground_BLACK.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefOutputBackground_BLACK.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #000;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #BCBCBC;\n"
"}\n"
"")
        self.prefOutputBackground_BLACK.setCheckable(True)
        self.prefOutputBackground_BLACK.setChecked(False)
        self.prefOutputBackground_BLACK.setAutoExclusive(True)
        self.prefOutputBackground_BLACK.setObjectName("prefOutputBackground_BLACK")
        self.prefOutputBackground.addWidget(self.prefOutputBackground_BLACK)
        self.prefOutputBackground_WHITE = QtWidgets.QPushButton(self.layoutWidget1)
        self.prefOutputBackground_WHITE.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefOutputBackground_WHITE.sizePolicy().hasHeightForWidth())
        self.prefOutputBackground_WHITE.setSizePolicy(sizePolicy)
        self.prefOutputBackground_WHITE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefOutputBackground_WHITE.setFont(font)
        self.prefOutputBackground_WHITE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefOutputBackground_WHITE.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #fff;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #BCBCBC;\n"
"}\n"
"")
        self.prefOutputBackground_WHITE.setCheckable(True)
        self.prefOutputBackground_WHITE.setChecked(False)
        self.prefOutputBackground_WHITE.setAutoExclusive(True)
        self.prefOutputBackground_WHITE.setObjectName("prefOutputBackground_WHITE")
        self.prefOutputBackground.addWidget(self.prefOutputBackground_WHITE)
        self.prefOutputBackground_CUSTOM = QtWidgets.QPushButton(self.layoutWidget1)
        self.prefOutputBackground_CUSTOM.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefOutputBackground_CUSTOM.sizePolicy().hasHeightForWidth())
        self.prefOutputBackground_CUSTOM.setSizePolicy(sizePolicy)
        self.prefOutputBackground_CUSTOM.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefOutputBackground_CUSTOM.setFont(font)
        self.prefOutputBackground_CUSTOM.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefOutputBackground_CUSTOM.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:checked {\n"
"background-color: #BAB9BA;\n"
"}")
        self.prefOutputBackground_CUSTOM.setCheckable(True)
        self.prefOutputBackground_CUSTOM.setChecked(False)
        self.prefOutputBackground_CUSTOM.setAutoExclusive(True)
        self.prefOutputBackground_CUSTOM.setObjectName("prefOutputBackground_CUSTOM")
        self.prefOutputBackground.addWidget(self.prefOutputBackground_CUSTOM)
        self.prefOutputBackground.setStretch(0, 2)
        self.prefOutputBackground.setStretch(1, 2)
        self.prefOutputBackground.setStretch(2, 1)
        self.formGeneral.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prefOutputBackground_widget)
        self.prefStageBackground_widget = QtWidgets.QWidget(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageBackground_widget.sizePolicy().hasHeightForWidth())
        self.prefStageBackground_widget.setSizePolicy(sizePolicy)
        self.prefStageBackground_widget.setObjectName("prefStageBackground_widget")
        self.layoutWidget2 = QtWidgets.QWidget(self.prefStageBackground_widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 661, 55))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.prefStageBackground = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.prefStageBackground.setContentsMargins(0, 0, 0, 0)
        self.prefStageBackground.setSpacing(0)
        self.prefStageBackground.setObjectName("prefStageBackground")
        self.prefStageBackground_BLACK = QtWidgets.QPushButton(self.layoutWidget2)
        self.prefStageBackground_BLACK.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageBackground_BLACK.sizePolicy().hasHeightForWidth())
        self.prefStageBackground_BLACK.setSizePolicy(sizePolicy)
        self.prefStageBackground_BLACK.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefStageBackground_BLACK.setFont(font)
        self.prefStageBackground_BLACK.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageBackground_BLACK.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #000;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #BCBCBC;\n"
"}\n"
"")
        self.prefStageBackground_BLACK.setCheckable(True)
        self.prefStageBackground_BLACK.setChecked(False)
        self.prefStageBackground_BLACK.setAutoExclusive(True)
        self.prefStageBackground_BLACK.setObjectName("prefStageBackground_BLACK")
        self.prefStageBackground.addWidget(self.prefStageBackground_BLACK)
        self.prefStageBackground_WHITE = QtWidgets.QPushButton(self.layoutWidget2)
        self.prefStageBackground_WHITE.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageBackground_WHITE.sizePolicy().hasHeightForWidth())
        self.prefStageBackground_WHITE.setSizePolicy(sizePolicy)
        self.prefStageBackground_WHITE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefStageBackground_WHITE.setFont(font)
        self.prefStageBackground_WHITE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageBackground_WHITE.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: #fff;\n"
"color: black;\n"
"}\n"
"\n"
"QPushButton:hover:!checked {\n"
"background-color: #BCBCBC;\n"
"}\n"
"")
        self.prefStageBackground_WHITE.setCheckable(True)
        self.prefStageBackground_WHITE.setChecked(False)
        self.prefStageBackground_WHITE.setAutoExclusive(True)
        self.prefStageBackground_WHITE.setObjectName("prefStageBackground_WHITE")
        self.prefStageBackground.addWidget(self.prefStageBackground_WHITE)
        self.prefStageBackground_CUSTOM = QtWidgets.QPushButton(self.layoutWidget2)
        self.prefStageBackground_CUSTOM.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageBackground_CUSTOM.sizePolicy().hasHeightForWidth())
        self.prefStageBackground_CUSTOM.setSizePolicy(sizePolicy)
        self.prefStageBackground_CUSTOM.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prefStageBackground_CUSTOM.setFont(font)
        self.prefStageBackground_CUSTOM.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageBackground_CUSTOM.setStyleSheet("QPushButton {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:checked {\n"
"background-color: #BAB9BA;\n"
"}")
        self.prefStageBackground_CUSTOM.setCheckable(True)
        self.prefStageBackground_CUSTOM.setChecked(False)
        self.prefStageBackground_CUSTOM.setAutoExclusive(True)
        self.prefStageBackground_CUSTOM.setObjectName("prefStageBackground_CUSTOM")
        self.prefStageBackground.addWidget(self.prefStageBackground_CUSTOM)
        self.prefStageBackground.setStretch(0, 2)
        self.prefStageBackground.setStretch(1, 2)
        self.prefStageBackground.setStretch(2, 1)
        self.formGeneral.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prefStageBackground_widget)
        self.viewTabs.addWidget(self.viewGeneral)
        self.viewDisplay = QtWidgets.QWidget()
        self.viewDisplay.setStyleSheet("QComboBox {color: black}")
        self.viewDisplay.setObjectName("viewDisplay")
        self.formLayoutWidget = QtWidgets.QWidget(self.viewDisplay)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 901, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formDisplay = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formDisplay.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formDisplay.setContentsMargins(60, 30, 60, 0)
        self.formDisplay.setSpacing(10)
        self.formDisplay.setObjectName("formDisplay")
        self.prefOutputDisplayID_LABEL = QtWidgets.QLabel(self.formLayoutWidget)
        self.prefOutputDisplayID_LABEL.setEnabled(True)
        self.prefOutputDisplayID_LABEL.setMinimumSize(QtCore.QSize(0, 30))
        self.prefOutputDisplayID_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefOutputDisplayID_LABEL.setObjectName("prefOutputDisplayID_LABEL")
        self.formDisplay.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.prefOutputDisplayID_LABEL)
        self.prefOutputDisplayID = QtWidgets.QComboBox(self.formLayoutWidget)
        self.prefOutputDisplayID.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefOutputDisplayID.sizePolicy().hasHeightForWidth())
        self.prefOutputDisplayID.setSizePolicy(sizePolicy)
        self.prefOutputDisplayID.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefOutputDisplayID.setObjectName("prefOutputDisplayID")
        self.formDisplay.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.prefOutputDisplayID)
        self.prefStageDisplay_LABEL = QtWidgets.QLabel(self.formLayoutWidget)
        self.prefStageDisplay_LABEL.setEnabled(False)
        self.prefStageDisplay_LABEL.setMinimumSize(QtCore.QSize(0, 30))
        self.prefStageDisplay_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefStageDisplay_LABEL.setObjectName("prefStageDisplay_LABEL")
        self.formDisplay.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prefStageDisplay_LABEL)
        self.prefStageDisplayID_LABEL = QtWidgets.QLabel(self.formLayoutWidget)
        self.prefStageDisplayID_LABEL.setEnabled(False)
        self.prefStageDisplayID_LABEL.setMinimumSize(QtCore.QSize(0, 30))
        self.prefStageDisplayID_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefStageDisplayID_LABEL.setObjectName("prefStageDisplayID_LABEL")
        self.formDisplay.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.prefStageDisplayID_LABEL)
        self.prefStageDisplayID = QtWidgets.QComboBox(self.formLayoutWidget)
        self.prefStageDisplayID.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageDisplayID.sizePolicy().hasHeightForWidth())
        self.prefStageDisplayID.setSizePolicy(sizePolicy)
        self.prefStageDisplayID.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageDisplayID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.prefStageDisplayID.setObjectName("prefStageDisplayID")
        self.formDisplay.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prefStageDisplayID)
        self.prefBackgroundMedia_LABEL = QtWidgets.QLabel(self.formLayoutWidget)
        self.prefBackgroundMedia_LABEL.setMinimumSize(QtCore.QSize(0, 30))
        self.prefBackgroundMedia_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefBackgroundMedia_LABEL.setObjectName("prefBackgroundMedia_LABEL")
        self.formDisplay.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.prefBackgroundMedia_LABEL)
        self.prefBackgroundAudio_LABEL = QtWidgets.QLabel(self.formLayoutWidget)
        self.prefBackgroundAudio_LABEL.setEnabled(True)
        self.prefBackgroundAudio_LABEL.setMinimumSize(QtCore.QSize(0, 30))
        self.prefBackgroundAudio_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefBackgroundAudio_LABEL.setObjectName("prefBackgroundAudio_LABEL")
        self.formDisplay.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.prefBackgroundAudio_LABEL)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formDisplay.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.prefStageDisplay_widget = QtWidgets.QWidget(self.formLayoutWidget)
        self.prefStageDisplay_widget.setObjectName("prefStageDisplay_widget")
        self.layoutWidget3 = QtWidgets.QWidget(self.prefStageDisplay_widget)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 667, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.prefStageDisplay = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.prefStageDisplay.setContentsMargins(0, 0, 0, 0)
        self.prefStageDisplay.setSpacing(0)
        self.prefStageDisplay.setObjectName("prefStageDisplay")
        self.prefStageDisplay_OFF = QtWidgets.QPushButton(self.layoutWidget3)
        self.prefStageDisplay_OFF.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageDisplay_OFF.sizePolicy().hasHeightForWidth())
        self.prefStageDisplay_OFF.setSizePolicy(sizePolicy)
        self.prefStageDisplay_OFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageDisplay_OFF.setCheckable(True)
        self.prefStageDisplay_OFF.setChecked(True)
        self.prefStageDisplay_OFF.setAutoExclusive(True)
        self.prefStageDisplay_OFF.setObjectName("prefStageDisplay_OFF")
        self.prefStageDisplay.addWidget(self.prefStageDisplay_OFF)
        self.prefStageDisplay_ON = QtWidgets.QPushButton(self.layoutWidget3)
        self.prefStageDisplay_ON.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefStageDisplay_ON.sizePolicy().hasHeightForWidth())
        self.prefStageDisplay_ON.setSizePolicy(sizePolicy)
        self.prefStageDisplay_ON.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefStageDisplay_ON.setCheckable(True)
        self.prefStageDisplay_ON.setChecked(False)
        self.prefStageDisplay_ON.setAutoExclusive(True)
        self.prefStageDisplay_ON.setObjectName("prefStageDisplay_ON")
        self.prefStageDisplay.addWidget(self.prefStageDisplay_ON)
        self.formDisplay.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prefStageDisplay_widget)
        self.prefBackgroundMedia_widget = QtWidgets.QWidget(self.formLayoutWidget)
        self.prefBackgroundMedia_widget.setObjectName("prefBackgroundMedia_widget")
        self.layoutWidget4 = QtWidgets.QWidget(self.prefBackgroundMedia_widget)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 667, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.prefBackgroundMedia = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.prefBackgroundMedia.setContentsMargins(0, 0, 0, 0)
        self.prefBackgroundMedia.setSpacing(0)
        self.prefBackgroundMedia.setObjectName("prefBackgroundMedia")
        self.prefBackgroundMedia_OFF = QtWidgets.QPushButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefBackgroundMedia_OFF.sizePolicy().hasHeightForWidth())
        self.prefBackgroundMedia_OFF.setSizePolicy(sizePolicy)
        self.prefBackgroundMedia_OFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefBackgroundMedia_OFF.setCheckable(True)
        self.prefBackgroundMedia_OFF.setChecked(True)
        self.prefBackgroundMedia_OFF.setAutoExclusive(True)
        self.prefBackgroundMedia_OFF.setObjectName("prefBackgroundMedia_OFF")
        self.prefBackgroundMedia.addWidget(self.prefBackgroundMedia_OFF)
        self.prefBackgroundMedia_ON = QtWidgets.QPushButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefBackgroundMedia_ON.sizePolicy().hasHeightForWidth())
        self.prefBackgroundMedia_ON.setSizePolicy(sizePolicy)
        self.prefBackgroundMedia_ON.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefBackgroundMedia_ON.setCheckable(True)
        self.prefBackgroundMedia_ON.setChecked(False)
        self.prefBackgroundMedia_ON.setAutoExclusive(True)
        self.prefBackgroundMedia_ON.setObjectName("prefBackgroundMedia_ON")
        self.prefBackgroundMedia.addWidget(self.prefBackgroundMedia_ON)
        self.formDisplay.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.prefBackgroundMedia_widget)
        self.prefBackgroundAudio_widget = QtWidgets.QWidget(self.formLayoutWidget)
        self.prefBackgroundAudio_widget.setObjectName("prefBackgroundAudio_widget")
        self.layoutWidget5 = QtWidgets.QWidget(self.prefBackgroundAudio_widget)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 667, 30))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.prefBackgroundAudio = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.prefBackgroundAudio.setContentsMargins(0, 0, 0, 0)
        self.prefBackgroundAudio.setSpacing(0)
        self.prefBackgroundAudio.setObjectName("prefBackgroundAudio")
        self.prefBackgroundAudio_OFF = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefBackgroundAudio_OFF.sizePolicy().hasHeightForWidth())
        self.prefBackgroundAudio_OFF.setSizePolicy(sizePolicy)
        self.prefBackgroundAudio_OFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefBackgroundAudio_OFF.setCheckable(True)
        self.prefBackgroundAudio_OFF.setChecked(True)
        self.prefBackgroundAudio_OFF.setAutoExclusive(True)
        self.prefBackgroundAudio_OFF.setObjectName("prefBackgroundAudio_OFF")
        self.prefBackgroundAudio.addWidget(self.prefBackgroundAudio_OFF)
        self.prefBackgroundAudio_ON = QtWidgets.QPushButton(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefBackgroundAudio_ON.sizePolicy().hasHeightForWidth())
        self.prefBackgroundAudio_ON.setSizePolicy(sizePolicy)
        self.prefBackgroundAudio_ON.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefBackgroundAudio_ON.setCheckable(True)
        self.prefBackgroundAudio_ON.setChecked(False)
        self.prefBackgroundAudio_ON.setAutoExclusive(True)
        self.prefBackgroundAudio_ON.setObjectName("prefBackgroundAudio_ON")
        self.prefBackgroundAudio.addWidget(self.prefBackgroundAudio_ON)
        self.formDisplay.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.prefBackgroundAudio_widget)
        self.btnSystemSettings = QtWidgets.QPushButton(self.viewDisplay)
        self.btnSystemSettings.setEnabled(True)
        self.btnSystemSettings.setGeometry(QtCore.QRect(50, 290, 781, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSystemSettings.sizePolicy().hasHeightForWidth())
        self.btnSystemSettings.setSizePolicy(sizePolicy)
        self.btnSystemSettings.setMinimumSize(QtCore.QSize(0, 55))
        self.btnSystemSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSystemSettings.setFont(font)
        self.btnSystemSettings.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSystemSettings.setStyleSheet("QPushButton {\n"
"background-color: #BAB9BA;\n"
"border: none;\n"
"color: white;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #8CC5FF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #509DF3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"")
        self.btnSystemSettings.setObjectName("btnSystemSettings")
        self.viewTabs.addWidget(self.viewDisplay)
        self.viewRemote = QtWidgets.QWidget()
        self.viewRemote.setEnabled(False)
        self.viewRemote.setObjectName("viewRemote")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.viewRemote)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(640, 100, 152, 27))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.prefRemoteAPI = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.prefRemoteAPI.setContentsMargins(0, 0, 0, 0)
        self.prefRemoteAPI.setSpacing(0)
        self.prefRemoteAPI.setObjectName("prefRemoteAPI")
        self.prefRemoteAPI_OFF = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefRemoteAPI_OFF.sizePolicy().hasHeightForWidth())
        self.prefRemoteAPI_OFF.setSizePolicy(sizePolicy)
        self.prefRemoteAPI_OFF.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefRemoteAPI_OFF.setCheckable(True)
        self.prefRemoteAPI_OFF.setChecked(True)
        self.prefRemoteAPI_OFF.setAutoExclusive(True)
        self.prefRemoteAPI_OFF.setObjectName("prefRemoteAPI_OFF")
        self.prefRemoteAPI.addWidget(self.prefRemoteAPI_OFF)
        self.prefRemoteAPI_ON = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefRemoteAPI_ON.sizePolicy().hasHeightForWidth())
        self.prefRemoteAPI_ON.setSizePolicy(sizePolicy)
        self.prefRemoteAPI_ON.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prefRemoteAPI_ON.setCheckable(True)
        self.prefRemoteAPI_ON.setChecked(False)
        self.prefRemoteAPI_ON.setAutoExclusive(True)
        self.prefRemoteAPI_ON.setObjectName("prefRemoteAPI_ON")
        self.prefRemoteAPI.addWidget(self.prefRemoteAPI_ON)
        self.prefTEMP_LABEL = QtWidgets.QLabel(self.viewRemote)
        self.prefTEMP_LABEL.setEnabled(False)
        self.prefTEMP_LABEL.setGeometry(QtCore.QRect(520, 100, 110, 25))
        self.prefTEMP_LABEL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prefTEMP_LABEL.setObjectName("prefTEMP_LABEL")
        self.label = QtWidgets.QLabel(self.viewRemote)
        self.label.setGeometry(QtCore.QRect(580, 140, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.viewRemote)
        self.lineEdit.setGeometry(QtCore.QRect(640, 140, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.viewRemote)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 180, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.viewRemote)
        self.label_6.setGeometry(QtCore.QRect(580, 180, 47, 13))
        self.label_6.setObjectName("label_6")
        self.viewTabs.addWidget(self.viewRemote)
        self.viewAbout = QtWidgets.QWidget()
        self.viewAbout.setObjectName("viewAbout")
        self.aboutInfo = QtWidgets.QLabel(self.viewAbout)
        self.aboutInfo.setGeometry(QtCore.QRect(10, 150, 861, 151))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.aboutInfo.setFont(font)
        self.aboutInfo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.aboutInfo.setObjectName("aboutInfo")
        self.aboutVersions = QtWidgets.QLabel(self.viewAbout)
        self.aboutVersions.setGeometry(QtCore.QRect(590, 470, 261, 201))
        self.aboutVersions.setText("")
        self.aboutVersions.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.aboutVersions.setObjectName("aboutVersions")
        self.aboutDescription = QtWidgets.QLabel(self.viewAbout)
        self.aboutDescription.setGeometry(QtCore.QRect(0, 350, 881, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.aboutDescription.setFont(font)
        self.aboutDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutDescription.setObjectName("aboutDescription")
        self.viewTabs.addWidget(self.viewAbout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.theming)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 901, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.viewTabsHeader = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.viewTabsHeader.setContentsMargins(0, 0, 0, 0)
        self.viewTabsHeader.setSpacing(0)
        self.viewTabsHeader.setObjectName("viewTabsHeader")
        self.viewTabs_General = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTabs_General.sizePolicy().hasHeightForWidth())
        self.viewTabs_General.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.viewTabs_General.setFont(font)
        self.viewTabs_General.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewTabs_General.setCheckable(True)
        self.viewTabs_General.setAutoExclusive(True)
        self.viewTabs_General.setObjectName("viewTabs_General")
        self.viewTabsHeader.addWidget(self.viewTabs_General)
        self.viewTabs_Display = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTabs_Display.sizePolicy().hasHeightForWidth())
        self.viewTabs_Display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.viewTabs_Display.setFont(font)
        self.viewTabs_Display.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewTabs_Display.setCheckable(True)
        self.viewTabs_Display.setAutoExclusive(True)
        self.viewTabs_Display.setObjectName("viewTabs_Display")
        self.viewTabsHeader.addWidget(self.viewTabs_Display)
        self.viewTabs_Remote = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.viewTabs_Remote.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTabs_Remote.sizePolicy().hasHeightForWidth())
        self.viewTabs_Remote.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.viewTabs_Remote.setFont(font)
        self.viewTabs_Remote.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewTabs_Remote.setCheckable(True)
        self.viewTabs_Remote.setAutoExclusive(True)
        self.viewTabs_Remote.setObjectName("viewTabs_Remote")
        self.viewTabsHeader.addWidget(self.viewTabs_Remote)
        self.viewTabs_About = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTabs_About.sizePolicy().hasHeightForWidth())
        self.viewTabs_About.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.viewTabs_About.setFont(font)
        self.viewTabs_About.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewTabs_About.setCheckable(True)
        self.viewTabs_About.setAutoExclusive(True)
        self.viewTabs_About.setObjectName("viewTabs_About")
        self.viewTabsHeader.addWidget(self.viewTabs_About)
        self.Header = QtWidgets.QLabel(self.theming)
        self.Header.setGeometry(QtCore.QRect(0, 0, 900, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Header.setFont(font)
        self.Header.setText("Settings")
        self.Header.setTextFormat(QtCore.Qt.AutoText)
        self.Header.setScaledContents(False)
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")
        self.btnSave = QtWidgets.QPushButton(self.theming)
        self.btnSave.setEnabled(False)
        self.btnSave.setGeometry(QtCore.QRect(20, 850, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSave.setFont(font)
        self.btnSave.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSave.setStyleSheet("QPushButton {\n"
"background-color: #BAB9BA;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"background-color: #8CC5FF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #509DF3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: #D8D8D8;\n"
"}\n"
"\n"
"")
        self.btnSave.setObjectName("btnSave")
        self.viewTabs.raise_()
        self.horizontalLayoutWidget.raise_()
        self.Header.raise_()
        self.btnSave.raise_()
        self.btnBack.raise_()

        self.retranslateUi(Settings)
        self.viewTabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.btnBack.setText(_translate("Settings", "← Back"))
        self.prefTheme_LABEL.setText(_translate("Settings", "Theme"))
        self.prefStageBackground_LABEL.setText(_translate("Settings", "Stage Display Background"))
        self.prefOutputBackground_LABEL.setText(_translate("Settings", "Output Display Background"))
        self.prefTheme_BLUE.setText(_translate("Settings", "Blue"))
        self.prefTheme_RED.setText(_translate("Settings", "Red"))
        self.prefTheme_GREY.setText(_translate("Settings", "Grey"))
        self.prefTheme_DARK.setText(_translate("Settings", "Dark"))
        self.prefTheme_CUSTOM.setText(_translate("Settings", "..."))
        self.prefOutputBackground_BLACK.setText(_translate("Settings", "Black"))
        self.prefOutputBackground_WHITE.setText(_translate("Settings", "White"))
        self.prefOutputBackground_CUSTOM.setText(_translate("Settings", "..."))
        self.prefStageBackground_BLACK.setText(_translate("Settings", "Black"))
        self.prefStageBackground_WHITE.setText(_translate("Settings", "White"))
        self.prefStageBackground_CUSTOM.setText(_translate("Settings", "..."))
        self.prefOutputDisplayID_LABEL.setText(_translate("Settings", "Output Monitor"))
        self.prefStageDisplay_LABEL.setText(_translate("Settings", "Enable Stage Display"))
        self.prefStageDisplayID_LABEL.setText(_translate("Settings", "Stage Display Monitor"))
        self.prefBackgroundMedia_LABEL.setText(_translate("Settings", "Pause media when hidden"))
        self.prefBackgroundAudio_LABEL.setText(_translate("Settings", "Mute audio when hidden"))
        self.prefStageDisplay_OFF.setText(_translate("Settings", "OFF"))
        self.prefStageDisplay_ON.setText(_translate("Settings", "ON"))
        self.prefBackgroundMedia_OFF.setText(_translate("Settings", "OFF"))
        self.prefBackgroundMedia_ON.setText(_translate("Settings", "ON"))
        self.prefBackgroundAudio_OFF.setText(_translate("Settings", "OFF"))
        self.prefBackgroundAudio_ON.setText(_translate("Settings", "ON"))
        self.btnSystemSettings.setText(_translate("Settings", "System Display Settings"))
        self.prefRemoteAPI_OFF.setText(_translate("Settings", "OFF"))
        self.prefRemoteAPI_ON.setText(_translate("Settings", "ON"))
        self.prefTEMP_LABEL.setText(_translate("Settings", "Enable API _TEMP_"))
        self.label.setText(_translate("Settings", "API IP"))
        self.label_6.setText(_translate("Settings", "API Port"))
        self.aboutInfo.setText(_translate("Settings", "OnCue Projector\n"
"\n"
"Author: Andrew Wong"))
        self.aboutDescription.setText(_translate("Settings", "OnCue Projector is an easy to use multimedia presentation wrapper to facilitate the seamless playback of sequential content"))
        self.viewTabs_General.setText(_translate("Settings", "General"))
        self.viewTabs_Display.setText(_translate("Settings", "Display"))
        self.viewTabs_Remote.setText(_translate("Settings", "Remote"))
        self.viewTabs_About.setText(_translate("Settings", "About"))
        self.btnSave.setText(_translate("Settings", "Save"))

