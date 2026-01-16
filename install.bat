@echo off
cd /d "%~dp0"
title Automated Matrix Inverter - Installation
color 0A

echo.
echo ============================================
echo   Automated Matrix Inverter - Installer
echo ============================================
echo.

:: Try different Python commands
set PYTHON_CMD=

:: Try 'python' first
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :python_found
)

:: Try 'python3'
python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    goto :python_found
)

:: Try 'py' (Python Launcher for Windows)
py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto :python_found
)

:: Python not found
echo [ERROR] Python is not installed or not in PATH.
echo.
echo Please install Python 3.8 or higher from:
echo    https://www.python.org/downloads/
echo.
echo IMPORTANT: Check "Add Python to PATH" during installation!
echo.
echo After installing Python, run this installer again.
echo.
pause
exit /b 1

:python_found
echo [OK] Python found using: %PYTHON_CMD%
%PYTHON_CMD% --version
echo.

:: Install sympy directly (most reliable method)
echo [INFO] Installing required packages...
echo.
%PYTHON_CMD% -m pip install --upgrade pip 2>nul
%PYTHON_CMD% -m pip install sympy

if %errorlevel% neq 0 (
    echo.
    echo [WARNING] pip install failed. Trying alternative method...
    %PYTHON_CMD% -m ensurepip --default-pip 2>nul
    %PYTHON_CMD% -m pip install sympy
)

echo.
echo ============================================
echo   Installation Complete!
echo ============================================
echo.
echo You can now run the application by:
echo   1. Double-clicking "run.bat"
echo   2. Or running: %PYTHON_CMD% Automated-Matrix-Inverter.py
echo.
echo.
set /p launch="Launch the application now? (Y/N): "
if /i "%launch%"=="Y" (
    echo.
    echo [INFO] Starting Automated Matrix Inverter...
    %PYTHON_CMD% Automated-Matrix-Inverter.py
)
if /i "%launch%"=="y" (
    echo.
    echo [INFO] Starting Automated Matrix Inverter...
    %PYTHON_CMD% Automated-Matrix-Inverter.py
)

pause
