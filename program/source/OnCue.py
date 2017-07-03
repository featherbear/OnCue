# -*- coding: utf-8 -*-

# Import modules
import glob
import os
import platform
import re
import sys
import tempfile
import win32api
import winreg

import win32com.client
from PyQt5 import QtCore, QtGui, QtWidgets

# Import the rest of the OnCue files
import OnCue

# Expose modules and functions to global scope
Vlc = OnCue.lib.vlc
vlc = Vlc.Instance()
colorPicker = lambda o: OnCue.forms.colorPicker.colorPicker(o, theme=states["interface"]["theme"]).exec_()
dprint = OnCue.lib.utils.dprint

selector = None


class Application(QtWidgets.QMainWindow):
    """
    Container class
    """

    def __init__(self):
        """
        Set up the interface
        """
        super(Application, self).__init__()
        global selector
        self.setWindowTitle("OnCue")
        self.setWindowIcon(QtGui.QIcon("OnCue.ico"))
        self.resize(900, 900)
        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        selector = QtWidgets.QStackedWidget()
        self.setCentralWidget(selector)
        states["interface"]["ui"] = [MAIN(), PREFERENCES()]
        [selector.addWidget(ui) for ui in states["interface"]["ui"]]


class MAIN(QtWidgets.QWidget, OnCue.forms_gen.main.Ui_OnCue):
    """
    Main Interface
    """

    # TODO not implemented
    # def seekMouse(self, e):
    #     self.mediaProgressSeek.setStyleSheet(
    #         "border-left-width: %spx;" % str(e.x() if isinstance(e, QtGui.QMouseEvent) else 0))

    def __init__(self):
        """
        Initialise class
        """
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        output.PPTevents.updateSlide = self.powerpointSlides.setCurrentRow
        self.contentControls.setCurrentIndex(0)

        # TODO not implemented
        """ 
        self.mediaProgressSeek.setMouseTracking(True)
        self.mediaProgressSeek.leaveEvent=self.seekMouse
        self.mediaProgressSeek.mouseMoveEvent=self.seekMouse
        self.mediaProgressSeek.mouseReleaseEvent=lambda e: output.seek(e.x()/self.mediaProgressSeek.width())
        """

        # Update video scrubber position
        class ProgressBarUpdater(QtCore.QThread):
            tick = QtCore.pyqtSignal(int)

            def run(self):
                while True:
                    self.sleep(1)
                    self.tick.emit(OnCue.lib.utils.confine(int(output.VLCposition() * 1000), 0, 1000))

        self.mediaProgressBarThread = ProgressBarUpdater()
        self.mediaProgressBarThread.tick.connect(
            lambda value: self.mediaProgressBar.setValue(value) or self.mediaProgressBar.repaint())

    def validateClick(self, pos, obj, callback):
        validation = bool(obj.itemAt(pos if isinstance(pos, QtCore.QPoint) else pos.pos()))
        callback() if validation else False

    def playItem(self):
        """
        Plays the selected item
        """
        data = self.listItemsPrimary.currentItem().data(256)
        output.load(data)

        if data["type"] == "media":
            # Plays video
            self.mediaProgressBarThread.start()
            self.mediaProgressBarThread.setPriority(QtCore.QThread.TimeCriticalPriority)
            self.mediaControls_PLAY.click()
            self.contentControls.setCurrentIndex(2)

        elif data["type"] == "powerpoint":
            # Clear existing content in the slide preview list
            self.powerpointSlides.clear()

            # Connect to PowerPoint COM
            PPTApplication = win32com.client.Dispatch("PowerPoint.Application")
            Presentation = PPTApplication.Presentations.Open(data["path"].replace("/", "\\"),
                                                             WithWindow=False)
            # Create slide previews
            temp = tempfile.TemporaryDirectory().name
            Presentation.Export(temp, "png")
            i = 1
            for file in glob.iglob(temp + "\\*.PNG"):
                item = QtWidgets.QListWidgetItem()
                item.setIcon(QtGui.QIcon(file))
                item.setText(str(i))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                i += 1
                self.powerpointSlides.addItem(item)
            self.contentControls.setCurrentIndex(1)
        else:
            # 'unknown' case - Hide controls
            self.contentControls.setCurrentIndex(0)

    def createQListWidgetItem(self, data):
        """
        Creates a QListWidgetItem() instance given a file path 
        """
        item = QtWidgets.QListWidgetItem()
        path = data.toLocalFile()
        type = OnCue.lib.utils.identifyFileType(path)
        item.setText(data.fileName())
        item.setData(256, {
            'type': type,
            'path': path
        })
        if type == "media":
            item.setToolTip(OnCue.lib.utils.parseMedia(path))
        else:
            item.setToolTip("Path: " + path)
        return item

    def handleDropEvent(self, e):
        """
        Handle adding items into the playlist 
        """
        if e.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            return QtWidgets.QListWidget.dropEvent(self.listItemsPrimary, e)
        data = e.mimeData().urls()[0]
        if isinstance(data, QtCore.QUrl): self.listItemsPrimary.addItem(self.createQListWidgetItem(data=data))

    def setupUi(self, MAIN):
        """
        Register button functions 
        """
        super().setupUi(MAIN)

        self.btnClear.clicked.connect(lambda: output.clear() or self.contentControls.setCurrentIndex(0))
        self.btnSettings.clicked.connect(
            lambda: states["interface"]["ui"][1].updateSettingInterface() or selector.setCurrentIndex(1))
        self.btnExit.clicked.connect(lambda: dprint("Quitting") or output.PPTclose() or sys.exit(0))

        # Output controls
        [self.btnOutput.itemAt(button).widget().setStyleSheet("") for button in range(self.btnOutput.count())]
        if len(states["screens"]) == 1:
            dprint("Output disabled, disabling display buttons")
            self.btnOutput_wrap.setEnabled(False)
        else:
            self.btnOutputClear.clicked.connect(output.contentHide)
            self.btnOutputContent.clicked.connect(output.contentShow)
            self.btnOutputDesktop.clicked.connect(output.contentDesktop)

        # Playlist right-click menu
        self.listItemsPrimary.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listItemsPrimary.dragEnterEvent = lambda e: (
            e.accept() if e.mimeData().hasUrls() or e.mimeData().hasFormat(
                'application/x-qabstractitemmodeldatalist') else e.ignore())
        self.listItemsPrimary.dropEvent = self.handleDropEvent
        self.listItemsPrimary.customContextMenuRequested.connect(
            lambda _: self.validateClick(_, self.listItemsPrimary, lambda: self.contextMenu.exec_()))

        # Playlist doubleclick
        self.listItemsPrimary.mouseDoubleClickEvent = lambda _: self.validateClick(_, self.listItemsPrimary,
                                                                                   self.playItem)
        # Powerpoint doubleclick
        self.powerpointSlides.mouseDoubleClickEvent = lambda _: self.validateClick(_, self.powerpointSlides,
                                                                                   lambda: output.PPTslide(

                                                                                       self.powerpointSlides.currentRow() + 1))
        # Powerpoint controls
        self.powerpointControls_PREVIOUS.clicked.connect(output.PPTprevious)
        self.powerpointControls_NEXT.clicked.connect(output.PPTnext)

        # Media controls
        self.mediaControls_PAUSE.clicked.connect(output.VLCpause)
        self.mediaControls_PLAY.clicked.connect(output.VLCplay)
        self.mediaControls_MUTE.clicked.connect(lambda: output.VLCmute(self.mediaControls_MUTE.isChecked()))

        # Update interface theme
        inactive, checked, hover = states["interface"]["theme"]
        self.theming.setStyleSheet(
            "QLabel[objectName='Header'] {background: #%s} "
            "QPushButton {background-color: #%s} "
            "QPushButton:checked {background-color: #%s} "
            "QPushButton:hover:!checked {background-color: #%s}"
            "QProgressBar:chunk {background-color: #%s;}"
            "QLabel[objectName='mediaProgressSeek'] {border-left-color: #%s;}"
            % (checked, inactive, checked, hover, checked, hover))

        class CCMenu(QtWidgets.QMenu):
            """
            Right-click menu
            """
            def __init__(self, area, parent):
                """
                Menu entries 
                """
                super().__init__()
                self.area = area
                self.parent = parent
                self.add("Play", self.play)
                self.addSeparator()
                # self.add("Debug", self.debug)
                self.add("Remove", self.remove)

            def add(self, label: str, function):
                # helper function to create menu entries
                item = QtWidgets.QAction(label, self)
                item.triggered.connect(function)
                self.addAction(item)

            def exec_(self):
                self.item = self.area.currentItem()
                #
                # Open right-click menu where the cursor is
                super().exec(QtGui.QCursor.pos())

            def play(self):
                # Play item
                self.parent.playItem()

            def remove(self):
                # Remove item from playlist
                self.area.takeItem(self.area.currentRow())

        # Register right-click menu
        self.contextMenu = CCMenu(self.listItemsPrimary, self)

