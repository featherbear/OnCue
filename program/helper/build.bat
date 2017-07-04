@echo off
cd %~dp0/..

rmdir /S /Q build 2>nul

cd source
"C:\Program Files (x86)\Python\3.6.0\python.exe" setup.py build

:: Delete the files we don't need
cd ../build

cd PyQt5
rmdir /S /Q uic
cd Qt
rmdir /S /Q plugins
rmdir /S /Q qml
rmdir /S /Q resources
rmdir /S /Q translations
del bin\Qt5WebEngineCore.dll
cd ../..

cd plugins
rmdir /S /Q gui
rmdir /S /Q video_filter
rmdir /S /Q stream_out
rmdir /S /Q stream_filter
rmdir /S /Q access_output
rmdir /S /Q services_discovery
rmdir /S /Q visualization
cd ..

del Qt5Core.dll
del Qt5Gui.dll
del Qt5Svg.dll
del Qt5Widgets.dll