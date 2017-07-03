@echo off
cd %~dp0/../source
rmdir /q /s build
"C:\Program Files (x86)\Python\3.6.0\python.exe" setup.py build