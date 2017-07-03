# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["OnCue"], include_files =["OnCue.ico","D:\Program Files (x86)\VideoLAN\VLC\plugins","D:\Program Files (x86)\VideoLAN\VLC\libvlc.dll","D:\Program Files (x86)\VideoLAN\VLC\libvlccore.dll"], excludes = [], optimize=2, silent=False, build_exe="../build/")

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('OnCue.py', base=base, copyright="Andrew Wong 2017",icon="OnCue.ico")
]

setup(name='OnCue Projector',
      version = '0.0.0.1',
      description = 'OnCue Projector',
      options = dict(build_exe = buildOptions),
      executables = executables)