class PREFERENCES(QtWidgets.QWidget, OnCue.forms_gen.settings.Ui_Settings):
    """
    Preferences interface
    """
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.viewTabs_General.click()  # Set General tab (Index 0) as default

        # Populate monitor dropdowns
        displaysArray = ["%s. %s" % (str(i), states["screens"][i]['name']) for i in states["screens"]]
        self.prefOutputDisplayID.addItems(displaysArray)
        # self.prefStageDisplayID.addItems(displaysArray) # TODO not implemented

        # Set component version info
        self.aboutVersions.setText(
            "\n".join(["%s Version: %s" % (
                component, states["versions"][component] if states["versions"][component] else "n/a") for component in
                       states["versions"].keys()]))

        # Set custom and last states
        self.customtheme = states["interface"]["theme"]
        self.lastbutton = themes.index(states["interface"]["theme"]) if states["interface"][
                                                                            "theme"] in themes else self.prefTheme.count() - 1
        self.customoutputbackground = states["display"]["outputbackground"]
        self.lastoutputbackground = backgrounds.index(states["display"]["outputbackground"]) if states["display"][
                                                                                                    "outputbackground"] in backgrounds else self.prefOutputBackground.count() - 1
        # TODO not implemented
        # self.customstagebackground = states["display"]["stagebackground"]
        # self.laststagebackground = backgrounds.index(states["display"]["stagebackground"]) if states["display"][
        #                                                                                           "stagebackground"] in backgrounds else self.prefStageBackground.count() - 1

        self.updateSettingInterface()

    def setupUi(self, SettingsWindow):
        """
        Connect buttons to functions 
        """
        super().setupUi(SettingsWindow)
        [self.viewTabsHeader.itemAt(button).widget().clicked.connect(self.handleTabSwitch) for button in
         range(self.viewTabsHeader.count())]
        self.btnBack.clicked.connect(self.back)
        self.btnSave.clicked.connect(self.handleSave)

        # GENERAL
        [self.prefTheme.itemAt(buttonID).widget().clicked.connect(self.handleTheme_standard) for buttonID in
         range(self.prefTheme.count() - 1)]
        self.prefTheme_CUSTOM.clicked.connect(self.handleTheme_custom)
        # TODO not implemented
        # [self.prefStageBackground.itemAt(buttonID).widget().clicked.connect(self.handleStageBackground_standard) for
        #  buttonID
        #  in range(self.prefStageBackground.count() - 1)]
        # self.prefStageBackground_CUSTOM.clicked.connect(self.handleStageBackground_custom)
        [self.prefOutputBackground.itemAt(buttonID).widget().clicked.connect(self.handleOutputBackground_standard) for
         buttonID
         in range(self.prefOutputBackground.count() - 1)]
        self.prefOutputBackground_CUSTOM.clicked.connect(self.handleOutputBackground_custom)

        # DISPLAY
        # self.prefStageDisplayID.activated.connect(self.setUnsaved)
        # self.prefStageDisplay_OFF.clicked.connect(lambda: self.handleEnableStageDisplay(False))
        # self.prefStageDisplay_ON.clicked.connect(lambda: self.handleEnableStageDisplay(True))

        self.prefOutputDisplayID.currentIndexChanged.connect(self.setUnsaved)
        # self.prefStageDisplayID.currentIndexChanged.connect(
        #     lambda: self.prefStageDisplayID_LABEL.setStyleSheet("") or self.setUnsaved())

        self.prefBackgroundMedia_OFF.clicked.connect(lambda: self.handleEnableBackgroundMedia(False))
        self.prefBackgroundMedia_ON.clicked.connect(lambda: self.handleEnableBackgroundMedia(True))

        [self.prefBackgroundAudio.itemAt(button).widget().clicked.connect(self.setUnsaved) for button in
         range(self.prefBackgroundAudio.count())]

        self.btnSystemSettings.clicked.connect(lambda: os.system("desk.cpl"))

        # [self.prefRemoteAPI.itemAt(button).widget().clicked.connect(self.setUnsaved) for button in range(self.prefRemoteAPI.count())] # TODO not implemented

    """
    Change theme schemes
    """
    def handleTheme_standard(self):
        self.lastbutton = [self.prefTheme_BLUE.isChecked(), self.prefTheme_RED.isChecked(),
                           self.prefTheme_GREY.isChecked(),
                           self.prefTheme_DARK.isChecked()].index(True)
        self.setUnsaved()

    def handleTheme_custom(self):
        """ 
        """
        inactive, checked, hover = self.customtheme
        result = colorPicker({"Inactive": inactive, "Checked": checked, "Hover": hover})
        if result:
            self.customtheme = tuple(result.values())
            self.lastbutton = 4
            self.setUnsaved()
        else:
            self.prefTheme.itemAt(self.lastbutton).widget().setChecked(True)

    def handleOutputBackground_standard(self):
        self.lastoutputbackground = [self.prefOutputBackground_BLACK.isChecked(),
                                     self.prefOutputBackground_WHITE.isChecked()].index(True)
        self.setUnsaved()

    def handleOutputBackground_custom(self):
        result = colorPicker(self.customoutputbackground)
        if result:
            self.customoutputbackground = result
            self.lastoutputbackground = 2
            self.setUnsaved()
        else:
            self.prefOutputBackground.itemAt(self.lastoutputbackground).widget().setChecked(True)

    # TODO not implemented
    # def handleStageBackground_standard(self):
    #     self.laststagebackground = [self.prefStageBackground_BLACK.isChecked(),
    #                                 self.prefStageBackground_WHITE.isChecked()].index(True)
    #     self.setUnsaved()
    #
    # def handleStageBackground_custom(self):
    #     result = colorPicker(self.customstagebackground)
    #     if result:
    #         self.customstagebackground = result
    #         self.laststagebackground = 2
    #         self.setUnsaved()
    #     else:
    #         self.prefStageBackground.itemAt(self.laststagebackground).widget().setChecked(True)

    def back(self):
        """
        Handle back button presses
        """

        # Check for saved changes and prompt about lost changes
        if self.btnSave.isEnabled():
            result = MODAL("Changes were made.\n\nSave?").exec_()
            if result == -1:
                return
            elif not result:
                self.updateSettingInterface()
            elif not self.handleSave():
                return
        selector.setCurrentIndex(0)

    def updateSettingInterface(self):
        """
        Update control states of preference control elements 
        """
        # GENERAL
        [self.prefTheme.itemAt(buttonID).widget().setChecked for buttonID in range(self.prefTheme.count())][
            themes.index(states["interface"]["theme"]) if states["interface"][
                                                              "theme"] in themes else self.prefTheme.count() - 1](
            True)
        [self.prefOutputBackground.itemAt(buttonID).widget().setChecked for buttonID in
         range(self.prefOutputBackground.count())][
            backgrounds.index(states["display"]["outputbackground"]) if states["display"][
                                                                            "outputbackground"] in backgrounds else self.prefOutputBackground.count() - 1](
            True)

        # TODO not implemented
        # [self.prefStageBackground.itemAt(buttonID).widget().setChecked for buttonID in
        #  range(self.prefStageBackground.count())][
        #     backgrounds.index(states["display"]["stagebackground"]) if states["display"][
        #                                                                    "stagebackground"] in backgrounds else self.prefStageBackground.count() - 1](
        #     True)

        # DISPLAY

        self.prefOutputDisplayID.setCurrentIndex(states["display"]["outputID"] - 1)
        # TODO not implemented
        # self.prefStageDisplayID.setCurrentIndex(states["display"]["stageID"] - 1)
        # self.prefStageDisplayID_LABEL.setStyleSheet("")
        # self.handleEnableStageDisplay(states["display"]["stageID"] > 0,
        #                               states["display"]["stageID"])  # Enable/display stage display
        # self.prefStageDisplay_ON.click() if states["display"][
        #     "stageID"] else self.prefStageDisplay_OFF.click()  # Set toggle control state

        self.handleEnableBackgroundMedia(bool(states["display"]["backgroundmedia"]))
        self.prefBackgroundMedia.itemAt(states["display"]["backgroundmedia"]).widget().setChecked(True)
        self.prefBackgroundAudio.itemAt(states["display"]["backgroundaudio"]).widget().setChecked(True)
        # self.prefRemoteAPI.itemAt(states["remote"]["apienabled"]).widget().setChecked(True)


        inactive, checked, hover = states["interface"]["theme"]
        self.theming.setStyleSheet(
            "QLabel[objectName='Header'] {background: #%s} "
            "QPushButton {background-color: #%s} "
            "QPushButton:checked {background-color: #%s} "
            "QPushButton:hover:!checked {background-color: #%s}" % (checked, inactive, checked, hover))

        self.btnSave.setEnabled(False)

    def setUnsaved(self):
        """
        Set unsaved state (by enabling the save button)
        """
        self.btnSave.setEnabled(True)

    def handleTabSwitch(self):
        """
        Handle tab switching events 
        """
        self.viewTabs.setCurrentIndex(
            [self.viewTabs_General.isChecked(), self.viewTabs_Display.isChecked(), self.viewTabs_Remote.isChecked(),
             self.viewTabs_About.isChecked()].index(True))

    # TODO not implemented
    # def handleEnableStageDisplay(self, state, screenID = None):
    #     self.prefStageDisplayID.setEnabled(state)
    #     self.prefStageDisplayID_LABEL.setEnabled(state)
    #     self.prefStageDisplayID.setCurrentIndex(
    #         -1 if not state else (screenID - 1 if screenID is not None else self.prefStageDisplayID.currentIndex()))

    def handleEnableBackgroundMedia(self, state):
        """
        Enables/Disables the background audio behaviour feature 
        """
        state = not state
        self.setUnsaved()
        self.prefBackgroundAudio_LABEL.setEnabled(state)
        [self.prefBackgroundAudio.itemAt(buttonID).widget().setEnabled(
            state) for buttonID in
            range(self.prefBackgroundAudio.count())]

    @staticmethod
    def saveChanges(key, value):
        """ 
        Save settings to registry and global store
        """
        parent, name = key.split("/")
        states[parent][name] = value
        QSettings.setValue(key, list(value) if isinstance(value, tuple) else value)

    def handleSave(self):
        """
        Saves configuration settings 
        """

        # Interface theme
        themeID = [self.prefTheme.itemAt(button).widget().isChecked() for button in
                   range(self.prefTheme.count())].index(True)
        self.saveChanges("interface/theme", self.customtheme if themeID == 4 else themes[themeID])

        # Output background colour
        outputbackgroundID = [self.prefOutputBackground.itemAt(button).widget().isChecked() for button in
                              range(self.prefOutputBackground.count())].index(True)
        self.saveChanges("display/outputbackground",
                         self.customoutputbackground if outputbackgroundID == 2 else backgrounds[outputbackgroundID])

        # TODO not implemented
        # stagebackgroundID = [self.prefStageBackground.itemAt(button).widget().isChecked() for button in
        #                      range(self.prefStageBackground.count())].index(True)
        # self.saveChanges("display/stagebackground",
        #                  self.customstagebackground if stagebackgroundID == 2 else backgrounds[stagebackgroundID])

        # TODO not implemented
        # if self.prefStageDisplay_ON.isChecked() and self.prefStageDisplayID.currentIndex() == -1:
        #     self.prefStageDisplayID_LABEL.setStyleSheet("color:red")
        #     print("Did not save: Some required settings missing")
        #     return False

        # Save background media behaviour
        self.saveChanges("display/backgroundmedia", 1 if self.prefBackgroundMedia_ON.isChecked() else 0)
        self.saveChanges("display/backgroundaudio", 1 if self.prefBackgroundAudio_ON.isChecked() else 0)

        # TODO not implemented
        # if states["display"]["stageID"] != self.prefStageDisplayID.currentIndex() + 1:
        #     self.saveChanges("display/stageID", self.prefStageDisplayID.currentIndex() + 1)

        # Output monitor
        if states["display"]["outputID"] != self.prefOutputDisplayID.currentIndex() + 1:
            self.saveChanges("display/outputID", self.prefOutputDisplayID.currentIndex() + 1)

        self.saveChanges("remote/apienabled", 1 if self.prefRemoteAPI_ON.isChecked() else 0)

        # Update interface theme
        inactive, checked, hover = states["interface"]["theme"]
        for ui in states["interface"]["ui"]:
            ui.theming.setStyleSheet(
                "QLabel[objectName='Header'] {background: #%s} "
                "QPushButton {background-color: #%s} "
                "QPushButton:checked {background-color: #%s} "
                "QPushButton:hover:!checked {background-color: #%s}" % (checked, inactive, checked, hover))

        # Reflect changed settings
        self.updateSettingInterface()

        # Update output windows
        output.draw()
        # stage.draw() # TODO not implemented

        dprint("Saved settings")
        self.btnSave.setEnabled(False)
        return True


