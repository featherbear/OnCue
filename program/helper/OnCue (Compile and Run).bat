@echo off
set nul=^>nul 2^>nul
cd /d %~dp0\..\source
title OnCue Development

cd OnCue\forms_gen
if %ERRORLEVEL%==1 echo Failed to change directory? && pause && exit
del *.py* %nul%
for %%f in (*.ui) do (
echo ^> Compiling %%f...
pyuic5 "%%f" -o "%%~nf.py"
)
echo # -*- coding: utf-8 -*->__init__.py
echo ^"^"^">>__init__.py
echo OnCue Projector>>__init__.py
echo Copyright 2017 Andrew Wong ^<featherbear@navhaxs.au.eu.org^>>>__init__.py
echo.>>__init__.py
echo The following code is licensed under the GNU Public License Version v3.0>>__init__.py
echo ^"^"^">>__init__.py
echo.>>__init__.py
echo import pkgutil; __path__ = pkgutil.extend_path(__path__, __name__); [__import__(modname) for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.')]>>__init__.py

cd ..\..

if [%1]==[-norun] exit /b

echo.
echo ^> Executing OnCue
echo.
echo [------ %date% %time% ------]
echo.

"C:\Program Files (x86)\Python\3.6.0\python.exe" OnCue.py

echo.
echo OnCue quit (%ERRORLEVEL%)

echo.
echo [------ %date% %time% ------]
echo.
echo ^> Application terminated... Closing in 3 seconds

timeout /t 3 >nul

exit /b