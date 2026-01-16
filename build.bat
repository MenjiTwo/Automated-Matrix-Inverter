@echo off
cd /d "%~dp0"
title Building Automated Matrix Inverter

echo.
echo ========================================
echo   Building Executable...
echo ========================================
echo.

pyinstaller --onefile --windowed --name "MatrixInverter" --clean Automated-Matrix-Inverter.py

echo.
if exist "dist\MatrixInverter.exe" (
    echo [SUCCESS] Executable created!
    echo.
    echo Location: dist\MatrixInverter.exe
    echo.
    explorer dist
) else (
    echo [ERROR] Build failed.
)

pause
