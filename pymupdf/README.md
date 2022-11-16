## Installation
- Since `pymupdf` is simply a wrapper around `mupdf`, different Linux distros need to install `mupdf` differently:
    - Fedora: `dnf install mupdf`
    - Arch Linux: `pacman -S mupdf`
- Then, to install, `pip install pymupdf`


## Usage
- `import fitz`, not `import pymupdf`. Cf. [here for the naming](https://github.com/pymupdf/PyMuPDF/wiki)
- Check version by `fitz.__doc__`, not by `fitz.__version__`, which does not even exist
- [OCR-like usage](https://pymupdf.readthedocs.io/en/latest/app1.html#blocks)