# TODO not implemented
"""
# Stage Display Window
class displayStage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        dprint("Starting stage display")
        super(displayStage, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setStyleSheet("background: darkred;")
        self.draw()

    def draw(self):
        self.hide()
        if states["display"]["stageID"]:
            self.setGeometry(app.desktop().screenGeometry(states["display"]["stageID"] - 1))
            super(displayStage, self).showFullScreen()
"""


class MODAL(QtWidgets.QDialog, OnCue.forms_gen.modal.Ui_modal_ynoc):
    """
    Message box
    """

    def __init__(self, text, **kwargs):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self, text, **kwargs)

    def setupUi(self, MODAL, text, yes=True, no=True, cancel=True, ok=False, tool=True):
        super().setupUi(MODAL)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        if tool: self.setWindowFlags(self.windowFlags() | QtCore.Qt.Tool)
        # Change response button visibility
        if not ok: self.response.button(QtWidgets.QDialogButtonBox.Ok).hide()
        self.response.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(
            lambda: self.setResult(1)) if yes else self.response.button(QtWidgets.QDialogButtonBox.Yes).hide()
        self.response.button(QtWidgets.QDialogButtonBox.No).clicked.connect(
            lambda: self.setResult(0)) if no else self.response.button(QtWidgets.QDialogButtonBox.No).hide()
        self.response.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(
            lambda: self.setResult(-1)) if cancel else self.response.button(QtWidgets.QDialogButtonBox.Cancel).hide()
        self.message.setText(text)

        # Set theming
        [btn.setStyleSheet(
            "QPushButton {background-color: #BAB9BA; _background-color: #%s;} "
            "QPushButton:pressed {background-color: #%s} "
            "QPushButton:hover:!pressed {background-color: #%s}" % states["interface"]["theme"]) for btn in
            self.response.buttons()]


