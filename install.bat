@echo off
title Automated Matrix Inverter - Installation
color 0A

echo ============================================
echo   Automated Matrix Inverter - Installer
echo ============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [OK] Python found:
python --version
echo.

:: Install dependencies
echo [INFO] Installing required packages...
echo.
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [WARNING] Could not install from requirements.txt
    echo [INFO] Trying direct installation...
    pip install sympy
)

echo.
echo ============================================
echo   Installation Complete!
echo ============================================
echo.
echo To run the application:
echo   - Double-click "run.bat"
echo   - Or run: python Automated-Matrix-Inverter.py
echo.

set /p launch="Launch the application now? (Y/N): "
if /i "%launch%"=="Y" (
    echo.
    echo [INFO] Starting Automated Matrix Inverter...
    python Automated-Matrix-Inverter.py
)

pause
