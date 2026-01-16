# Automated Matrix Inverter

A modern, user-friendly GUI application for computing matrix inverses using the Gauss-Jordan elimination method. Built with Python and Tkinter, featuring a clean interface with dark/light theme support.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

| Feature | Description |
|---------|-------------|
| **Matrix Sizes** | Supports 2×2 up to 10×10 matrices |
| **Symbolic Math** | Handles fractions, decimals, and algebraic variables (a, b, c...) |
| **Step-by-Step** | Shows all elementary row operations performed |
| **Theme Toggle** | Switch between light and dark modes |
| **Format Toggle** | View results as fractions or decimals |
| **Modern UI** | Rounded buttons and smooth visual design |

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.8 or higher |
| sympy | Latest |
| tkinter | Included with Python |

---

## Quick Installation

### Windows

**Option 1: One-Click Install**
1. Download or clone this repository
2. Double-click `install.bat`
3. When prompted, type `Y` and press Enter to launch

**Option 2: Manual Install (Recommended if Option 1 fails)**

Open **Command Prompt** or **PowerShell**, then run:
```cmd
# Navigate to the project folder (change path as needed)
cd "C:\path\to\Automated-Matrix-Inverter"

# Install the required package
pip install sympy

# Run the application
python Automated-Matrix-Inverter.py
```

> **Note:** If `python` doesn't work, try `py` or `python3` instead.

**Option 3: One-Liner (Copy & Paste)**
```cmd
pip install sympy && python Automated-Matrix-Inverter.py
```

---

### macOS / Linux

**Option 1: One-Click Install**
```bash
chmod +x install.sh && ./install.sh
```

**Option 2: Manual Install**

Open **Terminal** and run:
```bash
# Navigate to the project folder
cd /path/to/Automated-Matrix-Inverter

# Install sympy
pip3 install sympy

# Run the application
python3 Automated-Matrix-Inverter.py
```

**Linux Users - Install tkinter first (if not installed):**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

**macOS Users:**
```bash
# If using Homebrew Python
brew install python-tk
```

---

## Dependencies

All dependencies are automatically installed by the installation scripts.

| Package | Purpose |
|---------|---------|
| `sympy` | Symbolic mathematics library for matrix operations |

---

## How to Use

1. **Launch the application** using the install script or manually
2. **Select matrix size** (2×2 to 10×10) from the dropdown
3. **Click "Generate Matrix"** to create the input grid
4. **Enter values** in each cell (supports numbers, fractions like `1/2`, or variables like `a`, `b`)
5. **Click "Calculate"** to compute the inverse
6. **View results** showing the original matrix and its inverse
7. **Toggle format** between fractions and decimals using the button
8. **Review operations** in the right panel showing all Gauss-Jordan steps

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `'python' is not recognized` | Try using `py` or `python3` instead. Or reinstall Python and check "Add to PATH" |
| `ModuleNotFoundError: No module named 'sympy'` | Run `pip install sympy` (or `pip3 install sympy` on macOS/Linux) |
| `ModuleNotFoundError: No module named 'tkinter'` | **Linux:** `sudo apt-get install python3-tk` **macOS:** `brew install python-tk` |
| `install.bat` doesn't work | Right-click → "Run as administrator" OR use Manual Install steps above |
| Nothing happens when double-clicking `.py` file | Use Command Prompt/Terminal to run manually (see Manual Install) |

---

## Project Structure

```
LinAlg/
├── Automated-Matrix-Inverter.py   # Main application
├── install.bat                     # Windows installer
├── install.sh                      # macOS/Linux installer
├── requirements.txt                # Python dependencies
├── run.bat                         # Windows launcher
├── run.sh                          # macOS/Linux launcher
└── README.md                       # This file
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**MenjiTwo**

---

## Acknowledgments

- [SymPy](https://www.sympy.org/) - Python library for symbolic mathematics
- Gauss-Jordan elimination algorithm for matrix inversion