if __name__ == "__main__":
    # Create Qt Application instance
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # Constants
    themes = [("bab9ba", "509df3", "8cc5ff"), ("d8d8d8", "ff6666", "ffadad"), ("d8d8d8", "808080", "bcbcbc"),
              ("d8d8d8", "000000", "494949")]
    backgrounds = ["000000", "ffffff"]

    # Read preferences from registry
    QSettings = QtCore.QSettings("featherbear", "OnCue Projector")
    states = {
        'output': {},
        'display': {},
        'screens': {},
        'interface': {
            'ui': [],
            'theme': ()
        },
        'remote': {
            'apienabled': 0,
        },
        'versions': {}
    }
    states["display"]["outputID"] = QSettings.value("display/outputID", 2)
    # states["display"]["stageID"] = QSettings.value("display/stageID", 0) # TODO not implemented
    theme = QSettings.value("interface/theme", 0)
    states["interface"]["theme"] = tuple(QSettings.value("interface/theme", themes[0]))
    states["display"]["outputbackground"] = str(QSettings.value("display/outputbackground", backgrounds[0]))
    # states["display"]["stagebackground"] = str(QSettings.value("display/stagebackground", backgrounds[0])) # TODO not implemented
    states["display"]["backgroundmedia"] = QSettings.value("display/backgroundmedia", 0)
    states["display"]["backgroundaudio"] = QSettings.value("display/backgroundaudio", 0)
    # states["remote"]["apienabled"] = QSettings.value("remote/apienabled", 0) # TODO not implemented

    # Verify OS is Windows
    # TODO Cross-compatability
    platform = platform.system()
    print("OS is " + platform)
    if platform != "Windows": MODAL("Detected OS is not Windows. Program aborting", yes=False, no=False, cancel=False,
                                    ok=True, tool=False).exec_(); sys.exit("os")
    # states["osIsWindows"] = platform == "Windows" # TODO not implemented

    # Find latest version of PowerPoint present
    #print(win32com.client.Dispatch("PowerPoint.Application.XYZ").Version)
    states["versions"]["PowerPoint"] = None
    pptregistry = None
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office")
        for version in sorted(
                list(filter(lambda s: "." in s, [winreg.EnumKey(key, i) for i in range(winreg.QueryInfoKey(key)[0])])),
                reverse=True, key=lambda s: float(s)):
            try:
                pptregistry = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                             "Software\\Microsoft\\Office\\" + version + "\\PowerPoint\\Options",
                                             access=winreg.KEY_ALL_ACCESS)
                states["versions"]["PowerPoint"] = version
            except:
                continue
    except WindowsError:
        pass

    # Find versions of other components
    states["versions"]["Python"] = re.search(r'\(v(.+?),', sys.version).group(1)
    states["versions"]["Qt"] = QtCore.QT_VERSION_STR
    states["versions"]["PyQt"] = QtCore.PYQT_VERSION_STR
    states["versions"]["libVLC"] = Vlc.libvlc_get_version().decode('ascii')

    # Enumerate display monitors
    monitors = dict([((monitor["Monitor"][0], monitor["Monitor"][1]),
                      (monitor["Device"], win32api.EnumDisplayDevices(monitor["Device"]).DeviceString)) for monitor in
                     [win32api.GetMonitorInfo(display[0]) for display in win32api.EnumDisplayMonitors()]])

    # Populate monitor information
    for i in range(app.desktop().screenCount()):
        screen = app.desktop().screenGeometry(i)
        topleft = (screen.left(), screen.top())
        states["screens"][i + 1] = {
            'width': screen.width(),
            'height': screen.height(),
            'physical': monitors[topleft][0],
            'name': monitors[topleft][1],
        }

    dprint("Starting OnCue")

    # This application is to be used in a multi-monitor configuration - Output is disabled for single monitor setups
    if len(states["screens"]) == 1:
        errmsg = "Only one screen detected. Outputs disabled"
        dprint(errmsg)
        MODAL(errmsg, yes=False, no=False, cancel=False, ok=True, tool=False).exec_()

    # if states["remote"]["apienabled"]: _thread.start_new_thread(APIserver, ()) # TODO not implemented
    # Create output screens
    dprint("Creating output screens")
    # stage = displayStage() # TODO not implemented
    # stage.draw() # TODO not implemented
    output = OnCue.displays.displayOutput.displayOutput(
        dict(dprint=dprint, states=states, app=app, pptregistry=pptregistry, confine=OnCue.lib.utils.confine, Vlc=Vlc))
    output.draw()
    # Execute OnCue
    window = Application()
    window.show()
    sys.exit(app.exec_())
