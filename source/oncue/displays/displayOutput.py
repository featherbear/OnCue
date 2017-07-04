# -*- coding: utf-8 -*-
"""
OnCue Projector
Copyright 2017 Andrew Wong <featherbear@navhaxs.au.eu.org>

The following code is licensed under the GNU Public License Version v3.0
"""


# Imports
import winreg

import win32com.client
from PyQt5 import QtCore, QtWidgets


class displayOutput(QtWidgets.QWidget):
    """
    Output display class
    """

    def __init__(self, components: dict):
        # Initialise class
        self.dprint = components["dprint"]
        self.states = components["states"]
        self.app = components["app"]
        self.pptregistry = components["pptregistry"]
        self.confine = components["confine"]
        self.Vlc = components["Vlc"]
        self.vlc = self.Vlc.Instance()

        self.dprint("Starting output display")
        super(displayOutput, self).__init__(None, QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)

        gridLayout = QtWidgets.QGridLayout(self)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setSpacing(0)
        self.foreground = QtWidgets.QWidget(self)
        gridLayout.addWidget(self.foreground)
        self.player = self.vlc.media_player_new()
        # self.overlay = QtWidgets.QWidget(None, QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)

        # Initialise variables
        self.VLCmedia = None
        self.type = None
        self.VLCpaused = None
        self.VLCpaused_c = None
        self.VLCmuted_c = None
        self.PPTapplication = None
        self.PPTpresentation = None
        self.screen = None
        self.overlay = QtWidgets.QWidget(None, QtCore.Qt.WindowStaysOnTopHint)
        self.overlay.setWindowOpacity(0)
        self.draw()

        """ Not using VLC's event manager, it seems very buggy """
        # eventmanager = self.player.event_manager()
        # eventmanager.event_attach(Vlc.EventType.MediaPlayerPositionChanged, states["mediaSignals"]["update"])
        # eventmanager.event_attach(Vlc.EventType.MediaPlayerPaused, states["mediaSignals"]["pause"])
        # eventmanager.event_attach(Vlc.EventType.MediaPlayerPlaying, states["mediaSignals"]["play"])
        # eventmanager.event_attach(Vlc.EventType.MediaPlayerEndReached, states["mediaSignals"]["finish"])

    def draw(self):
        """
        Create output window 
        """
        if len(self.states["screens"]) != 1:
            self.hide()
            self.setStyleSheet("background: #" + self.states["display"]["outputbackground"])
            self.screen = self.app.desktop().screenGeometry(self.states["display"]["outputID"] - 1)
            self.setGeometry(self.screen)
            super(displayOutput, self).showFullScreen()

    def clear(self, bypass=False):
        """
        Clear output content 
        """
        if not bypass and self.type == "powerpoint":
            self.PPTpresentation.Close()
            self.overlay.hide()
        self.VLCstop()
        self.type = None
        self.VLCpaused = None
        self.VLCpaused_c = None

    def PPTclose(self):
        """
        Closes the presentation
        """
        try:
            self.PPTpresentation.Close()
        except:
            pass

    def PPTslide(self, slide: int):
        """
        Change current slide 
        """
        try:
            self.PPTpresentation.SlideShowWindow.View.GotoSlide(slide)
        except:
            pass

    def PPTnext(self):
        """
        Go to next slide 
        """
        try:
            self.PPTpresentation.SlideShowWindow.View.Next()
        except:
            pass

    def PPTprevious(self):
        """
        Go to previous slides 
        """
        try:
            self.PPTpresentation.SlideShowWindow.View.Previous()
        except:
            pass

    class PPTevents:
        """
        Handle PowerPoint COM events
        """
        updateSlide = None

        def OnSlideShowNextSlide(self, s):
            self.updateSlide(s.View.CurrentShowPosition - 1)

            # def OnSlideShowEnd(self, s):
            #     self.clear()

    def load(self, data):
        """
        Prepare the content for display
        """
        self.type = data["type"]
        if self.type == "powerpoint":
            if not self.pptregistry: return False
            # https://mail.python.org/pipermail/python-win32/2012-July/012471.html
            self.PPTapplication = win32com.client.DispatchWithEvents("PowerPoint.Application", self.PPTevents)
            try:
                self.PPTpresentation = self.PPTapplication.Presentations.Open(data["path"].replace("/", "\\"),
                                                                              WithWindow=False)
                # Change PowerPoint output monitor setting (Touch and revert)
                reset = []
                try:
                    reset.append((winreg.QueryValueEx(self.pptregistry, "UseAutoMonSelection")[0],
                                  lambda value: winreg.SetValueEx(self.pptregistry, "UseAutoMonSelection", 0,
                                                                  winreg.REG_DWORD,
                                                                  value)))
                except WindowsError:
                    reset.append((None, lambda _: winreg.DeleteValue(self.pptregistry, "UseAutoMonSelection")))
                try:
                    reset.append((winreg.QueryValueEx(self.pptregistry, "DisplayMonitor")[0],
                                  lambda value: winreg.SetValueEx(self.pptregistry, "DisplayMonitor", 0, winreg.REG_SZ,
                                                                  value)))
                except WindowsError:
                    reset.append((None, lambda _: winreg.DeleteValue(self.pptregistry, "DisplayMonitor")))

                winreg.SetValueEx(self.pptregistry, "DisplayMonitor", 0, winreg.REG_SZ,
                                  self.states["screens"][self.states["display"]["outputID"]]["physical"])

                winreg.SetValueEx(self.pptregistry, "UseAutoMonSelection", 0, winreg.REG_DWORD, 0)

                self.PPTpresentation.SlideShowSettings.ShowPresenterView = False
                self.PPTpresentation.SlideShowSettings.Run()
                self.PPTpresentation.SlideShowWindow.View.AcceleratorsEnabled = False
                self.overlay.setGeometry(self.screen)
                self.overlay.showFullScreen()
                [action(value) for value, action in reset]
            except Exception as e:
                print(e)
        else:
            # Play with VLC
            self.player.set_hwnd(int(self.foreground.winId()))
            self.VLCmedia = self.vlc.media_new(data["path"])
            self.player.set_media(self.VLCmedia)

    def VLCposition(self):
        """
        Get media progress (percentage) 
        """
        return self.player.get_position()

    # TODO not implemented
    # def VLCseek(self, pc):
    #     if self.type != "media":
    #         return
    #     self.player.set_position(self.confine(pc, 0.0, 1.0))
    #     self.player.play()

    def VLCpause(self):
        """
        Pause the media
        """
        if self.type != "media":
            return
        self.player.set_pause(True)
        self.VLCpaused_c = True

    def VLCplay(self):
        """
        Play/Resume the media
        """
        if self.type != "media":
            return
        self.player.play()
        self.VLCpaused_c = False

    def VLCstop(self):
        """
        Stop the media
        """
        if self.type != "media":
            return
        self.player.stop()

    def VLCmute(self, state):
        """
        Mute audio
        """
        if self.type != "media":
            return
        self.player.audio_set_mute(state)
        self.VLCmuted_c = state

    def contentShow(self):
        """
        Shows content on the output window
        """
        if self.type == "media" and self.VLCpaused:
            if not self.VLCmuted_c: self.player.audio_set_mute(False)  # Only unmute if the user did not force mute
            if not self.VLCpaused_c: self.player.play()  # Only resume if the user did not force pause
            self.VLCpaused = False
        self.show()
        self.foreground.show()

    def contentHide(self):
        """
        Hides content in the output window
        """
        if self.type == "media":
            if self.states["display"]["backgroundmedia"]:
                self.player.set_pause(True)  # Check background media behaviour
            elif self.states["display"]["backgroundaudio"]:
                self.player.audio_set_mute(True)  # Check background media behaviour
            self.VLCpaused = True
        self.foreground.hide()
        self.show()

    def contentDesktop(self):
        """
        Reveals the desktop
        """
        self.contentHide()
        self.hide()
