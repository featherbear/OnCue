# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OnCue(object):
    def setupUi(self, OnCue):
        OnCue.setObjectName("OnCue")
        OnCue.setEnabled(True)
        OnCue.resize(900, 900)
        OnCue.setMinimumSize(QtCore.QSize(900, 900))
        OnCue.setMaximumSize(QtCore.QSize(900, 900))
        OnCue.setFocusPolicy(QtCore.Qt.NoFocus)
        OnCue.setStyleSheet("QWidget {\n"
"text-align: center;\n"
"color: white;\n"
"border: none;\n"
"text-decoration: none;\n"
"}")
        self.theming = QtWidgets.QFrame(OnCue)
        self.theming.setGeometry(QtCore.QRect(0, 0, 900, 900))
        self.theming.setStyleSheet("QLabel[objectName=\"Header\"] {background: #509DF3;}\n"
"QPushButton {background-color: #BAB9BA;}\n"
"QPushButton:checked {background-color: #509DF3;}\n"
"QPushButton:hover:!checked {background-color: #8CC5FF;}\n"
"QProgressBar:chunk {background-color: #509DF3;}\n"
"QLabel[objectName=\"mediaProgressSeek\"] {border-left-color: #8CC5FF;}")
        self.theming.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.theming.setFrameShadow(QtWidgets.QFrame.Plain)
        self.theming.setObjectName("theming")
        self.btnSettings = QtWidgets.QPushButton(self.theming)
        self.btnSettings.setGeometry(QtCore.QRect(0, 0, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSettings.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnSettings.setStyleSheet("QPushButton {background-color: #BAB9BA;}\n"
"QPushButton:hover {background-color: #A0A0A0;}\n"
"")
        self.btnSettings.setObjectName("btnSettings")
        self.listItemsPrimary = QtWidgets.QListWidget(self.theming)
        self.listItemsPrimary.setGeometry(QtCore.QRect(0, 80, 300, 740))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listItemsPrimary.setFont(font)
        self.listItemsPrimary.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listItemsPrimary.setAcceptDrops(True)
        self.listItemsPrimary.setStyleSheet("QScrollBar:vertical {              \n"
"        background: #EAEAEA;\n"
"        width: 8px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background: #D8D8D8;\n"
"        min-height: 0px;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QScrollBar::handle:vertical:hover {\n"
"        background: #888;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"QListView::item {\n"
"    color: black;\n"
"    max-height: 50px;\n"
"}\n"
"QListView::item:alternate {\n"
"    _background: grey;\n"
"}\n"
"\n"
"QListView::item:selectedx {\n"
"    border: blue;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: #B3E4F2;\n"
"}\n"
"\n"
"QListView::item:hover:!selected {\n"
"    background: #DEF1F7;\n"
"}")
        self.listItemsPrimary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listItemsPrimary.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listItemsPrimary.setProperty("showDropIndicator", True)
        self.listItemsPrimary.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listItemsPrimary.setResizeMode(QtWidgets.QListView.Fixed)
        self.listItemsPrimary.setObjectName("listItemsPrimary")
        self.Header = QtWidgets.QLabel(self.theming)
        self.Header.setGeometry(QtCore.QRect(0, 0, 900, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Header.setFont(font)
        self.Header.setText("OnCue")
        self.Header.setTextFormat(QtCore.Qt.AutoText)
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")
        self.btnExit = QtWidgets.QPushButton(self.theming)
        self.btnExit.setGeometry(QtCore.QRect(825, 0, 75, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnExit.setFont(font)
        self.btnExit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnExit.setStyleSheet("QPushButton {background-color: #BAB9BA;}\n"
"QPushButton:hover {background-color: #FF4136;}")
        self.btnExit.setObjectName("btnExit")
        self.btnOutput_wrap = QtWidgets.QWidget(self.theming)
        self.btnOutput_wrap.setGeometry(QtCore.QRect(0, 820, 901, 80))
        self.btnOutput_wrap.setStyleSheet("QPushButton:disabled {\n"
"background-color: #727272;\n"
"color: #A7A7A7;\n"
"}")
        self.btnOutput_wrap.setObjectName("btnOutput_wrap")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.btnOutput_wrap)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.btnOutput = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.btnOutput.setContentsMargins(0, 0, 0, 0)
        self.btnOutput.setSpacing(0)
        self.btnOutput.setObjectName("btnOutput")
        self.btnOutputContent = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnOutputContent.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOutputContent.sizePolicy().hasHeightForWidth())
        self.btnOutputContent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnOutputContent.setFont(font)
        self.btnOutputContent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnOutputContent.setCheckable(True)
        self.btnOutputContent.setChecked(True)
        self.btnOutputContent.setAutoExclusive(True)
        self.btnOutputContent.setObjectName("btnOutputContent")
        self.btnOutput.addWidget(self.btnOutputContent)
        self.btnOutputClear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnOutputClear.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOutputClear.sizePolicy().hasHeightForWidth())
        self.btnOutputClear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnOutputClear.setFont(font)
        self.btnOutputClear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnOutputClear.setCheckable(True)
        self.btnOutputClear.setChecked(False)
        self.btnOutputClear.setAutoExclusive(True)
        self.btnOutputClear.setObjectName("btnOutputClear")
        self.btnOutput.addWidget(self.btnOutputClear)
        self.btnOutputDesktop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOutputDesktop.sizePolicy().hasHeightForWidth())
        self.btnOutputDesktop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnOutputDesktop.setFont(font)
        self.btnOutputDesktop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnOutputDesktop.setCheckable(True)
        self.btnOutputDesktop.setAutoExclusive(True)
        self.btnOutputDesktop.setObjectName("btnOutputDesktop")
        self.btnOutput.addWidget(self.btnOutputDesktop)
        self.mediaProgress = QtWidgets.QWidget(self.theming)
        self.mediaProgress.setGeometry(QtCore.QRect(660, 800, 240, 21))
        self.mediaProgress.setStyleSheet("QLabel {border-left-style: solid}")
        self.mediaProgress.setObjectName("mediaProgress")
        self.contentControls = QtWidgets.QStackedWidget(self.theming)
        self.contentControls.setGeometry(QtCore.QRect(300, 118, 260, 703))
        self.contentControls.setObjectName("contentControls")
        self.empty = QtWidgets.QWidget()
        self.empty.setObjectName("empty")
        self.contentControls.addWidget(self.empty)
        self.powerpoint = QtWidgets.QWidget()
        self.powerpoint.setObjectName("powerpoint")
        self.powerpointSlides = QtWidgets.QListWidget(self.powerpoint)
        self.powerpointSlides.setGeometry(QtCore.QRect(0, 0, 260, 651))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.powerpointSlides.setFont(font)
        self.powerpointSlides.setFocusPolicy(QtCore.Qt.NoFocus)
        self.powerpointSlides.setAcceptDrops(True)
        self.powerpointSlides.setStyleSheet("QScrollBar:vertical {              \n"
"        background: #EAEAEA;\n"
"        width: 8px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background: #D8D8D8;\n"
"        min-height: 0px;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QScrollBar::handle:vertical:hover {\n"
"        background: #888;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"QListView::item {\n"
"    color: black;\n"
"}\n"
"QListView::item:alternate {\n"
"    _background: grey;\n"
"}\n"
"\n"
"QListView::item:selectedx {\n"
"    border: blue;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: #B3E4F2;\n"
"}\n"
"\n"
"QListView::item:hover:!selected {\n"
"    background: #DEF1F7;\n"
"}")
        self.powerpointSlides.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.powerpointSlides.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.powerpointSlides.setDragEnabled(False)
        self.powerpointSlides.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.powerpointSlides.setAlternatingRowColors(False)
        self.powerpointSlides.setIconSize(QtCore.QSize(260, 117))
        self.powerpointSlides.setObjectName("powerpointSlides")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.powerpoint)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 650, 261, 53))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.powerpointControls = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.powerpointControls.setContentsMargins(0, 0, 0, 0)
        self.powerpointControls.setSpacing(0)
        self.powerpointControls.setObjectName("powerpointControls")
        self.powerpointControls_PREVIOUS = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerpointControls_PREVIOUS.sizePolicy().hasHeightForWidth())
        self.powerpointControls_PREVIOUS.setSizePolicy(sizePolicy)
        self.powerpointControls_PREVIOUS.setObjectName("powerpointControls_PREVIOUS")
        self.powerpointControls.addWidget(self.powerpointControls_PREVIOUS)
        self.powerpointControls_NEXT = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerpointControls_NEXT.sizePolicy().hasHeightForWidth())
        self.powerpointControls_NEXT.setSizePolicy(sizePolicy)
        self.powerpointControls_NEXT.setObjectName("powerpointControls_NEXT")
        self.powerpointControls.addWidget(self.powerpointControls_NEXT)
        self.contentControls.addWidget(self.powerpoint)
        self.media = QtWidgets.QWidget()
        self.media.setStyleSheet("QLabel {border-left-style: solid;}")
        self.media.setObjectName("media")
        self.mediaProgressSeek = QtWidgets.QLabel(self.media)
        self.mediaProgressSeek.setGeometry(QtCore.QRect(10, 500, 240, 31))
        self.mediaProgressSeek.setStyleSheet("")
        self.mediaProgressSeek.setText("")
        self.mediaProgressSeek.setObjectName("mediaProgressSeek")
        self.mediaProgressBar = QtWidgets.QProgressBar(self.media)
        self.mediaProgressBar.setGeometry(QtCore.QRect(10, 500, 240, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mediaProgressBar.setFont(font)
        self.mediaProgressBar.setStyleSheet("")
        self.mediaProgressBar.setMinimum(0)
        self.mediaProgressBar.setMaximum(1000)
        self.mediaProgressBar.setProperty("value", 0)
        self.mediaProgressBar.setTextVisible(False)
        self.mediaProgressBar.setObjectName("mediaProgressBar")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.media)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 550, 241, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.mediaControls = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.mediaControls.setContentsMargins(0, 0, 0, 0)
        self.mediaControls.setSpacing(0)
        self.mediaControls.setObjectName("mediaControls")
        self.mediaControls_PAUSE = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mediaControls_PAUSE.sizePolicy().hasHeightForWidth())
        self.mediaControls_PAUSE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mediaControls_PAUSE.setFont(font)
        self.mediaControls_PAUSE.setCheckable(True)
        self.mediaControls_PAUSE.setAutoExclusive(True)
        self.mediaControls_PAUSE.setObjectName("mediaControls_PAUSE")
        self.mediaControls.addWidget(self.mediaControls_PAUSE)
        self.mediaControls_PLAY = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mediaControls_PLAY.sizePolicy().hasHeightForWidth())
        self.mediaControls_PLAY.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mediaControls_PLAY.setFont(font)
        self.mediaControls_PLAY.setCheckable(True)
        self.mediaControls_PLAY.setAutoExclusive(True)
        self.mediaControls_PLAY.setObjectName("mediaControls_PLAY")
        self.mediaControls.addWidget(self.mediaControls_PLAY)
        self.mediaControls_MUTE = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mediaControls_MUTE.sizePolicy().hasHeightForWidth())
        self.mediaControls_MUTE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mediaControls_MUTE.setFont(font)
        self.mediaControls_MUTE.setCheckable(True)
        self.mediaControls_MUTE.setAutoExclusive(False)
        self.mediaControls_MUTE.setObjectName("mediaControls_MUTE")
        self.mediaControls.addWidget(self.mediaControls_MUTE)
        self.mediaProgressBar.raise_()
        self.mediaProgressSeek.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.contentControls.addWidget(self.media)
        self.views = QtWidgets.QWidget(self.theming)
        self.views.setEnabled(False)
        self.views.setGeometry(QtCore.QRect(520, 80, 381, 741))
        self.views.setStyleSheet("color: black;")
        self.views.setObjectName("views")
        self.labelOutput = QtWidgets.QLabel(self.views)
        self.labelOutput.setEnabled(False)
        self.labelOutput.setGeometry(QtCore.QRect(180, 660, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelOutput.setFont(font)
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.viewOutput = QtWidgets.QOpenGLWidget(self.views)
        self.viewOutput.setEnabled(False)
        self.viewOutput.setGeometry(QtCore.QRect(70, 400, 281, 245))
        self.viewOutput.setObjectName("viewOutput")
        self.viewPreview = QtWidgets.QOpenGLWidget(self.views)
        self.viewPreview.setEnabled(False)
        self.viewPreview.setGeometry(QtCore.QRect(70, 70, 281, 246))
        self.viewPreview.setObjectName("viewPreview")
        self.labelPreview = QtWidgets.QLabel(self.views)
        self.labelPreview.setEnabled(False)
        self.labelPreview.setGeometry(QtCore.QRect(170, 330, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPreview.setFont(font)
        self.labelPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPreview.setObjectName("labelPreview")
        self.label = QtWidgets.QLabel(self.views)
        self.label.setGeometry(QtCore.QRect(70, 130, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.views)
        self.label_2.setGeometry(QtCore.QRect(70, 470, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnClear = QtWidgets.QPushButton(self.theming)
        self.btnClear.setGeometry(QtCore.QRect(300, 80, 601, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnClear.setFont(font)
        self.btnClear.setStyleSheet("")
        self.btnClear.setObjectName("btnClear")
        self.views.raise_()
        self.listItemsPrimary.raise_()
        self.Header.raise_()
        self.btnExit.raise_()
        self.btnSettings.raise_()
        self.btnOutput_wrap.raise_()
        self.mediaProgress.raise_()
        self.contentControls.raise_()
        self.btnClear.raise_()

        self.retranslateUi(OnCue)
        self.contentControls.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(OnCue)
        OnCue.setTabOrder(self.btnSettings, self.btnExit)

    def retranslateUi(self, OnCue):
        _translate = QtCore.QCoreApplication.translate
        OnCue.setWindowTitle(_translate("OnCue", "OnCue"))
        self.btnSettings.setText(_translate("OnCue", "Settings"))
        self.btnExit.setText(_translate("OnCue", "Exit"))
        self.btnOutputContent.setText(_translate("OnCue", "Show Content"))
        self.btnOutputClear.setText(_translate("OnCue", "Hide Content"))
        self.btnOutputDesktop.setText(_translate("OnCue", "Show Desktop"))
        self.powerpointControls_PREVIOUS.setText(_translate("OnCue", "<<"))
        self.powerpointControls_NEXT.setText(_translate("OnCue", ">>"))
        self.mediaControls_PAUSE.setText(_translate("OnCue", "PAUSE"))
        self.mediaControls_PLAY.setText(_translate("OnCue", "PLAY"))
        self.mediaControls_MUTE.setText(_translate("OnCue", "MUTE"))
        self.labelOutput.setText(_translate("OnCue", "Output"))
        self.labelPreview.setText(_translate("OnCue", "Preview"))
        self.label.setText(_translate("OnCue", "not implemented"))
        self.label_2.setText(_translate("OnCue", "not implemented"))
        self.btnClear.setText(_translate("OnCue", "Clear Content"))

