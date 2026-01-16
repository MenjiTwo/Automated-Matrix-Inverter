#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Automated Matrix Inverter - Installer${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Detect OS
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
fi

echo -e "${YELLOW}[INFO]${NC} Detected OS: $OS"
echo ""

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PIP_CMD="pip3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PIP_CMD="pip"
else
    echo -e "${RED}[ERROR]${NC} Python is not installed."
    echo ""
    echo "Please install Python 3.8 or higher:"
    if [[ "$OS" == "macos" ]]; then
        echo "  brew install python"
        echo "  or download from https://www.python.org/downloads/"
    elif [[ "$OS" == "linux" ]]; then
        echo "  sudo apt-get install python3 python3-pip  (Ubuntu/Debian)"
        echo "  sudo dnf install python3 python3-pip      (Fedora)"
        echo "  sudo pacman -S python python-pip          (Arch)"
    fi
    exit 1
fi

echo -e "${GREEN}[OK]${NC} Python found: $($PYTHON_CMD --version)"
echo ""

# Check/Install tkinter
echo -e "${YELLOW}[INFO]${NC} Checking tkinter..."
if ! $PYTHON_CMD -c "import tkinter" &> /dev/null; then
    echo -e "${YELLOW}[WARNING]${NC} tkinter not found. Installing..."
    
    if [[ "$OS" == "linux" ]]; then
        # Detect package manager
        if command -v apt-get &> /dev/null; then
            echo -e "${YELLOW}[INFO]${NC} Using apt-get..."
            sudo apt-get update
            sudo apt-get install -y python3-tk
        elif command -v dnf &> /dev/null; then
            echo -e "${YELLOW}[INFO]${NC} Using dnf..."
            sudo dnf install -y python3-tkinter
        elif command -v pacman &> /dev/null; then
            echo -e "${YELLOW}[INFO]${NC} Using pacman..."
            sudo pacman -S --noconfirm tk
        elif command -v zypper &> /dev/null; then
            echo -e "${YELLOW}[INFO]${NC} Using zypper..."
            sudo zypper install -y python3-tk
        else
            echo -e "${RED}[ERROR]${NC} Could not detect package manager."
            echo "Please install python3-tk manually."
            exit 1
        fi
    elif [[ "$OS" == "macos" ]]; then
        echo -e "${YELLOW}[INFO]${NC} On macOS, tkinter should come with Python."
        echo "If missing, try: brew install python-tk"
    fi
else
    echo -e "${GREEN}[OK]${NC} tkinter is available"
fi
echo ""

# Upgrade pip
echo -e "${YELLOW}[INFO]${NC} Upgrading pip..."
$PYTHON_CMD -m pip install --upgrade pip --quiet

# Install dependencies
echo -e "${YELLOW}[INFO]${NC} Installing required packages..."
echo ""

if [[ -f "requirements.txt" ]]; then
    $PIP_CMD install -r requirements.txt
else
    $PIP_CMD install sympy
fi

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR]${NC} Failed to install dependencies."
    echo "Try running: $PIP_CMD install sympy"
    exit 1
fi

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}  Installation Complete!${NC}"
echo -e "${GREEN}============================================${NC}"
echo ""
echo "To run the application:"
echo "  ./run.sh"
echo "  or: $PYTHON_CMD Automated-Matrix-Inverter.py"
echo ""

# Ask to launch
read -p "Launch the application now? (y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo -e "${YELLOW}[INFO]${NC} Starting Automated Matrix Inverter..."
    $PYTHON_CMD Automated-Matrix-Inverter.py
fi
