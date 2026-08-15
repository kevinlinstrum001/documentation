@echo off
setlocal

rem ------------------------------------------------------------
rem Klinswork Documentation Viewer launcher
rem ------------------------------------------------------------

rem Normalize paths so they do NOT end in a trailing backslash.
for %%I in ("%~dp0.") do set "VIEWER_ROOT=%%~fI"
for %%I in ("%~dp0..\..") do set "DOCUMENTATION_ROOT=%%~fI"

set "VIEWER=%VIEWER_ROOT%\tools\json-viewer-v1.6.0.py"
set "MANIFEST_BUILDER=%DOCUMENTATION_ROOT%\documentation-viewer-manifest.py"

echo Klinswork Documentation Viewer
echo.

rem ------------------------------------------------------------
rem Refresh source-aware Documentation Viewer manifest
rem ------------------------------------------------------------

if exist "%MANIFEST_BUILDER%" (
    echo Refreshing Documentation Viewer manifest...
    py -3 "%MANIFEST_BUILDER%" --documentation-root "%DOCUMENTATION_ROOT%"
    echo.
) else (
    echo WARNING: Documentation Viewer manifest builder not found:
    echo %MANIFEST_BUILDER%
    echo.
)

rem ------------------------------------------------------------
rem Verify local Viewer
rem ------------------------------------------------------------

if not exist "%VIEWER%" (
    echo ERROR: Local Viewer not found:
    echo %VIEWER%
    echo.
    pause
    exit /b 1
)

rem ------------------------------------------------------------
rem Launch local Viewer
rem ------------------------------------------------------------

echo Starting local viewer...
py -3 "%VIEWER%" --folder "%VIEWER_ROOT%"
set "EXIT_CODE=%ERRORLEVEL%"

if not "%EXIT_CODE%"=="0" (
    echo.
    echo ERROR: Viewer exited with code %EXIT_CODE%.
    echo.
    pause
    exit /b %EXIT_CODE%
)

endlocal