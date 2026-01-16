#!/bin/bash

# Find Python command
if command -v python3 &> /dev/null; then
    python3 Automated-Matrix-Inverter.py
elif command -v python &> /dev/null; then
    python Automated-Matrix-Inverter.py
else
    echo "Error: Python is not installed."
    echo "Please run ./install.sh first."
    exit 1
fi
