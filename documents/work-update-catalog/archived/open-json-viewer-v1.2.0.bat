@echo off
setlocal
cd /d "%~dp0"

echo Local JSON Explorer launcher v1.2.0
echo Launching:
echo %~dp0json-viewer-v1.2.0.py
echo.

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "%~dp0json-viewer-v1.2.0.py"
    goto :end
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "%~dp0json-viewer-v1.2.0.py"
    goto :end
)

echo Python 3 was not found.
echo Install Python 3, then run this file again.
pause

:end
endlocal
