@echo off
cd %~dp0
title OnCue Projector Setup Packager
call build.bat
cd %~dp0
"D:\Program Files (x86)\Inno Setup 5\iscc.exe" "OnCue Projector.iss"