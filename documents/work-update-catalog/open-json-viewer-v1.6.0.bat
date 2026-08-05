@echo off
setlocal
cd /d "%~dp0"

set "VIEWER=%~dp0tools\json-viewer-v1.6.0.py"
set "CONTENT_ROOT=%~dp0."

echo Local JSON Explorer launcher v1.6.0
echo.
echo Application:
echo %VIEWER%
echo.
echo Content root:
echo %CONTENT_ROOT%
echo.

if not exist "%VIEWER%" (
    echo ERROR: Viewer script was not found.
    echo Expected:
    echo %VIEWER%
    echo.
    pause
    exit /b 1
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "%VIEWER%" --folder "%CONTENT_ROOT%"
    set "EXIT_CODE=%ERRORLEVEL%"
    goto :after_python
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "%VIEWER%" --folder "%CONTENT_ROOT%"
    set "EXIT_CODE=%ERRORLEVEL%"
    goto :after_python
)

echo ERROR: Python 3 was not found.
echo Install Python 3, then run this launcher again.
echo.
pause
exit /b 1

:after_python
if not "%EXIT_CODE%"=="0" (
    echo.
    echo ERROR: JSON Explorer exited with code %EXIT_CODE%.
    echo The error shown above identifies the failure.
    echo.
    pause
)

endlocal