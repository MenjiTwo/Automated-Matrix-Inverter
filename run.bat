@echo off
cd /d "%~dp0"

:: Try different Python commands
python --version >nul 2>&1
if %errorlevel% equ 0 (
    python Automated-Matrix-Inverter.py
    exit /b
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    py Automated-Matrix-Inverter.py
    exit /b
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    python3 Automated-Matrix-Inverter.py
    exit /b
)

echo [ERROR] Python not found. Please install Python first.
pause
