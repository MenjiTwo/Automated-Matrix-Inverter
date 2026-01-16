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

## Installation

### Windows (Executable)

**No Python required!**

1. Clone or download this repository
2. Open the `dist` folder
3. Double-click `MatrixInverter.exe`

---

### Windows (From Source)

1. **Install Python 3.8+** from [python.org](https://www.python.org/downloads/)
   - ⚠️ Check **"Add Python to PATH"** during installation

2. **Open Command Prompt** and navigate to the project folder:
   ```cmd
   cd "C:\path\to\Automated-Matrix-Inverter"
   ```

3. **Install the required package:**
   ```cmd
   pip install sympy
   ```

4. **Run the application:**
   ```cmd
   python Automated-Matrix-Inverter.py
   ```

> **Tip:** If `python` doesn't work, try `py` or `python3` instead.

---

### macOS

1. **Install Python 3.8+** from [python.org](https://www.python.org/downloads/) or via Homebrew:
   ```bash
   brew install python
   ```

2. **Open Terminal** and navigate to the project folder:
   ```bash
   cd /path/to/Automated-Matrix-Inverter
   ```

3. **Install the required package:**
   ```bash
   pip3 install sympy
   ```

4. **Run the application:**
   ```bash
   python3 Automated-Matrix-Inverter.py
   ```

---

### Linux

1. **Install Python and tkinter:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3 python3-pip python3-tk

   # Fedora
   sudo dnf install python3 python3-pip python3-tkinter

   # Arch
   sudo pacman -S python python-pip tk
   ```

2. **Navigate to the project folder:**
   ```bash
   cd /path/to/Automated-Matrix-Inverter
   ```

3. **Install the required package:**
   ```bash
   pip3 install sympy
   ```

4. **Run the application:**
   ```bash
   python3 Automated-Matrix-Inverter.py
   ```

---

## How to Use

1. **Launch the application** using the steps above
2. **Select matrix size** (2×2 to 10×10) from the dropdown
3. **Click "Generate Matrix"** to create the input grid
4. **Enter values** in each cell:
   - Numbers: `5`, `-3`, `0.5`
   - Fractions: `1/2`, `3/4`
   - Variables: `a`, `b`, `x`
5. **Click "Calculate"** to compute the inverse
6. **View results** showing the original matrix and its inverse
7. **Toggle format** between fractions and decimals
8. **Review operations** in the right panel showing all Gauss-Jordan steps

---

## Build Executable (Windows)

To create your own `.exe` file:

```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name "MatrixInverter" Automated-Matrix-Inverter.py
```

Or simply double-click `build.bat`.

The executable will be created in the `dist/` folder.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `'python' is not recognized` | Use `py` or `python3` instead, or reinstall Python with "Add to PATH" checked |
| `ModuleNotFoundError: No module named 'sympy'` | Run `pip install sympy` (or `pip3` on macOS/Linux) |
| `ModuleNotFoundError: No module named 'tkinter'` | **Linux:** `sudo apt-get install python3-tk` |
| `.exe` blocked by Windows | Click "More info" → "Run anyway" |

---

## Project Structure

```
Automated-Matrix-Inverter/
├── Automated-Matrix-Inverter.py   # Main application source code
├── build.bat                       # Script to build .exe (Windows)
├── dist/
│   └── MatrixInverter.exe          # Standalone executable (Windows)
├── LICENSE                         # MIT License
└── README.md                       # This file
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| [SymPy](https://www.sympy.org/) | Symbolic mathematics for matrix operations |
| tkinter | GUI framework (included with Python) |

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**[MenjiTwo](https://github.com/MenjiTwo)**
