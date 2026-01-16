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

**Option 1: One-Click Install (Recommended)**
```cmd
install.bat
```

**Option 2: Manual Install**
```cmd
pip install sympy
python Automated-Matrix-Inverter.py
```

---

### macOS / Linux

**Option 1: One-Click Install (Recommended)**
```bash
chmod +x install.sh
./install.sh
```

**Option 2: Manual Install**
```bash
# Install tkinter if not present (Linux only)
# Ubuntu/Debian:
sudo apt-get install python3-tk

# Fedora:
sudo dnf install python3-tkinter

# macOS (tkinter comes with Python from python.org or brew)
brew install python-tk

# Install dependencies and run
pip3 install sympy
python3 Automated-Matrix-Inverter.py
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
| `ModuleNotFoundError: No module named 'sympy'` | Run `pip install sympy` or use the install script |
| `ModuleNotFoundError: No module named 'tkinter'` | Install tkinter for your OS (see installation section) |

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
