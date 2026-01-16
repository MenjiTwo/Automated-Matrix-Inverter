# Automated Matrix Inverter

A simple GUI app for calculating matrix inverses using Gauss-Jordan elimination.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Download & Run (Windows)

1. Go to [**Releases**](https://github.com/MenjiTwo/Automated-Matrix-Inverter/releases)
2. Download `MatrixInverter.exe`
3. Double-click to run — **no installation needed!**

---

## Features

- Matrix sizes from **2×2 to 10×10**
- Supports **fractions** (`1/2`), **decimals**, and **variables** (`a`, `b`, `c`)
- Shows **step-by-step** Gauss-Jordan operations
- **Dark/Light theme** toggle
- **Fraction/Decimal** display toggle

---

## Run from Source (All Platforms)

If you prefer running from Python source code:

### 1. Install Python
Download from [python.org](https://www.python.org/downloads/) (check "Add to PATH")

### 2. Install dependency
```bash
pip install sympy
```

### 3. Run
```bash
python Automated-Matrix-Inverter.py
```

> **Linux users:** You may need to install tkinter first:  
> `sudo apt-get install python3-tk` (Ubuntu/Debian)

---

## Build Executable Yourself

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "MatrixInverter" Automated-Matrix-Inverter.py
```

The `.exe` will be in the `dist/` folder.

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Made by [MenjiTwo](https://github.com/MenjiTwo)**
