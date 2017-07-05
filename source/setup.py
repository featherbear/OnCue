# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable
import sys, OnCue

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["oncue","win32com.client"], include_files = ["OnCue.ico", "D:\Program Files (x86)\VideoLAN\VLC\plugins", "D:\Program Files (x86)\VideoLAN\VLC\libvlc.dll", "D:\Program Files (x86)\VideoLAN\VLC\libvlccore.dll"], excludes = ["urllib", "logging", "imageformats", "unittest", "pydoc_data", "email", "html", "xml", "http"], optimize = 2, silent = False, build_exe = "../build/")

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('OnCue.py', base = base, copyright = "2017 Andrew Wong", icon = "OnCue.ico")
]

setup(name='OnCue Projector',
      version = OnCue.__VERSION__,
      description = 'OnCue Projector',
      options = dict(build_exe = buildOptions),
      executables = executables)
